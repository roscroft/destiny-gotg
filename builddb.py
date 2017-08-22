#!/usr/bin/python
#This file (with update option set) is run daily; it pulls new clan members and new accounts. For existing members, it adds newly created characters, and updates all existing stats.
#Perhaps most importantly, it pulls in new activities completed by all members.
import os, sys
import json, requests
import sqlite3
from datetime import datetime
from sqlalchemy import exists, and_
from sqlalchemy.sql.expression import literal_column
from sqlalchemy.inspection import inspect
from initdb import Base, Bungie, Account, PvPAggregate, PvEAggregate, Character, AccountWeaponUsage, CharacterActivityStats, AccountMedals, ActivityReference, ClassReference, WeaponReference, ActivityTypeReference, BucketReference, AccountActivityModeStats, LastUpdated
from destinygotg import Session, loadConfig
sys.path.append("./")
import importlib, time, itertools
from functools import partial
#endpoints = importlib.import_module("Destiny-API-Frameworks.python.endpoints")

GROUP_URL_START = "https://bungie.net/Platform"
URL_START = "https://bungie.net/d1/Platform"
UPDATE_DIFF = 1 # Number of days between updates

def makeHeader():
    return {'X-API-KEY':os.environ['BUNGIE_APIKEY']}

def timeit(func, args=None):
    start_time = time.clock()
    if args == None:
        func()
    else:
        func(args)
    print("--- %s seconds ---" % (time.clock() - start_time))

def buildDB():
    """Main function to build the full database"""
    session = Session()
    #handleBungieTable()
    handleAccountTable()
    #handleAggregateTables()
    #handleCharacterTable()
    #handleWeaponUsageTable()
    #handleActivityStatsTable()
    #handleMedalTable()
    #handleAccountActivityModeStatsTable()
    #handleActivityHistory()
    #handleReferenceTables(session)

#infoMap = {'attrs':{'attr1':'attr1Name', ...}
#           ,'kwargs':{'kwargs1':'attr1', ...}
#           ,'url_params':{'param1':'attr1', ...}
#           ,'values':{'value1':'location1', ...}
#           ,'statics':{'static1':'attr1', ...}
#           ,'primary_keys':{'keyName1':'attr1', ...}}

def requestAndInsert(session, request_session, infoMap, staticMap, url, outFile, message, iterator, table, instrument=None):
    """Does everything else"""
    addList = []
    #Actual request done here
    data = jsonRequest(request_session, url, outFile, message)
    if data is None:
        print("No data retrieved.")
        return ([], None)
    #dynamicDictIndex gives us the specific iterator in the json we'll be using - could be games, characters, weapons, etc.
    group = dynamicDictIndex(data, iterator)
    if group == None:
        print("No group found.")
        return ([], None)
    if type(group) == list:
        for elem in group:
            if elem == None:
                continue
            #buildDict uses a nifty dynamic dictionary indexing function that allows us to grab info from multiply-nested fields in the dict
            insertDict = buildDict(elem, infoMap['values'])
            #Statics are pre-defined values - maybe the id from user.id in defineParams
            if 'statics' in infoMap:
                insertDict = {**insertDict, **staticMap}
            #Create a new element for insertion using kwargs
            #print(insertDict)
            insert_elem = table(**insertDict)
            inspection = inspect(insert_elem)
            objectDict = inspection.dict
            primaryKeyMap = {}
            for key in infoMap['primary_keys']:
                primaryKeyMap[key] = objectDict[key]
            #Upsert the element
            addList.append(upsert(table, primaryKeyMap, insert_elem, session))
    elif type(group) == dict:
        insertDict = buildDict(group, infoMap['values'])
        if 'statics' in infoMap:
            insertDict = {**insertDict, **staticMap}
        #Create a new element for insertion using kwargs
        #print(insertDict)
        insert_elem = table(**insertDict)
        inspection = inspect(insert_elem)
        objectDict = inspection.dict
        primaryKeyMap = {}
        for key in infoMap['primary_keys']:
            primaryKeyMap[key] = objectDict[key]
        #Upsert the element
        addList.append(upsert(table, primaryKeyMap, insert_elem, session))
    output = None
    if instrument is not None:
        #The only instrumentation we use so far is hasMore, but it's here if we need it for other things.
        output = dynamicDictIndex(data, instrument)
    return (addList, output)

