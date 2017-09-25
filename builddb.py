#!/usr/bin/python
"""This script handles API calls from Bungie and fills the database with information parsed from
those files."""
import os
import json
import time
import sqlite3
from datetime import datetime

import requests
from sqlalchemy import func
from sqlalchemy.inspection import inspect

from destinygotg import SESSION
from initdb import LastUpdated, Bungie, Account, Character, CharacterTotalStats, \
        CharacterWeaponStats, CharacterExoticWeaponStats, CharacterMedalStats, \
        AccountTotalStats, AccountWeaponStats, ClassReference, WeaponReference#, \
        # AccountExoticWeaponStats, AccountMedalStats

URL_START = "https://bungie.net/Platform"
OLD_URL_START = "https://bungie.net/d1/Platform"
UPDATE_DIFF = 1 # Number of days between updates
REQUEST_SESSION = requests.session()
SESSION = SESSION()

def make_header():
    """Takes the APIKEY from the config file and makes a header."""
    return {'X-API-KEY':os.environ['BUNGIE_APIKEY']}

def timeit(funct, args=None):
    """Given a function, returns the runtime."""
    start_time = time.clock()
    if args is None:
        funct()
    else:
        funct(args)
    print("--- %s seconds ---" % (time.clock() - start_time))

def build_db(opts):
    """Main function to build the full database"""
    start_time = time.clock()
    if opts["update"] or opts["clean"]:
        handle_bungie_table()
        handle_account_table()
        handle_character_table()
        handle_account_updates()
        handle_character_total_table()
        handle_weapon_stats_table()
        handle_exotic_weapon_table()
        handle_medal_table()
        handle_filling_account_tables()
        handle_reference_tables()
    elif opts["bungie"]:
        handle_bungie_table()
    elif opts["account"]:
        handle_account_table()
    elif opts["character"]:
        handle_character_table()
    elif opts["account2"]:
        handle_account_updates()
    elif opts["stats"]:
        handle_character_total_table()
    elif opts["weapons"]:
        handle_weapon_stats_table()
    elif opts["exotics"]:
        handle_exotic_weapon_table()
    elif opts["medals"]:
        handle_medal_table()
    elif opts["accountstats"]:
        handle_filling_account_tables()
    elif opts["refs"]:
        handle_reference_tables()
    print("--- %s seconds ---" % (time.clock() - start_time))

#info_map = {'attrs':{'attr1':'attr1Name', ...}
#           ,'kwargs':{'kwargs1':'attr1', ...}
#           ,'url_params':{'param1':'attr1', ...}
#           ,'values':{'value1':'location1', ...}
#           ,'statics':{'static1':'attr1', ...}
#           ,'primary_keys':{'key_name1':'attr1', ...}}

def request_and_insert(info_map, static_map, request_info):
    """Does everything else"""
    table = info_map['table']
    #Figure out if we need to update. We have kwargs and the table name, so just check LastUpdated
    # for it.
    add_list = []
    #Actual request done here
    data = json_request(request_info)
    if data is None:
        print("No data retrieved.")
        return []
    # dynamic_dict_index gives us the specific iterator in the json we'll be using - could be games,
    # characters, weapons, etc.
    group = dynamic_dict_index(data, info_map['iterator'])
    if group is None:
        print("Nothing to insert.")
        return []
    # Sometimes we get arrays, other times we get dictionaries. Wrap the dicts in a list to avoid
    # headache later.
    if isinstance(group, dict):
        group = group.items()
    for elem in group:
        if elem is None:
            continue
        # build_dict uses a nifty dynamic dictionary indexing function that allows us to grab
        # info from multiply-nested fields in the dict
        if isinstance(elem, tuple):
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
        #Statics are pre-defined values - maybe the id from user.id in insert_from_table
        if 'statics' in info_map:
            insert_dict = {**insert_dict, **static_map}
        #Create a new element for insertion using kwargs
        insert_elem = table(**insert_dict)
        primary_key_map = {}
        for key in info_map['primary_keys']:
            primary_key_map[key] = getattr(insert_elem, key)
        #Upsert the element
        add_list.append(upsert(table, primary_key_map, insert_elem))
    #Get rid of the None elements - they've been updated already
    add_list = [item for item in add_list if item is not None]
    return add_list

