#!/usr/bin/python
#This file (with update option set) is run daily; it pulls new clan members and new accounts. For existing members, it adds newly created characters, and updates all existing stats.
#Perhaps most importantly, it pulls in new activities completed by all members.
import os
import sys
import json
import time
import sqlite3
import requests
import itertools
from datetime import datetime
from initdb import Base, Bungie, Account, PvPAggregate, PvEAggregate, Character, AccountWeaponUsage, CharacterActivityStats, AccountMedals, ActivityReference, ClassReference, WeaponReference, ActivityTypeReference, BucketReference, AccountActivityModeStats, LastUpdated
from destinygotg import Session, load_config
from functools import partial
import tableGenerator

URL_START = "https://bungie.net/Platform"
OLD_URL_START = "https://bungie.net/d1/Platform"
UPDATE_DIFF = 1 # Number of days between updates
# write_files = False
write_files = True

def make_header():
    return {'X-API-KEY':os.environ['BUNGIE_APIKEY']}

def timeit(func, args=None):
    start_time = time.clock()
    if args == None:
        func()
    else:
        func(args)
    print("--- %s seconds ---" % (time.clock() - start_time))

def build_db():
    """Main function to build the full database"""
    start_time = time.clock()
    session = Session()
    # handle_bungie_table()
    # handle_account_table()
    handle_character_table()
    # handle_aggregate_tables()
    # handle_weapon_usage_table()
    # handle_activity_stats_table()
    # handle_medal_table()
    # handle_account_activity_mode_stats_table()
    # handle_reference_tables()
    print("--- %s seconds ---" % (time.clock() - start_time))

#info_map = {'attrs':{'attr1':'attr1Name', ...}
#           ,'kwargs':{'kwargs1':'attr1', ...}
#           ,'url_params':{'param1':'attr1', ...}
#           ,'values':{'value1':'location1', ...}
#           ,'statics':{'static1':'attr1', ...}
#           ,'primary_keys':{'key_name1':'attr1', ...}}

def request_and_insert(session, request_session, info_map, static_map, url, out_file, message, iterator, table):
    """Does everything else"""
    #Figure out if we need to update. We have kwargs and the table name, so just check LastUpdated for it.
    add_list = []
    #Actual request done here
    data = json_request(request_session, url, out_file, message)
    if data is None:
        print("No data retrieved.")
        return []
    #dynamic_dict_index gives us the specific iterator in the json we'll be using - could be games, characters, weapons, etc.
    group = dynamic_dict_index(data, iterator)
    if group == None:
        print("Nothing to insert.")
        return []
    #Sometimes we get arrays, other times we get dictionaries. Wrap the dicts in a list to avoid headache later.
    # tableGenerator.table_generator(iterator, group)
    if type(group) == dict:
        group = group.values()
    #gonna insert some hacky code in here to generate a table in initdb
    for elem in group:
        if elem == None:
            continue
        #build_dict uses a nifty dynamic dictionary indexing function that allows us to grab info from multiply-nested fields in the dict
        insert_dict = build_dict(elem, info_map['values'])
        print(insert_dict)
        if table == Character:
            #Hackily convert the dates. Not sure how else to do this.
            insert_dict["last_played"] = datetime.strptime(insert_dict["last_played"], "%Y-%m-%dT%H:%M:%SZ")
        #Statics are pre-defined values - maybe the id from user.id in define_params
        if 'statics' in info_map:
            insert_dict = {**insert_dict, **static_map}
        #Create a new element for insertion using kwargs
        insert_elem = table(**insert_dict)
        primary_key_map = {}
        for key in info_map['primary_keys']:
            primary_key_map[key] = getattr(insert_elem, key)
        #Upsert the element
        add_list.append(upsert(table, primary_key_map, insert_elem, session))
    #Get rid of the None elements - they've been updated already
    add_list = [item for item in add_list if item is not None]
    return add_list