def defineParams(queryTable, infoMap, urlFunction, iterator, table, altInsert=None, instrument=None):
    """Does like everything"""
    #Build a single request session for the duration of the table creation
    request_session = requests.session()
    session = Session()
    totalAddList = []
    #Elems is what we'll be iterating through - could be users, characters, etc.
    elems = session.query(queryTable).all()
    for elem in elems:
        #Attrs are the attributes associated with the elem. User.id or user.membership_type, for example. AKA fields in the database.
        attrMap = {}
        for (key, value) in infoMap['attrs'].items():
            if queryTable == Character:
                try: 
                    attrMap[key] = getattr(elem, value)
                except AttributeError:
                    attrMap[key] = getattr(session.query(Account).filter_by(id=attrMap['membershipId']).first(), value)
            else:
                attrMap[key] = getattr(elem, value)
        #Kwargs are used to check if the database needs updating for the current elem.
        kwargs = {}
        for (key, value) in infoMap['kwargs'].items():
            kwargs[key] = attrMap[value]
        if not needsUpdate(table, kwargs, session):
            print(f"Not updating {table.__tablename__} table for user: {queriedMap['name']}")
            continue
        #urlParams are used to build the request URL.
        urlParams = {}
        for (key, value) in infoMap['url_params'].items():
            urlParams[key] = attrMap[value]
        url = urlFunction(**urlParams)
        outFile = f"{attrMap['name']}_{table.__tablename__}.json"
        message = f"Fetching {table.__tablename__} data for: {attrMap['name']}"
        #Statics actually need to get passed to the insert function so they can be put in the table.
        staticMap = {}
        for (key, value) in infoMap['statics'].items():
            if value.endswith('_actual'):
                staticMap[key] = value[:-7]
            else:
                staticMap[key] = attrMap[value]
        if altInsert == None:
            (addList, output) = requestAndInsert(session, request_session, infoMap, staticMap, url, outFile, message, iterator, table, instrument)
        else:
            (addList, output) = altInsert(session, request_session, infoMap, staticMap, url, outFile, message, iterator, table, instrument)
        totalAddList = totalAddList + addList
    totalAddList = [item for item in totalAddList if item is not None]
    session.add_all(totalAddList)
    session.commit()

def handleBungieTable():
    """Fills Bungie table with all users in the clan"""
    def requestInfo(currentPage):
        clanUrl = f"{GROUP_URL_START}/Group/{os.environ['BUNGIE_CLANID']}/ClanMembers/?currentPage={currentPage}&platformType=2"
        outFile = f"clanUser_p{currentPage}.json"
        message = f"Fetching page {currentPage} of clan users."
        return (clanUrl, outFile, message)
    session = Session()
    request_session = requests.Session()
    totalAddList = []
    currentPage = 1
    queryTable = None
    infoMap = {'values' :{'id':[['bungieNetUserInfo', 'membershipId']]
                         ,'id_2':[['membershipId']]
                         ,'bungie_name':[['bungieNetUserInfo', 'displayName']]
                         ,'bungie_name_2':[['destinyUserInfo', 'displayName']]
                         ,'membership_type':[['bungieNetUserInfo', 'membershipType']]
                         ,'membership_type_2':[['destinyUserInfo', 'membershipType']]}
              ,'primary_keys' :['id']}
    clanUrl, outFile, message = requestInfo(currentPage)
    iterator = ['Response', 'results']
    table = Bungie
    instrument = ['Response', 'hasMore']
    (addList, output) = requestAndInsert(session, request_session, infoMap, {}, clanUrl, outFile, message, iterator, table, instrument)
    totalAddList = totalAddList + addList
    while output is True:
        currentPage += 1
        clanUrl, outFile, message = requestInfo(currentPage)
        (addList, output) = requestAndInsert(session, request_session, infoMap, {}, clanUrl, outFile, message, iterator, Bungie, instrument)
        totalAddList = totalAddList + addList
    totalAddList = [item for item in totalAddList if item is not None]
    session.add_all(totalAddList)
    session.commit()

def handleAccountTable():
    """Retrieve JSONs for users, listing their Destiny accounts. Fills account table."""
    def accountUrl(id, membershipType):
        return f"{GROUP_URL_START}/User/GetMembershipsById/{id}/{membershipType}"
    session = Session()
    queryTable = Bungie
    infoMap = {'attrs'  :{'id'             : 'id'
                         ,'name'           : 'bungie_name'
                         ,'membershipType' : 'membership_type'}
              ,'kwargs' :{'bungie_id' : 'id'}
              ,'url_params' :{'id'             : 'id'
                             ,'membershipType' : 'membershipType'}
              ,'values' :{'id'              : [['membershipId']]
                         ,'membership_type' : [['membershipType']]
                         ,'display_name'    : [['displayName']]}
              ,'statics' :{'bungie_id' : 'id'}
              ,'primary_keys' : ['id']}
    iterator = ['Response', 'destinyMemberships']
    table = Account
    defineParams(queryTable, infoMap, accountUrl, iterator, table)

