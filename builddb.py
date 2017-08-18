#!/usr/bin/python
#This file (with update option set) is run daily; it pulls new clan members and new accounts. For existing members, it adds newly created characters, and updates all existing stats.
#Perhaps most importantly, it pulls in new activities completed by all members.
import os, sys
import json, requests
import sqlite3
from datetime import datetime
from sqlalchemy import exists, and_
from sqlalchemy.sql.expression import literal_column
from initdb import Base, Bungie, Account, PvPAggregate, PvEAggregate, Character, CharacterUsesWeapon, ActivityStatsAccount, MedalsCharacter, ActivityReference, ClassReference, WeaponReference, ActivityTypeReference, BucketReference, CharacterStatMayhemClash, LastUpdated
from destinygotg import Session, loadConfig
sys.path.append("./")
import importlib, time, itertools
endpoints = importlib.import_module("Destiny-API-Frameworks.python.endpoints")

URL_START = "https://bungie.net/Platform"
#URL_START = "https://bungie.net/D1/Platform"
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
    #handleAccountTable()
    #handleAggregateTables()
    #handleCharacterTable()
    #timeit(oldHandleAggregateActivities, session)
    timeit(handleActivityStatsTable)
    #handleAggregateActivities(session)
    #handleMedals(session)
    #handleWeaponUsage(session)
    #handleActivityHistory(session)
    #handleReferenceTables(session)

#infoMap = {'attrs':{'attr1':'attr1Name', ...}
#           ,'kwargs':{'kwargs1':'attr1', ...}
#           ,'url_params':{'param1':'attr1', ...}
#           ,'values':{'value1':'location1', ...}
#           ,'statics':{'static1':'attr1', ...}

def requestAndInsert(session, request_session, infoMap, staticMap, url, outFile, message, iterator, table, instrument=None):
    """Does everything else"""
    #Actual request done here
    data = jsonRequest(request_session, url, outFile, message)
    if data is None:
        print("No data retrieved.")
        return None
    #dynamicDictIndex gives us the specific iterator in the json we'll be using - could be games, characters, weapons, etc.
    group = dynamicDictIndex(data, iterator)
    print(group) 
    for elem in group:
        #buildDict uses a nifty dynamic dictionary indexing function that allows us to grab info from multiply-nested fields in the dict
        insertDict = buildDict(elem, infoMap['values'])
        #Statics are pre-defined values - maybe the id from user.id in defineParams
        if 'statics' in infoMap:
            insertDict = {**insertDict, **staticMap}
        #Create a new element for insertion using kwargs
        insert_elem = table(**insertDict)
        #Upsert the element
        insertOrUpdate(table, insert_elem, session)
    if instrument is not None:
        #The only instrumentation we use so far is hasMore, but it's here if we need it for other things.
        output = dynamicDictIndex(data, instrument)
        return output

def defineParams(queryTable, infoMap, urlFunction, iterator, table, altInsert=None, instrument=None):
    """Does like everything"""
    #Build a single request session for the duration of the table creation
    request_session = requests.session()
    session = Session()
    #Elems is what we'll be iterating through - could be users, characters, etc.
    elems = session.query(queryTable).all()
    for elem in elems:
        #Attrs are the attributes associated with the elem. User.id or user.membership_type, for example. AKA fields in the database.
        attrMap = {}
        for (key, value) in infoMap['attrs'].items():
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
            staticMap[key] = attrMap[value]
        if altInsert == None:
            requestAndInsert(session, request_session, infoMap, staticMap, url, outFile, message, iterator, table, instrument)
        else:
            altInsert(session, request_session, infoMap, staticMap, url, outFile, message, iterator, table, instrument)

def handleBungieTable():
    """Fills Bungie table with all users in the clan"""
    session = Session()
    request_session = requests.session()
    currentPage = 1
    clan_url = f"{URL_START}/Group/{os.environ['BUNGIE_CLANID']}/ClanMembers/?currentPage={currentPage}&platformType=2"
    outFile = f"clanUser_p{currentPage}.json"
    message = f"Fetching page {currentPage} of clan users."
    iterator = ['Response', 'results']
    infoMap = {'values' :{'id':[['bungieNetUserInfo', 'membershipId'], ['membershipId']]
                         ,'bungie_name':[['bungieNetUserInfo', 'displayName'], ['destinyUserInfo','displayName']]
                         ,'membership_type':[['bungieNetUserInfo', 'membershipType'], ['destinyUserInfo', 'membershipType']]}}
    instrument = ['Response', 'hasMore']
    output = requestAndInsert(session, request_session, infoMap, {}, clan_url, outFile, message, iterator, Bungie, instrument)
    while output is True:
        currentPage += 1
        clan_url = f"{URL_START}/Group/{os.environ['BUNGIE_CLANID']}/ClanMembers/?currentPage={currentPage}&platformType=2"
        outFile = f"clanUser_p{currentPage}.json"
        message = f"Fetching page {currentPage} of clan users."
        output = requestAndInsert(session, request_session, infoMap, {}, clan_url, outFile, message, iterator, Bungie, instrument)