def define_params(query_table, info_map, url_function, iterator, table, alt_insert=None):
    """Does like everything"""
    #Build a single request session for the duration of the table creation
    request_session = requests.session()
    session = Session()
    total_add_list = []
    #Elems is what we'll be iterating through - could be users, characters, etc.
    elems = session.query(query_table).all()
    for elem in elems:
        #Attrs are the attributes associated with the elem. User.id or user.membership_type, for example. AKA fields in the database.
        attr_map = {}
        for (key, value) in info_map['attrs'].items():
            if query_table == Character:
                try: 
                    attr_map[key] = getattr(elem, value)
                except AttributeError:
                    attr_map[key] = getattr(session.query(Account).filter_by(id=attr_map['membershipId']).first(), value)
            else:
                attr_map[key] = getattr(elem, value)
        #url_params are used to build the request URL.
        url_params = build_value_dict(info_map['url_params'], attr_map)
        url = url_function(**url_params)
        out_file = f"{attr_map['name']}_{table.__tablename__}.json"
        message = f"Fetching {table.__tablename__} data for: {attr_map['name']}"
        #Statics actually need to get passed to the insert function so they can be put in the table.
        static_map = build_value_dict(info_map['statics'], attr_map)
        #Kwargs are used to check if the database needs updating for the current elem.
        kwargs = build_value_dict(info_map['kwargs'], attr_map)
        kwargs['table_name'] = table.__tablename__
        to_update = needs_update(kwargs, session)
        to_update = True
        if not to_update:
            print(f"Not updating {table.__tablename__} table for user: {attr_map['name']}")
            add_list = []
        elif alt_insert == None:
            add_list = request_and_insert(session, request_session, info_map, static_map, url, out_file, message, iterator, table)
        else:
            add_list = alt_insert(session, request_session, info_map, static_map, url, out_file, message, iterator, table)
        total_add_list = total_add_list + add_list
        #Upsert into LastUpdated
        if table != AccountActivityModeStats:
            update_id = attr_map[info_map['kwargs']['id']]
            update_item = set_last_updated(update_id, table, session)
            total_add_list = total_add_list + [update_item]
    total_add_list = [item for item in total_add_list if item is not None]
    final_list = remove_duplicates(total_add_list)
    session.add_all(final_list)
    session.commit()

def handle_bungie_table():
    """Fills Bungie table with all users in the clan"""
    # Destiny 2 changes results per page to be 100. Because there is a max of 100 people in the clan, we don't need the extra stuff here anymore.
    # The Bungie table is going to match the account table for a while...
    session = Session()
    request_session = requests.Session()
    info_map = {'values' :{'id':[['bungieNetUserInfo', 'membershipId']]
                         ,'id_2':[['destinyUserInfo', 'membershipId']]
                         ,'bungie_name':[['bungieNetUserInfo', 'displayName']]
                         ,'bungie_name_2':[['destinyUserInfo', 'displayName']]
                         ,'membership_type':[['bungieNetUserInfo', 'membershipType']]
                         ,'membership_type_2':[['destinyUserInfo', 'membershipType']]}
              ,'kwargs' :{'id' : 'id'}
              ,'primary_keys' :['id']}
    clan_url = f"{URL_START}/GroupV2/{os.environ['BUNGIE_CLANID']}/Members/?currentPage=1"
    out_file = "clanUsers.json"
    message = "Fetching list of clan users."
    iterator = ['Response', 'results']
    table = Bungie
    add_list = request_and_insert(session, request_session, info_map, {}, clan_url, out_file, message, iterator, table)
    final_list = remove_duplicates(add_list)
    session.add_all(final_list)
    session.commit()