class RequestInfo(object):
    """Contains all of the necessary info to build a table."""

    url = ""
    out_file = ""
    message = ""

    def __init__(self, url_function, url_map, attr_map, table):
        self.url_function = url_function
        self.url_map = url_map
        self.attr_map = attr_map
        self.table = table

    def get_url(self):
        """Builds the actual url string."""
        if self.url != "":
            return self.url
        return self.url_function(**self.url_map)

    def get_file(self):
        """Builds the out file name."""
        if self.out_file != "":
            return self.out_file
        return f"{self.attr_map['name']}_{self.table.__tablename__}.json"

    def get_msg(self):
        """Builds the print message."""
        if self.message != "":
            return self.message
        return f"Fetching {self.table.__tablename__} data for: {self.attr_map['name']}"

def insert_from_table(query_table, info_map):
    """Does like everything"""
    table = info_map['table']
    url_function = info_map['url']
    #Build a single request session for the duration of the table creation
    total_add_list = []
    #Elems is what we'll be iterating through - could be users, characters, etc.
    for elem in SESSION.query(query_table).all():
        # Attrs are the attributes associated with the elem. User.id or user.membership_type,
        # for example. AKA fields in the database.
        attr_map, url_map, static_map, kwargs_map = retrieve_attributes(elem, info_map)
        request_info = RequestInfo(url_function, url_map, attr_map, table)
        to_update = needs_update(kwargs_map)
        to_update = True
        if not to_update:
            print(f"Not updating {table.__tablename__} table for user: {attr_map['name']}")
            add_list = []
        add_list = request_and_insert(info_map, static_map, request_info)
        total_add_list = total_add_list + add_list
        #Upsert into LastUpdated
        update_id = attr_map[info_map['kwargs']['id']]
        update_item = set_last_updated(update_id, table)
        total_add_list = total_add_list + [update_item]
    total_add_list = [item for item in total_add_list if item is not None]
    # final_list = remove_duplicates(total_add_list)
    final_list = total_add_list
    SESSION.add_all(final_list)
    SESSION.commit()

def retrieve_attributes(elem, info_map):
    """Given a row and an info_map, extracts useful information."""
    attrs = info_map['attrs']
    url_params = info_map['url_params']
    statics = info_map['statics']
    kwargs = info_map['kwargs']
    table = info_map['table']

    attr_map = {}
    for (key, value) in attrs.items():
        try:
            attr_map[key] = getattr(elem, value)
        except AttributeError:
            attr_map[key] = getattr(SESSION.query(Account).filter_by(
                id=attr_map['membership_id']).first(), value)
    # url_params are used to build the request URL.
    url_map = build_value_dict(url_params, attr_map)
    # Statics actually need to get passed to the insert function so they can be put in the table.
    static_map = build_value_dict(statics, attr_map)
    # Kwargs are used to check if the database needs updating for the current elem.
    kwargs_map = build_value_dict(kwargs, attr_map)
    kwargs_map['table_name'] = table.__tablename__
    return attr_map, url_map, static_map, kwargs_map

def handle_bungie_table():
    """Fills Bungie table with all users in the clan"""
    # Destiny 2 changes results per page to be 100. Because there is a max of 100 people in
    # the clan, we don't need the extra stuff here anymore.
    info_map = {'values': {'id': [['bungieNetUserInfo', 'membershipId']],
                           'id_2':[['destinyUserInfo', 'membershipId']],
                           'bungie_name':[['bungieNetUserInfo', 'displayName']],
                           'bungie_name_2':[['destinyUserInfo', 'displayName']],
                           'membership_type':[['bungieNetUserInfo', 'membershipType']],
                           'membership_type_2':[['destinyUserInfo', 'membershipType']]},
                'kwargs': {'id': 'id'},
                'primary_keys': ['id'],
                'iterator': ['Response', 'results'],
                'table': Bungie}
    request_info = RequestInfo(None, None, None, None)
    request_info.url = f"{URL_START}/GroupV2/{os.environ['BUNGIE_CLANID']}/Members/?currentPage=1"
    request_info.out_file = "clanUsers.json"
    request_info.message = "Fetching list of clan users."
    add_list = request_and_insert(info_map, {}, request_info)
    final_list = remove_duplicates(add_list)
    SESSION.add_all(final_list)
    SESSION.commit()