def handleAccountTable():
    """Retrieve JSONs for users, listing their Destiny accounts. Fills account table."""
    def accountUrl(id, membershipType):
        return f"{URL_START}/User/GetMembershipsById/{id}/{membershipType}"
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
              ,'statics' :{'bungie_id' : 'id'}}
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
            insertOrUpdate(table, insert_elem, session)
        #Actual request done here
        data = jsonRequest(request_session, url, outFile, message)
        if data is None:
            print("No data retrieved.")
            return None
        #dynamicDictIndex gives us the specific iterator in the json we'll be using - could be games, characters, weapons, etc.
        tables = [PvPAggregate, PvEAggregate]
        for table in tables:
            if table == PvPAggregate:
                mode = 'allPvP'
            elif table == PvEAggregate:
                mode = 'allPvE'
            stats = dynamicDictIndex(data, iterator+[mode, 'allTime'])
            fillAndInsertDict(stats, table, staticMap)
    
    session = Session()
    queryTable = Account
    infoMap = {'attrs'  :{'id'             : 'id'
                         ,'name'           : 'display_name'
                         ,'membershipType' : 'membership_type'}
              ,'kwargs' :{'id' : 'id'}
              ,'url_params' :{'id'             : 'id'
                             ,'membershipType' : 'membershipType'}
              ,'values' :{'getAllStats' : ''}
              ,'statics' :{'id' : 'id'}}
    iterator = ['Response', 'mergedAllCharacters', 'results']
    queryTable = Account
    table = PvPAggregate
    defineParams(queryTable, infoMap, aggregateStatsUrl, iterator, table, altInsert)

def handleCharacterTable():
    def characterUrl(id, membershipType):
        return f"{URL_START}/Destiny/{membershipType}/Account/{id}"
    session = Session()
    queryTable = Account
    infoMap = {'attrs' :{'id' : 'id'
                        ,'name' : 'display_name'
                        ,'membershipType' : 'membership_type'}
              ,'kwargs' :{'id' : 'id'}
              ,'url_params' :{'id' : 'id'
                             ,'membershipType' : 'membershipType'}
              ,'values' :{'id' : [['characterBase', 'characterId']]
                         ,'minutes_played' : [['characterBase', 'minutesPlayedTotal']]
                         ,'light_level' : [['characterBase', 'powerLevel']]
                         ,'class_hash' : [['characterBase', 'classHash']]
                         ,'grimoire' : [['characterBase', 'grimoireScore']]}
              ,'statics' :{'id' : 'id'}}
    iterator = ['Response', 'data', 'characters']
    table = Character
    defineParams(queryTable, infoMap, characterUrl, iterator, table)

def handleActivityStatsTable():
    def activityUrl(id, membershipType):
        return f"{URL_START}/Destiny/Stats/AggregateActivityStats/{membershipType}/{id}/{c_id}/"
    session = Session()
    queryTable = Account
    infoMap = {'attrs' :{'id' : 'id'
                        ,'name' : 'display_name'
                        ,'membershipType' : 'membership_type'}
              ,'kwargs' :{'id' : 'id'}
              ,'url_params' :{'id' : 'id'
                             ,'membershipType' : 'membershipType'}
              ,'values' :{'activity_hash' : 'activityHash'
                         ,'getAllStats' : [['placeholder', 'basic', 'value']]}
              ,'statics' :{'id' : 'id'}}
    iterator = ['Response', 'data', 'activities']
    table = ActivityStatsAccount
    defineParams(queryTable, infoMap, activityUrl, iterator, table)