def handle_account_table():
    """Retrieve JSONs for users, listing their Destiny accounts. Fills account table."""
    def account_url(id, membershipType):
        return f"{URL_START}/User/GetMembershipsById/{id}/{membershipType}"
    query_table = Bungie
    info_map = {'attrs'  :{'id'             : 'id'
                         ,'name'           : 'bungie_name'
                         ,'membershipType' : 'membership_type'}
              ,'kwargs' :{'id' : 'id'}
              ,'url_params' :{'id'             : 'id'
                             ,'membershipType' : 'membershipType'}
              ,'values' :{'id'              : [['membershipId']]
                         ,'membership_type' : [['membershipType']]
                         ,'display_name'    : [['displayName']]}
              ,'statics' :{'bungie_id' : 'id'}
              ,'primary_keys' : ['id']}
    iterator = ['Response', 'destinyMemberships']
    table = Account
    define_params(query_table, info_map, account_url, iterator, table)

def handle_character_table():
    def character_url(membershipId, membershipType):
        return f"{URL_START}/Destiny2/{membershipType}/Profile/{membershipId}/?components=200"
    query_table = Account
    info_map = {'attrs' :{'membershipId' : 'id'
                        ,'name' : 'display_name'
                        ,'membershipType' : 'membership_type'}
              ,'kwargs' :{'id' : 'membershipId'}
              ,'url_params' :{'membershipId' : 'membershipId'
                             ,'membershipType' : 'membershipType'}
              ,'values' :{'id': [['characterId']]
                         ,'level': [['baseCharacterLevel']]
                         ,'class_hash': [['classHash']]
                         ,'class_type': [['classType']]
                         ,'last_played': [['dateLastPlayed']]
                         ,'light_level': [['light']]
                         ,'minutes_played': [['minutesPlayedTotal']]
                         ,'race_hash': [['raceHash']]
                         ,'race_type': [['raceType']]}
              ,'statics' :{'membership_id' : 'membershipId'}
              ,'primary_keys' : ['id']}
    iterator = ['Response', 'characters', 'data']
    table = Character
    define_params(query_table, info_map, character_url, iterator, table)

def handle_aggregate_tables():
    """Fills pvpAggregate and pveAggregate with aggregate stats."""
    def aggregate_stats_url(membershipType, id):
        return f"{URL_START}/Destiny/Stats/Account/{membershipType}/{id}"
        # return f"{URL_START}/Destiny2/{membershipType}/Account/{id}/Stats/"
    def alt_insert(session, request_session, info_map, static_map, url, out_file, message, iterator, table):
        def fill_and_insert_dict(stats, table, statics):
            add_list = []
            insert_dict = {}
            if stats == None:
                return []
            for stat in stats:
                if 'pga' in stats[stat]:
                    insert_dict[stat+'pg'] = stats[stat]['pga']['value']
                insert_dict[stat] = stats[stat]['basic']['value']
            insert_dict = {**insert_dict, **static_map}
            insert_elem = table(**insert_dict)
            primary_key_map = {}
            for key in info_map['primary_keys']:
                primary_key_map[key] = insert_dict[key]
            #Upsert the element
            add_list.append(upsert(table, primary_key_map, insert_elem, session))
            add_list = [item for item in add_list if item is not None]
            return add_list
        #Actual request done here
        data = json_request(request_session, url, out_file, message)
        if data is None:
            print("No data retrieved.")
            return []
        #dynamic_dict_index gives us the specific iterator in the json we'll be using - could be games, characters, weapons, etc.
        tables = [PvPAggregate, PvEAggregate]
        total_list = []
        for table in tables:
            if table == PvPAggregate:
                mode = 'allPvP'
            elif table == PvEAggregate:
                mode = 'allPvE'
            stats = dynamic_dict_index(data, iterator+[mode, 'allTime'])
            total_list = total_list + fill_and_insert_dict(stats, table, static_map)
        return total_list
    
    query_table = Account
    info_map = {'attrs'  :{'id'             : 'id'
                         ,'name'           : 'display_name'
                         ,'membershipType' : 'membership_type'}
              ,'kwargs' :{'id' : 'id'}
              ,'url_params' :{'id'             : 'id'
                             ,'membershipType' : 'membershipType'}
              ,'values' :{'' : [[],[]]}
              ,'statics' :{'id' : 'id'}
              ,'primary_keys' : ['id']}
    iterator = ['Response', 'mergedAllCharacters', 'results']
    query_table = Account
    table = PvPAggregate
    define_params(query_table, info_map, aggregate_stats_url, iterator, table, alt_insert)