def handle_account_table():
    """Retrieve JSONs for users, listing their Destiny accounts. Fills account table."""
    def account_url(id, membership_type):
        """Builds the account URL."""
        return f"{URL_START}/User/GetMembershipsById/{id}/{membership_type}"
    query_table = Bungie
    info_map = {'attrs': {'id': 'id', 'name': 'bungie_name', 'membership_type': 'membership_type'},
                'kwargs': {'id': 'id'},
                'url_params': {'id': 'id', 'membership_type': 'membership_type'},
                'values': {'id': [['membershipId']], 'membership_type' : [['membershipType']],
                           'display_name': [['displayName']]},
                'statics': {'bungie_id': 'id'},
                'primary_keys' : ['id'],
                'url': account_url,
                'iterator': ['Response', 'destinyMemberships'],
                'table': Account}
    insert_from_table(query_table, info_map)

def handle_character_table():
    """Fills the Character table."""
    def character_url(membership_id, membership_type):
        """Builds the character URL."""
        return f"{URL_START}/Destiny2/{membership_type}/Profile/{membership_id}/?components=200"
    query_table = Account
    info_map = {'attrs': {'membership_id': 'id', 'name': 'display_name',
                          'membership_type' : 'membership_type'},
                'kwargs': {'id': 'membership_id'},
                'url_params': {'membership_id': 'membership_id',
                               'membership_type': 'membership_type'},
                'values': {'id': [['characterId']], 'level': [['baseCharacterLevel']],
                           'class_hash': [['classHash']], 'class_type': [['classType']],
                           'last_played': [['dateLastPlayed']], 'light_level': [['light']],
                           'minutes_played': [['minutesPlayedTotal']], 'race_hash': [['raceHash']],
                           'race_type': [['raceType']]},
                'statics': {'membership_id': 'membership_id'},
                'primary_keys': ['id'],
                'url': character_url,
                'iterator': ['Response', 'characters', 'data'],
                'table': Character}
    insert_from_table(query_table, info_map)

def handle_character_total_table():
    """Fills the CharacterTotalStats table."""
    def activity_url(membership_type, membership_id, id):
        """Builds activity URL."""
        return f"""{URL_START}/Destiny2/{membership_type}/Account/{membership_id}/Character/{id}/Stats/"""
    query_table = Character
    info_map = {'attrs': {'id': 'id', 'membership_id': 'membership_id', 'name': 'display_name',
                          'membership_type': 'membership_type'},
                'kwargs': {'id': 'id'},
                'url_params': {'id': 'id', 'membership_type': 'membership_type',
                               'membership_id':'membership_id'},
                'values': {'': [['allTime'], ['basic', 'value']]},
                'statics': {'id': 'id'},
                'primary_keys': ['id', 'mode'],
                'url': activity_url,
                'iterator': ['Response'],
                'table': CharacterTotalStats}
    insert_from_table(query_table, info_map)

def handle_weapon_stats_table():
    """Fills the CharacterWeaponStats table."""
    def weapon_url(membership_type, membership_id, id):
        """Builds weapon URL."""
        return f"{URL_START}/Destiny2/{membership_type}/Account/{membership_id}/Character/{id}/Stats/?groups=2"
    query_table = Character
    info_map = {'attrs': {'id': 'id', 'membership_id': 'membership_id', 'name': 'display_name',
                          'membership_type': 'membership_type'},
                'kwargs': {'id': 'id'},
                'url_params': {'id': 'id', 'membership_type':'membership_type',
                               'membership_id':'membership_id'},
                'values': {'': [['allTime'], ['basic', 'value']]},
                'statics': {'id': 'id'},
                'primary_keys': ['id', 'mode'],
                'url': weapon_url,
                'iterator': ['Response'],
                'table': CharacterWeaponStats}
    insert_from_table(query_table, info_map)