def oldHandleAggregateActivities(session):
    """Retrieve aggregate activity stats for users. Builds aggregateStatsCharacter table."""
    characters = session.query(Character).all()
    for character in characters:
        characterId = character.id
        membershipId = character.membership_id
        displayName = session.query(Account).filter_by(id=membershipId).first().display_name
        kwargs = {"id" : characterId}
        if not needsUpdate(AggregateStatsCharacter, kwargs, session):
            print(f"Not updating AggregateStatsCharacter table for user: {displayName}")
            continue
        membershipType = session.query(Account).filter_by(id=membershipId).first().membership_type
        stat_url = f"{URL_START}/Destiny/Stats/AggregateActivityStats/{membershipType}/{membershipId}/{characterId}"
        message = f"Fetching aggregate activity stats for: {displayName}"
        outFile =f"{displayName}_activities.json"
        data = jsonRequest(stat_url, outFile, message)
        if data is None:
            #TODO: Throw an error
            print("")
            continue
        #This part does the heavy lifting of table building
        aggStatDict = {}
        aggStatDict['id'] = characterId
        activities = data['Response']['data']['activities']
        for activity in activities:
            aggStatDict['activity_hash'] = activity['activityHash']
            for value in activity['values']:
                aggStatDict[value] = activity['values'][value]['basic']['value']
        new_aggregate_statistics = AggregateStatsCharacter(**aggStatDict)
        insertOrUpdate(AggregateStatsCharacter, new_aggregate_statistics, session)

def handleWeaponUsage(session):
    """Retrieve weapon usage for characters. Builds characterUsesWeapon table."""
    characters = session.query(Character).all()
    for character in characters:
        characterId = character.id
        membershipId = character.membership_id
        displayName = session.query(Account).filter_by(id=membershipId).first().display_name
        kwargs = {"character_id" : characterId}
        if not needsUpdate(CharacterUsesWeapon, kwargs, session):
            print(f"Not updating CharacterUsesWeapon table for user: {displayName}")
            continue
        membershipType = session.query(Account).filter_by(id=membershipId).first().membership_type
        stat_url = f"{URL_START}/Destiny/Stats/UniqueWeapons/{membershipType}/{membershipId}/{characterId}"
        message = f"Fetching weapon usage stats for: {displayName}"
        outFile = f"{displayName}_weapons.json"
        data = jsonRequest(stat_url, outFile, message)
        if data is None:
            #TODO: Throw an error
            print("")
            continue
        elif data['Response']['data'] == {}:
            continue
        weapons = data['Response']['data']['weapons']
        for weapon in weapons:
            weaponDict = {}
            weaponDict['character_id'] = characterId
            weaponDict['id'] = weapon['referenceId']
            weaponValues = weapon['values']
            weaponDict['kills'] = weaponValues['uniqueWeaponKills']['basic']['value']
            weaponDict['precision_kills'] = weaponValues['uniqueWeaponPrecisionKills']['basic']['value']
            weaponDict['precision_kill_percentage'] = weaponValues['uniqueWeaponKillsPrecisionKills']['basic']['value']
            new_weapon_stats = CharacterUsesWeapon(**weaponDict)
            
            matches = session.query(exists().where(and_(CharacterUsesWeapon.id == new_weapon_stats.id, CharacterUsesWeapon.character_id == new_weapon_stats.character_id))).scalar()
            if matches:
                # We have to do some strange things to pass update statements. This creates a dynamic dictionary to update all fields.
                session.query(CharacterUsesWeapon).filter_by(id=new_weapon_stats.id, character_id=new_weapon_stats.character_id).update({column: getattr(new_weapon_stats, column) for column in CharacterUsesWeapon.__table__.columns.keys()})
            else:
                session.add(new_weapon_stats)
            session.commit()

def handleMedals(session):
    """Retrieve aggregate activity stats for users. Builds aggregateStatsCharacter table."""
    accounts = session.query(Account).all()
    for account in accounts:
        membershipId = account.id
        displayName = session.query(Account).filter_by(id=membershipId).first().display_name
        kwargs = {"membership_id" : membershipId}
        if not needsUpdate(MedalsCharacter, kwargs, session):
            print(f"Not updating MedalsCharacter table for user: {displayName}")
            continue
        membershipType = session.query(Account).filter_by(id=membershipId).first().membership_type
        stat_url = f"{URL_START}/Destiny/Stats/Account/{membershipType}/{membershipId}/?Groups=Medals"
        message = f"Fetching medal stats for: {displayName}"
        outFile = f"{displayName}_medals.json"
        data = jsonRequest(stat_url, outFile, message)
        if data is None:
            #TODO: Throw an error
            print("")
            continue
        
        #This part does the heavy lifting of table building
        medalDict = {}
        characters = data['Response']['characters']
        for character in characters:
            medalDict['id'] = character['characterId']
            medalDict['membership_id'] = membershipId
            if 'merged' in character and 'allTime' in character['merged']:
                for medal in character['merged']['allTime']:
                    medalDict[medal] = character['merged']['allTime'][medal]['basic']['value']
            new_medal_statistics = MedalsCharacter(**medalDict)
            insertOrUpdate(MedalsCharacter, new_medal_statistics, session)