def handle_weapon_usage_table():
    def weapon_url(id, membershipType):
        #0 can be used instead of character ids
        return f"{OLD_URL_START}/Destiny/Stats/UniqueWeapons/{membershipType}/{id}/0"
    query_table = Account
    info_map = {'attrs' :{'id' : 'id'
                        ,'name' : 'display_name'
                        ,'membershipType' : 'membership_type'}
              ,'kwargs' :{'id' : 'id'}
              ,'url_params' :{'id' : 'id'
                             ,'membershipType' : 'membershipType'}
              ,'values' :{'weaponHash' : [['referenceId']]
                         ,'kills' : [['values', 'uniqueWeaponKills', 'basic', 'value']]
                         ,'precision_kills' : [['values', 'uniqueWeaponPrecisionKills', 'basic', 'value']]
                         ,'precision_kill_percentage' : [['values', 'uniqueWeaponKillsPrecisionKills', 'basic', 'value']]}
              ,'statics' :{'id' : 'id'}
              ,'primary_keys' : ['id', 'weaponHash']}
    iterator = ['Response', 'data', 'weapons']
    table = AccountWeaponUsage
    define_params(query_table, info_map, weapon_url, iterator, table)

def handle_activity_stats_table():
    def activity_url(id, membershipId, membershipType):
        return f"{OLD_URL_START}/Destiny/Stats/AggregateActivityStats/{membershipType}/{membershipId}/{id}/"
    query_table = Character
    info_map = {'attrs' :{'id' : 'id'
                        ,'membershipId' : 'membership_id'
                        ,'name' : 'display_name'
                        ,'membershipType' : 'membership_type'}
              ,'kwargs' :{'id' : 'id'}
              ,'url_params' :{'id' : 'id'
                             ,'membershipId' : 'membershipId'
                             ,'membershipType' : 'membershipType'}
              ,'values' :{'activityHash' : [['activityHash']]
                         ,'' : [['values'], ['basic', 'value']]}
              ,'statics' :{'id' : 'id'}
              ,'primary_keys' : ['id', 'activityHash']}
    iterator = ['Response', 'data', 'activities']
    table = CharacterActivityStats
    define_params(query_table, info_map, activity_url, iterator, table)

def handle_medal_table():
    def medal_url(id, membershipType):
        return f"{OLD_URL_START}/Destiny/Stats/Account/{membershipType}/{id}/?Groups=Medals"
    query_table = Account
    info_map = {'attrs' :{'id' : 'id'
                        ,'name' : 'display_name'
                        ,'membershipType' : 'membership_type'}
              ,'kwargs' :{'id' : 'id'}
              ,'url_params' :{'id' : 'id'
                             ,'membershipType' : 'membershipType'}
              ,'values' :{'' : [[], ['basic', 'value']]}
              ,'statics' :{'id' : 'id'}
              ,'primary_keys' : ['id']}
    iterator = ['Response', 'mergedAllCharacters', 'merged', 'allTime']
    table = AccountMedals
    define_params(query_table, info_map, medal_url, iterator, table)

