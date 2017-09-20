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
from initdb import Base, Bungie, Account, Character, CharacterTotalStats, CharacterWeaponStats, CharacterExoticWeaponStats, CharacterMedalStats, AccountTotalStats, AccountWeaponStats, AccountExoticWeaponStats, AccountMedalStats, LastUpdated
from destinygotg import Session, load_config
from functools import partial
from sqlalchemy import func
from sqlalchemy.inspection import inspect

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
    handle_bungie_table()
    handle_account_table()
    handle_character_table()
    handle_account_updates()
    handle_character_total_table()
    handle_weapon_stats_table()
    # handle_exotic_weapon_table()
    # handle_medal_table()
    handle_filling_account_tables()
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
    if type(group) == dict:
        group = group.items()

    for elem in group:
        if elem == None:
            continue
        #build_dict uses a nifty dynamic dictionary indexing function that allows us to grab info from multiply-nested fields in the dict
        if type(elem) == tuple:
            # We're in a dict, so we need to add info to the insert dict from the key and the value
            tuple_key_info = {}
            if table == CharacterTotalStats or table == CharacterWeaponStats:
                tuple_key_info = {'mode':elem[0]}
                # This is as normal
                tuple_value_info = build_dict(elem[1], info_map['values'])
                # Combine the dicts
                insert_dict = {**tuple_key_info, **tuple_value_info}
            else:
                insert_dict = build_dict(elem[1], info_map['values'])
        else:
            insert_dict = build_dict(elem, info_map['values'])
        #Handle Bungie's weird time format
        for key in insert_dict.keys():
            if key == "last_played" or key == "period":
                insert_dict[key] = datetime.strptime(insert_dict[key], "%Y-%m-%dT%H:%M:%SZ")
        # print(insert_dict)
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
            try: 
                attr_map[key] = getattr(elem, value)
            except AttributeError:
                attr_map[key] = getattr(session.query(Account).filter_by(id=attr_map['membership_id']).first(), value)
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
        add_list = request_and_insert(session, request_session, info_map, static_map, url, out_file, message, iterator, table)
        total_add_list = total_add_list + add_list
        #Upsert into LastUpdated
        update_id = attr_map[info_map['kwargs']['id']]
        update_item = set_last_updated(update_id, table, session)
        total_add_list = total_add_list + [update_item]
    total_add_list = [item for item in total_add_list if item is not None]
    # final_list = remove_duplicates(total_add_list)
    final_list = total_add_list
    session.add_all(final_list)
    session.commit()

def handle_bungie_table():
    """Fills Bungie table with all users in the clan"""
    # Destiny 2 changes results per page to be 100. Because there is a max of 100 people in the clan, we don't need the extra stuff here anymore.
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
    def account_url(id, membership_type):
        return f"{URL_START}/User/GetMembershipsById/{id}/{membership_type}"
    query_table = Bungie
    info_map = {'attrs'  :{'id'             : 'id'
                         ,'name'           : 'bungie_name'
                         ,'membership_type' : 'membership_type'}
              ,'kwargs' :{'id' : 'id'}
              ,'url_params' :{'id'             : 'id'
                             ,'membership_type' : 'membership_type'}
              ,'values' :{'id'              : [['membershipId']]
                         ,'membership_type' : [['membershipType']]
                         ,'display_name'    : [['displayName']]}
              ,'statics' :{'bungie_id' : 'id'}
              ,'primary_keys' : ['id']}
    iterator = ['Response', 'destinyMemberships']
    table = Account
    define_params(query_table, info_map, account_url, iterator, table)

def handle_character_table():
    def character_url(membership_id, membership_type):
        return f"{URL_START}/Destiny2/{membership_type}/Profile/{membership_id}/?components=200"
    query_table = Account
    info_map = {'attrs' :{'membership_id' : 'id'
                        ,'name' : 'display_name'
                        ,'membership_type' : 'membership_type'}
              ,'kwargs' :{'id' : 'membership_id'}
              ,'url_params' :{'membership_id' : 'membership_id'
                             ,'membership_type' : 'membership_type'}
              ,'values' :{'id': [['characterId']]
                         ,'level': [['baseCharacterLevel']]
                         ,'class_hash': [['classHash']]
                         ,'class_type': [['classType']]
                         ,'last_played': [['dateLastPlayed']]
                         ,'light_level': [['light']]
                         ,'minutes_played': [['minutesPlayedTotal']]
                         ,'race_hash': [['raceHash']]
                         ,'race_type': [['raceType']]}
              ,'statics' :{'membership_id' : 'membership_id'}
              ,'primary_keys' : ['id']}
    iterator = ['Response', 'characters', 'data']
    table = Character
    define_params(query_table, info_map, character_url, iterator, table)