def handle_exotic_weapon_table():
    """Fills the CharacterExoticWeaponStats table."""
    def exotic_url(membership_type, membership_id, id):
        """Builds exotic weapon URL."""
        return f"{URL_START}/Destiny2/{membership_type}/Account/{membership_id}/Character/{id}/Stats/UniqueWeapons/"
    query_table = Character
    info_map = {'attrs': {'id': 'id', 'membership_id': 'membership_id', 'name': 'display_name',
                          'membership_type':'membership_type'},
                'kwargs': {'id': 'id'},
                'url_params': {'id': 'id', 'membership_type':'membership_type',
                               'membership_id': 'membership_id'},
                'values': {'': [['allTime'], ['basic', 'value']]},
                'statics': {'id': 'id'},
                'primary_keys': ['id', 'mode'],
                'url': exotic_url,
                'iterator': ['Response'],
                'table': CharacterExoticWeaponStats}
    # insert_from_table(query_table, info_map)

def handle_medal_table():
    """Fills the CharacterMedalStats table."""
    def medal_url(id, membership_type):
        """Builds the medals URL."""
        return f"{OLD_URL_START}/Destiny/Stats/Account/{membership_type}/{id}/?Groups=Medals"
    query_table = Account
    info_map = {'attrs': {'id': 'id', 'name': 'display_name', 'membership_type': 'membership_type'},
                'kwargs': {'id': 'id'},
                'url_params': {'id': 'id', 'membership_type': 'membership_type'},
                'values': {'': [[], ['basic', 'value']]},
                'statics': {'id': 'id'},
                'primary_keys': ['id'],
                'url': medal_url,
                'iterator': ['Response', 'mergedAllCharacters', 'merged', 'allTime'],
                'table': CharacterMedalStats}
    # insert_from_table(query_table, info_map)

def handle_account_updates():
    """Fills account with remaining columns needing aggregation from character table."""
    # Need to add records for max_light_level and minutes_played
    # First, grab all account records
    table = Account
    elems = SESSION.query(table).all()
    for elem in elems:
        max_light = SESSION.query(func.max(Character.light_level)).join(Account).filter(
            Character.membership_id == elem.id).first()[0]
        minutes_played = SESSION.query(func.sum(Character.minutes_played)).join(Account).filter(
            Character.membership_id == elem.id).first()[0]
        most_recently_played = SESSION.query(func.max(Character.last_played)).join(Account).filter(
            Character.membership_id == elem.id).first()[0]
        SESSION.query(Account).filter(Account.id == elem.id).update(
            {'max_light': max_light, 'total_minutes_played': minutes_played,
             'most_recently_played': most_recently_played})
    SESSION.commit()