def handle_account_activity_mode_stats_table():
    def activity_mode_url(id, membershipType, mode):
        return f"{OLD_URL_START}/Destiny/Stats/{membershipType}/{id}/0/?modes={mode}"
    query_table = Account
    mode_dict = {2:'story', 3:'strike', 4:'raid', 5:'allPvP', 6:'patrol', 7:'allPvE', 8:'pvpIntroduction', 9:'threeVsThree', 10:'control'
               ,11 : 'lockdown', 12:'team', 13:'freeForAll', 14:'trialsOfOsiris', 15:'doubles', 16:'nightfall', 17:'heroic', 18:'allStrikes', 19:'ironBanner', 20:'allArena'
               ,21 : 'arena', 22:'arenaChallenge', 23:'elimination', 24:'rift', 25:'allMayhem', 26:'mayhemClash', 27:'mayhemRumble', 28:'zoneControl', 29:'racing', 30:'arenaElderChallenge'
               ,31 : 'supremacy', 32:'privateMatchesAll', 33:'supremacyRumble', 34:'supremacyClash', 35:'supremacyInferno', 36:'supremacyMayhem'}
    table = AccountActivityModeStats
    for mode in range(2,37):
        info_map = {'attrs' :{'id' : 'id'
                            ,'name' : 'display_name'
                            ,'membershipType' : 'membership_type'}
                ,'kwargs' :{'id' : 'id'}
                ,'url_params' :{'id' : 'id'
                                ,'membershipType' : 'membershipType'}
                ,'values' :{'' : [[], ['basic', 'value']]}
                ,'statics' :{'id' : 'id'
                            ,'mode' : f'{modeDict[mode]}_actual'}
                ,'primary_keys' : ['id', 'mode']}
        partial_url = partial(activity_mode_url, mode=mode)
        iterator = ['Response', f'{mode_dict[mode]}', 'allTime']
        define_params(query_table, info_map, partial_url, iterator, table)

def handle_reference_tables():
    """Connects to the manifest.content database and builds the necessary reference tables."""
    session = Session()
    def build_reference_table(table_name, table, statement, dictionary, condition=None):
        print(f"Building {table_name} reference table...")
        add_list = []
        con = sqlite3.connect(os.environ['MANIFEST_CONTENT'])
        cur = con.cursor()
        with con:
            cur.execute(statement)
            group = cur.fetchall()
            for item in group:
                item_info = json.loads(item[1])
                item_dict = {}
                if not condition is None and condition(item_info):
                    continue
                for (key,value) in dictionary['info'].items():
                    item_dict[key] = item_info[value]
                new_item_def = table(**item_dict)
                inspection = inspect(new_item_def)
                object_dict = inspection.dict
                primary_key_map = {}
                for key in dictionary['primary_keys']:
                    primary_key_map[key] = object_dict[key]
                add_list.append(upsert(table, primary_key_map, new_item_def, session))
        session.add_all(add_list)
        session.commit()

    # Classes
    class_table = ClassReference
    class_info = {'info':{'id':'classHash', 'class_name':'className'}, 'primary_keys':{'id'}}
    class_statement = "SELECT * FROM DestinyClassDefinition"
    class_dict = build_reference_table("class", class_table, class_statement, class_info)

    # Weapons
    weapon_table = WeaponReference
    weapon_info = {'info':{'id':'itemHash', 'weapon_name':'itemName', 'weapon_type':'itemTypeName'}, 'weapon_rarity':'tierTypeName', 'primary_keys':{'id'}}
    weapon_statement = "SELECT * FROM DestinyInventoryItemDefinition"
    def weapon_condition(info):
        weapon_types = ['Rocket Launcher', 'Scout Rifle', 'Fusion Rifle', 'Sniper Rifle', 'Shotgun', 'Machine Gun', 'Pulse Rifle', 'Auto Rifle', 'Hand Cannon', 'Sidearm']
        return not ("itemTypeName" in info and info['itemTypeName'] in weapon_types)
    weapon_dict = build_reference_table("weapon", weapon_table, weapon_statement, weapon_info, weapon_condition)

    # Activities
    activity_table = ActivityReference
    activity_info = {'info':{'id':'activityHash', 'activity_name':'activityName', 'activity_type_hash':'activityTypeHash'}, 'primary_keys':{'id'}}
    activity_statement = "SELECT * FROM DestinyActivityDefinition"
    def activity_condition(info):
        return not ("activityName" in info)
    activity_dict = build_reference_table("activity", activity_table, activity_statement, activity_info, activity_condition)

    # Activity types
    activity_type_table = ActivityTypeReference
    activity_type_info = {'info':{'id':'activityTypeHash', 'activity_type_name':'activityTypeName'}, 'primary_keys':{'id'}}
    activity_type_statement = "SELECT * FROM DestinyActivityTypeDefinition"
    def activity_type_condition(info):
        return not ("activityTypeName" in info)
    activity_type_dict = build_reference_table("activity type", activity_type_table, activity_type_statement, activity_type_info, activity_type_condition)

    # Buckets
    bucket_table = BucketReference
    bucket_info = {'info':{'id':'bucketHash', 'bucket_name':'bucketName'}, 'primary_keys':{'id'}}
    bucket_statement = "SELECT * FROM DestinyInventoryBucketDefinition"
    def bucket_condition(info): 
        return not ("bucketName" in info)
    bucket_dict = build_reference_table("bucket", bucket_table, bucket_statement, bucket_info, bucket_condition)