def handle_character_total_table():
    def activity_url(membership_type, membership_id, id):
        return f"{URL_START}/Destiny2/{membership_type}/Account/{membership_id}/Character/{id}/Stats/"
    query_table = Character
    info_map = {'attrs':{'id':'id'
                        ,'membership_id':'membership_id'
                        ,'name':'display_name'
                        ,'membership_type':'membership_type'}
            ,'kwargs':{'id':'id'}
            ,'url_params':{'id':'id'
                            ,'membership_type':'membership_type'
                            ,'membership_id':'membership_id'}
            ,'values':{'':[['allTime'], ['basic', 'value']]}
            ,'statics':{'id':'id'}
            ,'primary_keys':['id', 'mode']}
    iterator = ['Response']
    table = CharacterTotalStats
    define_params(query_table, info_map, activity_url, iterator, table)

def handle_weapon_stats_table():
    def weapon_url(membership_type, membership_id, id):
        return f"{URL_START}/Destiny2/{membership_type}/Account/{membership_id}/Character/{id}/Stats/?groups=2"
    query_table = Character
    info_map = {'attrs':{'id':'id'
                        ,'membership_id':'membership_id'
                        ,'name':'display_name'
                        ,'membership_type':'membership_type'}
            ,'kwargs':{'id':'id'}
            ,'url_params':{'id':'id'
                            ,'membership_type':'membership_type'
                            ,'membership_id':'membership_id'}
            ,'values':{'':[['allTime'], ['basic', 'value']]}
            ,'statics':{'id':'id'}
            ,'primary_keys':['id', 'mode']}
    iterator = ['Response']
    table = CharacterWeaponStats
    define_params(query_table, info_map, weapon_url, iterator, table)

def handle_exotic_weapon_table():
    def weapon_url(membership_type, membership_id, id):
        return f"{URL_START}/Destiny2/{membership_type}/Account/{membership_id}/Character/{id}/Stats/?groups=103"
    query_table = Character
    info_map = {'attrs':{'id':'id'
                        ,'membership_id':'membership_id'
                        ,'name':'display_name'
                        ,'membership_type':'membership_type'}
            ,'kwargs':{'id':'id'}
            ,'url_params':{'id':'id'
                            ,'membership_type':'membership_type'
                            ,'membership_id':'membership_id'}
            ,'values':{'':[['allTime'], ['basic', 'value']]}
            ,'statics':{'id':'id'}
            ,'primary_keys':['id', 'mode']}
    iterator = ['Response']
    table = CharacterExoticStats
    define_params(query_table, info_map, weapon_url, iterator, table)

def handle_medal_table():
    def medal_url(id, membership_type):
        return f"{OLD_URL_START}/Destiny/Stats/Account/{membership_type}/{id}/?Groups=Medals"
    query_table = Account
    info_map = {'attrs' :{'id' : 'id'
                        ,'name' : 'display_name'
                        ,'membership_type' : 'membership_type'}
              ,'kwargs' :{'id' : 'id'}
              ,'url_params' :{'id' : 'id'
                             ,'membership_type' : 'membership_type'}
              ,'values' :{'' : [[], ['basic', 'value']]}
              ,'statics' :{'id' : 'id'}
              ,'primary_keys' : ['id']}
    iterator = ['Response', 'mergedAllCharacters', 'merged', 'allTime']
    table = AccountMedals
    define_params(query_table, info_map, medal_url, iterator, table)