def handle_filling_account_tables():
    """Fills account tables from the character tables. Rebuilds Float columns cleverly."""
    # At a high level:
    # 1. Anything that is an integer needs to summed, and
    # 2. Anything that is a float needs to be averaged.
    # In fact, let's just ignore anything that is a float, and recalculate those at out convenience.
    # Every stat group has an activitiesEntered column we can use for per game stats.
    table_list = [(CharacterTotalStats, AccountTotalStats),
                  (CharacterWeaponStats, AccountWeaponStats)]
                  # (CharacterExoticWeaponStats, AccountExoticWeaponStats),
                 #, (CharacterMedalStats, AccountMedalStats)]
    mode_list = ["allPvP", "allStrikes", "story", "patrol"]
    add_list = []
    for src_table, dst_table in table_list:
        elems = SESSION.query(Account).all()
        for elem in elems:
            print(f"Updating {dst_table.__tablename__} table for {elem.display_name}.")
            for mode in mode_list:
                update_dict = {}
                all_columns = src_table.__table__.columns
                columns = [(column.key, str(column.type)) for column in all_columns]
                # Handle the averages later
                basics = [column[0] for column in columns if not column[1] == "FLOAT"
                          and column[0] != "id" and column[0] != "mode"]
                pgas = [column[0] for column in columns if column[1] == "FLOAT"]
                for column in basics:
                    col = [column]
                    attr = (getattr(src_table, column) for column in col)
                    value = SESSION.query(func.sum(*attr)).join(Character).filter(
                        Character.membership_id == elem.id, src_table.mode == mode).first()[0]
                    update_dict[column] = value
                for column in pgas:
                    try:
                        if src_table == CharacterTotalStats:
                            deaths = update_dict["deaths"]
                            if deaths == 0:
                                deaths = 1
                            kills = update_dict["kills"]
                        activities = update_dict["activitiesEntered"]
                        if activities == 0:
                            activities = 1
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
                        elif column == "winLossRatio":
                            value = (update_dict["activitiesWon"]*1.0)/activities
                        elif column.startswith("weaponKillsPrecisionKills"):
                            weapon = f"{column[25:]}"
                            weapon_kills = update_dict[f"weaponKills{weapon}"]
                            if weapon_kills == 0:
                                weapon_kills = 1
                            weapon_precision_kills = update_dict[f"weaponPrecisionKills{weapon}"]
                            value = (weapon_precision_kills*1.0)/weapon_kills
                        elif column.endswith("pg"):
                            value = (update_dict[column[:-2]]*1.0)/update_dict["activitiesEntered"]
                    except TypeError:
                        value = None
                    update_dict[column] = value
                update_dict["id"] = elem.id
                update_dict["mode"] = mode
                insert_elem = dst_table(**update_dict)
                primary_key_map = {}
                primary_key_list = [key.name for key in inspect(src_table).primary_key]
                for key in primary_key_list:
                    primary_key_map[key] = getattr(insert_elem, key)
                #Upsert the element
                add_list.append(upsert(dst_table, primary_key_map, insert_elem))
    add_list = [item for item in add_list if item is not None]
    SESSION.add_all(add_list)
    SESSION.commit()

def handle_reference_tables():
    """Connects to the manifest.content database and builds the necessary reference tables."""
    def build_reference_table(table_name, table, statement, info_map, condition=None):
        """Equivalent of the insert_from_table function for the ref tables"""
        print(f"Building {table_name} reference table...")
        add_list = []
        con = sqlite3.connect(f"{os.environ['APP_PATH']}/{os.environ['MANIFEST_NAME']}")
        cur = con.cursor()
        with con:
            cur.execute(statement)
            group = cur.fetchall()
            for item in group:
                item_info = json.loads(item[1])
                if not condition is None and condition(item_info):
                    continue
                item_dict = build_dict(item_info, info_map['values'])
                new_item_def = table(**item_dict)
                primary_key_map = {}
                for key in info_map['primary_keys']:
                    primary_key_map[key] = getattr(new_item_def, key)
                add_list.append(upsert(table, primary_key_map, new_item_def))
        add_list = [item for item in add_list if item is not None]
        SESSION.add_all(add_list)
        SESSION.commit()

    # Classes
    class_info = {'values': {'id': [['hash']],
                             'class_name':[['displayProperties', 'name']]},
                  'primary_keys':['id']}
    class_statement = "SELECT * FROM DestinyClassDefinition"
    build_reference_table("class", ClassReference, class_statement, class_info)

    # Weapons
    weapon_info = {'values': {'id': [['hash']],
                              'weapon_name': [['displayProperties', 'name']],
                              'weapon_type': [['itemTypeDisplayName']],
                              'weapon_rarity': [['inventory', 'tierTypeName']]},
                   'primary_keys': ['id']}
    weapon_statement = "SELECT * FROM DestinyInventoryItemDefinition"
    def weapon_condition(info):
        """Checks if the item is a weapon or not"""
        weapon_types = ['Rocket Launcher', 'Scout Rifle', 'Fusion Rifle', 'Sniper Rifle',
                        'Shotgun', 'Machine Gun', 'Pulse Rifle', 'Auto Rifle', 'Hand Cannon',
                        'Sidearm', 'Submachinegun']
        return not ("itemTypeDisplayName" in info and info['itemTypeDisplayName'] in weapon_types)
    build_reference_table(
        "weapon", WeaponReference, weapon_statement, weapon_info, weapon_condition)