def dynamic_dict_index(dct, value):
    try:
        ret = dct
        for item in value:
            ret = ret[item]
    except KeyError:
        ret = None
    return ret

def build_dict(dct, value_map):
    out_dict = {}
    for (key, val_list) in value_map.items():
        if len(val_list) == 1:
            if key.endswith('_2'):
                key = key[:-2]
            if (key in out_dict and out_dict[key] == None) or (key not in out_dict):
                out_dict[key] = dynamic_dict_index(dct, val_list[0])
        else:
            loop_dict = dynamic_dict_index(dct, val_list[0])
            if loop_dict == None:
                continue
            if key == '':
                for item in loop_dict:
                    out_dict[item] = dynamic_dict_index(loop_dict, [item]+val_list[1])
            else:
                out_dict[key] = dynamic_dict_index(loop_dict, val_list[1])
    return out_dict

def json_request(request_session, url, out_file, message=""):
    print(f"Connecting to Bungie: {url}")
    print(message)
    headers = make_header()
    res = request_session.get(url, headers=headers)
    #print(res.text)
    try:
        data = res.json()
    except json.decoder.JSONDecode_error:
        print(res.text)
        return None
    error_stat = data['ErrorStatus']
    if error_stat == "Success":
        if write_files:
            with open(f"JSON/{out_file}","w+") as f:
                json.dump(data, f)
        return data
    else:
        print("Error Status: " + error_stat)
        return None 

def upsert(table, primary_key_map, obj, session):
    first = session.query(table).filter_by(**primary_key_map).first()
    if first != None:
        session.query(table).filter_by(**primary_key_map).update({column: getattr(obj, column) for column in table.__table__.columns.keys()})
        return None
    return obj

def needs_update(kwargs, session):
    now = datetime.now()
    try:
        last_update = session.query(LastUpdated).filter_by(**kwargs).first().last_updated
        print("Fetching last update...")
        days_since = (now - last_update).days
        # print (f"Days since update: {days_since}")
        return days_since >= UPDATE_DIFF
    except (AttributeError, TypeError):
        return True

def remove_duplicates(add_list):
    zipped_list = [(item.id, item.__tablename__, item) for item in add_list]
    seen = set()
    final_list = []
    for id, tablename, item in zipped_list:
        if not ((id, tablename) in seen):
            seen.add((id, tablename))
            final_list.append(item)
    return final_list

def set_last_updated(update_id, table, session):
    update_dict = {'id' : update_id, 'table_name' : table.__tablename__, 'last_updated' : datetime.now()}
    update_elem = LastUpdated(**update_dict)
    update_primary_key = {'id' : update_dict['id'], 'table_name' : update_dict['table_name']}
    return upsert(LastUpdated, update_primary_key, update_elem, session)

def build_value_dict(target_map, attr_map):
    ret_dict = {}
    for (key, value) in target_map.items():
        if value.endswith('_actual'):
            ret_dict[key] = value[:-7]
        else:
            ret_dict[key] = attr_map[value]
    return ret_dict

if __name__ == "__main__":
    # load_config for testing purposes
    APP_PATH = "/etc/destinygotg"
    load_config()
    import time
    start_time = time.time()
    build_db()
    print("--- %s seconds ---" % (time.time() - start_time))