def handle_account_updates():
    # Need to add records for max_light_level and minutes_played
    # First, grab all account records
    session = Session()
    table = Account
    elems = session.query(table).all()
    add_list = []
    for elem in elems:
        max_light = session.query(func.max(Character.light_level)).join(Account).filter(Character.membership_id == elem.id).first()[0]
        minutes_played = session.query(func.sum(Character.minutes_played)).join(Account).filter(Character.membership_id == elem.id).first()[0]
        most_recently_played = session.query(func.max(Character.last_played)).join(Account).filter(Character.membership_id == elem.id).first()[0]
        session.query(Account).filter(Account.id == elem.id).update({'max_light': max_light, 
            'total_minutes_played': minutes_played, 'most_recently_played': most_recently_played})
    session.commit()

def handle_filling_account_tables():
    # At a high level:
    # 1. Anything that is an integer needs to summed, and
    # 2. Anything that is a float needs to be averaged.
    # In fact, let's just ignore anything that is a float, and recalculate those at out convenience.
    # Every stat group has an activitiesEntered column we can use for per game stats.
    session = Session()
    table_list = [(CharacterTotalStats, AccountTotalStats), (CharacterWeaponStats, AccountWeaponStats)]
                 #, (CharacterMedalStats, AccountMedalStats)]
    mode_list = ["allPvP", "allStrikes", "story", "patrol"]
    add_list = []
    for source_table, dest_table in table_list:
        elems = session.query(Account).all()
        for elem in elems:
            print(f"Updating {dest_table.__tablename__} table for {elem.display_name}.")
            for mode in mode_list:
                update_dict = {}
                all_columns = source_table.__table__.columns
                columns = [(column.key, str(column.type)) for column in all_columns]
                # Handle the averages later
                basics = [column[0] for column in columns if not column[1] == "FLOAT" and column[0] is not "id" and column[0] is not "mode"]
                pgas = [column[0] for column in columns if column[1] == "FLOAT"]
                for column in basics:
                    col = [column]
                    value = session.query(func.sum(*(getattr(source_table, column) for column in col))).join(Character).filter(Character.membership_id == elem.id, source_table.mode == mode).first()[0]
                    update_dict[column] = value
                for column in pgas:
                    try:
                        deaths = update_dict["deaths"]
                        if deaths == 0:
                            deaths = 1
                        kills = update_dict["kills"]
                        activities = update_dict["activitiesEntered"]
                        if column == "killsDeathsRatio":
                            value = (kills*1.0)/deaths
                        elif column == "killsDeathsAssists":
                            value = (kills*1.0 + update_dict["assists"])/deaths
                        elif column == "averageDeathDistance":
                            value = (update_dict["totalDeathDistance"]*1.0)/deaths
                        elif column == "averageKillDistance":
                            value = (update_dict["totalKillDistance"]*1.0)/kills
                        elif column == "averageLifespan":
                            value = (update_dict["secondsPlayed"]*1.0)/deaths
                        elif column == "averageScorePerKill":
                            value = (update_dict["score"]*1.0)/kills
                        elif column == "averageScorePerLife":
                            value = (update_dict["score"]*1.0)/deaths
                        elif column.startswith("weaponKillsPrecisionKills"):
                            value = (update_dict[f"weaponPrecisionKills{column[25:]}"]*1.0)/update_dict[f"weaponKills{column[25:]}"]
                        elif column.endswith("pg"):
                            value = (update_dict[column[:-2]]*1.0)/update_dict["activitiesEntered"]
                    except (KeyError, TypeError):
                        value = None
                    update_dict[column] = value
                update_dict["id"] = elem.id
                update_dict["mode"] = mode
                insert_elem = dest_table(**update_dict)
                primary_key_map = {}
                primary_key_list = [key.name for key in inspect(source_table).primary_key]
                for key in primary_key_list:
                    primary_key_map[key] = getattr(insert_elem, key)
                #Upsert the element
                add_list.append(upsert(dest_table, primary_key_map, insert_elem, session))
    add_list = [item for item in add_list if item is not None]
    session.add_all(add_list)
    session.commit()

# def handle_filling_account_table_averages():
#     session = Session()
#     table_list = [AccountTotalStats, AccountWeaponStats]
#     for table in table_list:


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
                for item in loop_dict:
                    if 'pga' in item:
                        out_dict[item+'pg'] = dynamic_dict_index(loop_dict, [item]+['pga', 'value'])
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
    except json.decoder.JSONDecodeError:
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