def dynamic_dict_index(dct, value):
    """Allows for dynamic indexing of a dictionary given a value list."""
    try:
        ret = dct
        for item in value:
            ret = ret[item]
    except KeyError:
        ret = None
    return ret

def build_dict(dct, value_map):
    """Given a working dict and a map of values, build a dict of the requested information."""
    out_dict = {}
    for (key, val_list) in value_map.items():
        if len(val_list) == 1:
            if key.endswith('_2'):
                key = key[:-2]
            if (key in out_dict and out_dict[key] is None) or (key not in out_dict):
                out_dict[key] = dynamic_dict_index(dct, val_list[0])
        else:
            loop_dict = dynamic_dict_index(dct, val_list[0])
            if loop_dict is None:
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

def json_request(request_info):
    """Performs a JSON request and potentially writes to a file."""
    url = request_info.get_url()
    out_file = request_info.get_file()
    message = request_info.get_msg()
    print(f"Connecting to Bungie: {url}")
    print(message)
    headers = make_header()
    res = REQUEST_SESSION.get(url, headers=headers)
    #print(res.text)
    try:
        data = res.json()
    except json.decoder.JSONDecodeError:
        print(res.text)
        return None
    error_stat = data['ErrorStatus']
    if error_stat == "Success":
        if os.environ["WRITE_FILES"]:
            with open(f"JSON/{out_file}", "w+") as write_file:
                json.dump(data, write_file)
        return data
    else:
        print("Error Status: " + error_stat)
        return None

def upsert(table, primary_key_map, obj):
    """Decides whether to insert or update an object."""
    first = SESSION.query(table).filter_by(**primary_key_map).first()
    if first != None:
        keys = table.__table__.columns.keys()
        SESSION.query(table).filter_by(**primary_key_map).update(
            {column: getattr(obj, column) for column in keys})
        return None
    return obj

def needs_update(kwargs):
    """Given a primary key list, returns True if a record hasn't been updated in the last
    UPDATE_DIFF period."""
    now = datetime.now()
    try:
        last_update = SESSION.query(LastUpdated).filter_by(**kwargs).first().last_updated
        print("Fetching last update...")
        days_since = (now - last_update).days
        # print (f"Days since update: {days_since}")
        return days_since >= UPDATE_DIFF
    except (AttributeError, TypeError):
        return True

def remove_duplicates(add_list):
    """Removes duplicates based on primary keys and table names."""
    zipped_list = [(item.id, item.__tablename__, item) for item in add_list]
    seen = set()
    final_list = []
    for uid, tablename, item in zipped_list:
        if not (uid, tablename) in seen:
            seen.add((uid, tablename))
            final_list.append(item)
    return final_list

def set_last_updated(update_id, table):
    """Updates the LastUpdated table with the time a primary key/table pair was updated."""
    update_dict = {'id': update_id, 'table_name': table.__tablename__,
                   'last_updated': datetime.now()}
    update_elem = LastUpdated(**update_dict)
    update_primary_key = {'id' : update_dict['id'], 'table_name' : update_dict['table_name']}
    return upsert(LastUpdated, update_primary_key, update_elem)

def build_value_dict(target_map, attr_map):
    """Takes a target and the attribute map, and returns a dict with the require attrs."""
    ret_dict = {}
    for (key, value) in target_map.items():
        if value.endswith('_actual'):
            ret_dict[key] = value[:-7]
        else:
            ret_dict[key] = attr_map[value]
    return ret_dict