def handleAggregateTables():
    """Fills pvpAggregate and pveAggregate with aggregate stats."""
    def aggregateStatsUrl(membershipType, id):
        return f"{URL_START}/Destiny/Stats/Account/{membershipType}/{id}"
    def altInsert(session, request_session, infoMap, staticMap, url, outFile, message, iterator, table, instrument=None):
        def fillAndInsertDict(stats, table, statics):
            insertDict = {}
            if stats == None:
                return None
            for stat in stats:
                if 'pga' in stats[stat]:
                    insertDict[stat+'pg'] = stats[stat]['pga']['value']
                insertDict[stat] = stats[stat]['basic']['value']
            insertDict = {**insertDict, **staticMap}
            insert_elem = table(**insertDict)
            inspection = inspect(insert_elem)
            objectDict = inspection.dict
            primaryKeyMap = {}
            for key in infoMap['primary_keys']:
                primaryKeyMap[key] = objectDict[key]
            return upsert(table, primaryKeyMap, insert_elem, session)
        #Actual request done here
        data = jsonRequest(request_session, url, outFile, message)
        if data is None:
            print("No data retrieved.")
            return ([], None)
        #dynamicDictIndex gives us the specific iterator in the json we'll be using - could be games, characters, weapons, etc.
        tables = [PvPAggregate, PvEAggregate]
        addList = []
        for table in tables:
            if table == PvPAggregate:
                mode = 'allPvP'
            elif table == PvEAggregate:
                mode = 'allPvE'
            stats = dynamicDictIndex(data, iterator+[mode, 'allTime'])
            addList.append(fillAndInsertDict(stats, table, staticMap))
        return (addList, None)
    
    session = Session()
    queryTable = Account
    infoMap = {'attrs'  :{'id'             : 'id'
                         ,'name'           : 'display_name'
                         ,'membershipType' : 'membership_type'}
              ,'kwargs' :{'id' : 'id'}
              ,'url_params' :{'id'             : 'id'
                             ,'membershipType' : 'membershipType'}
              ,'values' :{'getAllStats' : [[],[]]}
              ,'statics' :{'id' : 'id'}
              ,'primary_keys' : ['id']}
    iterator = ['Response', 'mergedAllCharacters', 'results']
    queryTable = Account
    table = PvPAggregate
    defineParams(queryTable, infoMap, aggregateStatsUrl, iterator, table, altInsert)

def handleCharacterTable():
    def characterUrl(membershipId, membershipType):
        return f"{URL_START}/Destiny/{membershipType}/Account/{membershipId}"
    session = Session()
    queryTable = Account
    infoMap = {'attrs' :{'membershipId' : 'id'
                        ,'name' : 'display_name'
                        ,'membershipType' : 'membership_type'}
              ,'kwargs' :{'membership_id' : 'membershipId'}
              ,'url_params' :{'membershipId' : 'membershipId'
                             ,'membershipType' : 'membershipType'}
              ,'values' :{'id' : [['characterBase', 'characterId']]
                         ,'minutes_played' : [['characterBase', 'minutesPlayedTotal']]
                         ,'light_level' : [['characterBase', 'powerLevel']]
                         ,'class_hash' : [['characterBase', 'classHash']]
                         ,'grimoire' : [['characterBase', 'grimoireScore']]}
              ,'statics' :{'membership_id' : 'membershipId'}
              ,'primary_keys' : ['id']}
    iterator = ['Response', 'data', 'characters']
    table = Character
    defineParams(queryTable, infoMap, characterUrl, iterator, table)