# This is going to be a lot. 2-36 are all different activity modes that will each require tracking.
def handleActivityHistory(session):
    accounts = session.query(Account).all()
    for account in accounts:
        membershipId = account.id
        displayName = account.display_name
        kwargs = {"id" : membershipId}
        if not needsUpdate(CharacterStatMayhemClash, kwargs, session):
            pass
            print(f"Not updating CharacterStatMayhemClash table for user: {displayName}")
            continue
        membershipType = account.membership_type
        stat_url = f"{URL_START}/Destiny/Stats/{membershipType}/{membershipId}/0/?modes=MayhemClash"
        message = f"Fetching mayhem clash stats for: {displayName}"
        outFile = f"{displayName}_stats.json"
        data = jsonRequest(stat_url, outFile, message)
        print("Data received.")
        if data is None:
            #TODO: Throw an error
            print("")
            continue
        
        #This part does the heavy lifting of table building
        actDict = {}
        actDict['id'] = membershipId
        if 'allTime' in data['Response']['mayhemClash']:
            stats = data['Response']['mayhemClash']['allTime']
        else:
            continue
        for stat in stats:
            actDict[stat] = stats[stat]['basic']['value']
            new_activity_statistics = CharacterStatMayhemClash(**actDict)
            insertOrUpdate(CharacterStatMayhemClash, new_activity_statistics, session)

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
                for (key,value) in dictionary.items():
                    itemDict[key] = itemInfo[value]
                new_item_def = table(**itemDict)
                insertOrUpdate(table, new_item_def, session)

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
    print(dct, value)
    try:
        ret = dct
        for item in value:
            ret = ret[item]
    except KeyError:
        ret = None
    return ret

def buildDict(dct, valueMap):
    def getAllStats(dct, path):
        outDict = {}
        if path == [[""]]:
            for (key, value) in dct.items():
                outDict[key] = value
        else:
            for (key, value) in dynamicDictIndex(dct, path).items():
                outDict[key] = value
        return outDict
    outDict = {}
    if 'getAllStats' in valueMap.keys():
        outDict = getAllStats(dct)
    else:
        for (key, valList) in valueMap.items():
            print(key, valList)
            if 'placeholder' in valList[0]:
                valList = valList[0]
                firstTier = list(itertools.takewhile(lambda x: x != 'placeholder', valList)) 
                secondTier = list(itertools.dropwhile(lambda x: x != 'placeholder', valList))[1:]
                newDict = dynamicDictIndex(dct, firstTier)
                if secondTier == ['getAllStats']:
                    outDict = {**outDict, **getAllStats(newDict, "")}
                else:
                    outDict[key] = dynamicDictIndex(newDict, secondTier)
            else:
                ret = dynamicDictIndex(dct, valList[0])
                if ret == None:
                    ret = dynamicDictIndex(dct, valList[1])
                outDict[key] = ret
    return outDict

def jsonRequest(request_session, url, outFile, message=""):
    print(f"Connecting to Bungie: {url}")
    print(message)
    headers = makeHeader()
    #print(url)
    res = request_session.get(url, headers=headers)
    #print(res.text)
    data = res.json()
    error_stat = data['ErrorStatus']
    if error_stat == "Success":
        #with open(outFile,"w+") as f:
        #    json.dump(data, f)
        return data
    else:
        print("Error Status: " + error_stat)
        return None 

def insertOrUpdate(table, obj, session):
    matches = session.query(exists().where(table.id == obj.id)).scalar()
    if matches:
        # We have to do some strange things to pass update statements. This create a dynamic dictionary to update all fields.
        session.query(table).filter_by(id=obj.id).update({column: getattr(obj, column) for column in table.__table__.columns.keys()})
    else:
        session.add(obj)
    session.commit()

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