def handleWeaponUsageTable():
    def weaponUrl(id, membershipType):
        #0 can be used instead of character ids
        return f"{URL_START}/Destiny/Stats/UniqueWeapons/{membershipType}/{id}/0"
    session = Session()
    queryTable = Account
    infoMap = {'attrs' :{'id' : 'id'
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
    defineParams(queryTable, infoMap, weaponUrl, iterator, table)

def handleActivityStatsTable():
    def activityUrl(id, membershipId, membershipType):
        return f"{URL_START}/Destiny/Stats/AggregateActivityStats/{membershipType}/{membershipId}/{id}/"
    session = Session()
    queryTable = Character
    infoMap = {'attrs' :{'id' : 'id'
                        ,'membershipId' : 'membership_id'
                        ,'name' : 'display_name'
                        ,'membershipType' : 'membership_type'}
              ,'kwargs' :{'id' : 'id'}
              ,'url_params' :{'id' : 'id'
                             ,'membershipId' : 'membershipId'
                             ,'membershipType' : 'membershipType'}
              ,'values' :{'activityHash' : [['activityHash']]
                         ,'getAllStats' : [['values'], ['basic', 'value']]}
              ,'statics' :{'id' : 'id'}
              ,'primary_keys' : ['id', 'activityHash']}
    iterator = ['Response', 'data', 'activities']
    table = CharacterActivityStats
    defineParams(queryTable, infoMap, activityUrl, iterator, table)

def handleMedalTable():
    def medalUrl(id, membershipType):
        return f"{URL_START}/Destiny/Stats/Account/{membershipType}/{id}/?Groups=Medals"
    session = Session()
    queryTable = Account
    infoMap = {'attrs' :{'id' : 'id'
                        ,'name' : 'display_name'
                        ,'membershipType' : 'membership_type'}
              ,'kwargs' :{'id' : 'id'}
              ,'url_params' :{'id' : 'id'
                             ,'membershipType' : 'membershipType'}
              ,'values' :{'getAllStats' : [[], ['basic', 'value']]}
              ,'statics' :{'id' : 'id'}
              ,'primary_keys' : ['id']}
    iterator = ['Response', 'mergedAllCharacters', 'merged', 'allTime']
    table = AccountMedals
    defineParams(queryTable, infoMap, medalUrl, iterator, table)

def handleAccountActivityModeStatsTable():
    def activityModeUrl(id, membershipType, mode):
        return f"{URL_START}/Destiny/Stats/{membershipType}/{id}/0/?modes={mode}"
    session = Session()
    queryTable = Account
    modeDict = {2:'story', 3:'strike', 4:'raid', 5:'allPvP', 6:'patrol', 7:'allPvE', 8:'pvpIntroduction', 9:'threeVsThree', 10:'control'
               ,11 : 'lockdown', 12:'team', 13:'freeForAll', 14:'trialsOfOsiris', 15:'doubles', 16:'nightfall', 17:'heroic', 18:'allStrikes', 19:'ironBanner', 20:'allArena'
               ,21 : 'arena', 22:'arenaChallenge', 23:'elimination', 24:'rift', 25:'allMayhem', 26:'mayhemClash', 27:'mayhemRumble', 28:'zoneControl', 29:'racing', 30:'arenaElderChallenge'
               ,31 : 'supremacy', 32:'privateMatchesAll', 33:'supremacyRumble', 34:'supremacyClash', 35:'supremacyInferno', 36:'supremacyMayhem'}
    table = AccountActivityModeStats
    for mode in range(2,37):
        infoMap = {'attrs' :{'id' : 'id'
                            ,'name' : 'display_name'
                            ,'membershipType' : 'membership_type'}
                ,'kwargs' :{'id' : 'id'}
                ,'url_params' :{'id' : 'id'
                                ,'membershipType' : 'membershipType'}
                ,'values' :{'getAllStats' : [['allTime'], ['basic', 'value']]}
                ,'statics' :{'id' : 'id'
                            ,'mode' : f'{modeDict[mode]}_actual'}
                ,'primary_keys' : ['id', 'mode']}
        partialUrl = partial(activityModeUrl, mode=mode)
        iterator = ['Response', f'{modeDict[mode]}', 'allTime']
        defineParams(queryTable, infoMap, partialUrl, iterator, table)

def handleReferenceTables(session):
    """Connects to the manifest.content database and builds the necessary reference tables."""
    def buildReferenceTable(tableName, table, statement, dictionary, condition=None):
        print(f"Building {tableName} reference table...")
        con = sqlite3.connect(os.environ['MANIFEST_CONTENT'])
        cur = con.cursor()
        with con:
            cur.execute(statement)
            group = cur.fetchall()
            for item in group:
                itemInfo = json.loads(item[1])
                itemDict = {}
                if not condition is None and condition(itemInfo):
                    continue
                for (key,value) in dictionary.iteritems():
                    itemDict[key] = itemInfo[value]
                new_item_def = table(**itemDict)
                upsert(table, new_item_def, session)

    # Classes
    classTable = ClassReference
    classInfo = {'id':'classHash', 'class_name':'className'}
    classStatement = "SELECT * FROM DestinyClassDefinition"
    classDict = buildReferenceTable("class", classTable, classStatement, classInfo)

    # Weapons
    weaponTable = WeaponReference
    weaponInfo = {'id':'itemHash', 'weapon_name':'itemName', 'weapon_type':'itemTypeName', 'weapon_rarity':'tierTypeName'}
    weaponStatement = "SELECT * FROM DestinyInventoryItemDefinition"
    def weaponCondition(info):
        weapon_types = ['Rocket Launcher', 'Scout Rifle', 'Fusion Rifle', 'Sniper Rifle', 'Shotgun', 'Machine Gun', 'Pulse Rifle', 'Auto Rifle', 'Hand Cannon', 'Sidearm']
        return not ("itemTypeName" in info and info['itemTypeName'] in weapon_types)
    weaponDict = buildReferenceTable("weapon", weaponTable, weaponStatement, weaponInfo, weaponCondition)

    # Activities
    activityTable = ActivityReference
    activityInfo = {'id':'activityHash', 'activity_name':'activityName', 'activity_type_hash':'activityTypeHash'}
    activityStatement = "SELECT * FROM DestinyActivityDefinition"
    def activityCondition(info):
        return not ("activityName" in info)
    activityDict = buildReferenceTable("activity", activityTable, activityStatement, activityInfo, activityCondition)

    # Activity types
    activityTypeTable = ActivityTypeReference
    activityTypeInfo = {'id':'activityTypeHash', 'activity_type_name':'activityTypeName'}
    activityTypeStatement = "SELECT * FROM DestinyActivityTypeDefinition"
    def activityTypeCondition(info):
        return not ("activityTypeName" in info)
    activityTypeDict = buildReferenceTable("activity type", activityTypeTable, activityTypeStatement, activityTypeInfo, activityTypeCondition)

    # Buckets
    bucketTable = BucketReference
    bucketInfo = {'id':'bucketHash', 'bucket_name':'bucketName'}
    bucketStatement = "SELECT * FROM DestinyInventoryBucketDefinition"
    def bucketCondition(info): 
        return not ("bucketName" in info)
    bucketDict = buildReferenceTable("bucket", bucketTable, bucketStatement, bucketInfo, bucketCondition)

def dynamicDictIndex(dct, value):
    try:
        ret = dct
        for item in value:
            ret = ret[item]
    except KeyError:
        ret = None
    return ret

def buildDict(dct, valueMap):
    outDict = {}
    for (key, valList) in valueMap.items():
        if len(valList) == 1:
            if key.endswith('_2'):
                key = key[:-2]
            if (key in outDict and outDict[key] == None) or (key not in outDict):
                outDict[key] = dynamicDictIndex(dct, valList[0])
        else:
            loopDict = dynamicDictIndex(dct, valList[0])
            if loopDict == None:
                continue
            if key == 'getAllStats':
                for item in loopDict:
                    outDict[item] = dynamicDictIndex(loopDict, [item]+valList[1])
            else:
                outDict[key] = dynamicDictIndex(loopDict, valList[1])
    return outDict

def jsonRequest(request_session, url, outFile, message=""):
    print(f"Connecting to Bungie: {url}")
    print(message)
    headers = makeHeader()
    #print(url)
    res = request_session.get(url, headers=headers)
    #print(res.text)
    try:
        data = res.json()
    except json.decoder.JSONDecodeError:
        print(res.text)
        return None
    error_stat = data['ErrorStatus']
    if error_stat == "Success":
        #with open(f"JSON/{outFile}","w+") as f:
        #    json.dump(data, f)
        return data
    else:
        print("Error Status: " + error_stat)
        return None 

def upsert(table, primaryKeyMap, obj, session):
    add = False
    first = session.query(table).filter_by(**primaryKeyMap).first()
    add = False
    if first != None:
        session.query(table).filter_by(**primaryKeyMap).update({column: getattr(obj, column) for column in table.__table__.columns.keys()})
    else:
        add = True
    if add:
        return obj
    else:
        return None

def needsUpdate(table, kwargs, session):
    now = datetime.now()
    try:
        lastUpdate = session.query(table).filter_by(**kwargs).first().last_updated
        print("Fetching last update...")
        daysSince = (now - lastUpdate).days
        #print (f"Days since update: {daysSince}")
        return daysSince >= UPDATE_DIFF
    except (AttributeError, TypeError):
        return True

if __name__ == "__main__":
    # loadConfig for testing purposes
    APP_PATH = "/etc/destinygotg"
    loadConfig()
    import time
    start_time = time.time()
    buildDB()
    print("--- %s seconds ---" % (time.time() - start_time))
