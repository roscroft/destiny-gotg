#!/usr/bin/python
#This file (with update option set) is run daily; it pulls new clan members and new accounts. For existing members, it adds newly created characters, and updates all existing stats.
#Perhaps most importantly, it pulls in new activities completed by all members.
import os, sys
import json, requests
import sqlite3
from datetime import datetime
from sqlalchemy import exists, and_
from sqlalchemy.sql.expression import literal_column
from initdb import Base, Bungie, Account, PvPTotal, PvPAverage, PvETotal, PvEAverage, Character, CharacterUsesWeapon, AggregateStatsCharacter, ActivityReference, ClassReference, WeaponReference, ActivityTypeReference
from destinygotg import Session, loadConfig

URL_START = "https://bungie.net/Platform"
UPDATE_DIFF = 1 # Number of days between updates

def makeHeader():
    return {'X-API-KEY':os.environ['BUNGIE_APIKEY']}

def buildDB():
    """Main function to build the full database"""
    session = Session()
    #handleBungieUsers(session)
    #handleDestinyUsers(session)
    #handleAggregateStats(session)
    #handleCharacters(session)
    #handleAggregateActivities(session)
    handleWeaponUsage(session)
    #handleReferenceTables(session)

def handleBungieUsers(session):
    """Retrieve JSON containing all clan users, and build the Bungie table from the JSON"""
    clan_url = f"{URL_START}/Group/{os.environ['BUNGIE_CLANID']}/Membersv3/?lc=en&fmt=true&currentPage=1&platformType=2"
    outFile = "clanUser_p1.json"
    message = "Fetching page 1 of clan users."
    data = jsonRequest(clan_url, outFile, message)
    if data is None:
        #TODO: Throw some error or something
        print("")
    
    #This section stores all clan users in the Bungie table 
    for user in data['Response']['results']:
        bungieDict = {}
        bungieDict['last_updated'] = datetime.now()
        bungieDict['membership_type']=254
        bungieDict['id'] = user['user']['membershipId']
        #Some people have improperly linked accounts, this will handle those by setting bungieId as their PSN id
        if bungieDict['id'] == '0':
            bungieDict['id'] = user['membershipId']
            bungieDict['membership_type'] = user['membershipType']
        bungieDict['bungie_name'] = user['user']['displayName']
        bungie_user = Bungie(**bungieDict)
        insertOrUpdate(Bungie, bungie_user, session)

def handleDestinyUsers(session):
    """Retrieve JSONs for users, listing their Destiny accounts. Builds account table."""
    users = session.query(Bungie).all()
    for user in users:
        bungieId = user.id
        bungieName = user.bungie_name
        kwargs = {"bungie_id" : bungieId}
        if not needsUpdate(Account, kwargs, session):
            print(f"Not updating account table for user: {bungieName}")
            continue
        membershipType = user.membership_type
        user_url = f"{URL_START}/User/GetMembershipsById/{bungieId}/{membershipType}/"
        message = f"Fetching membership data for: {bungieName}"
        outFile = f"{bungieName}.json"
        data = jsonRequest(user_url, outFile, message)
        if data is None:
            #TODO: Throw an error
            print("")
            continue

        #Grab all of the individual accounts and put them in the Account table
        accounts = data['Response']['destinyMemberships']
        for account in accounts:
            accountDict = {}
            accountDict['last_updated'] = datetime.now()
            accountDict['id'] = account['membershipId']
            accountDict['membership_type'] = account['membershipType']
            accountDict['display_name'] = account['displayName']
            accountDict['bungie_id'] = bungieId
            new_account = Account(**accountDict)
            insertOrUpdate(Account, new_account, session)

def handleAggregateStats(session):
    """Retrieve aggregate stats for users. Builds PvP and PvE average and total tables."""
    accounts = session.query(Account).all()
    for account in accounts:
        membershipId = account.id
        displayName = account.display_name
        kwargs = {"id" : membershipId}
        if not needsUpdate(PvPTotal, kwargs, session):
            print(f"Not updating PvP and PvE tables for user: {displayName}")
            continue
        membershipType = account.membership_type
        stat_url = f"{URL_START}/Destiny/Stats/Account/{membershipType}/{membershipId}"
        message = f"Fetching aggregate historical stats for: {displayName}"
        outFile = f"{displayName}_stats.json"
        data = jsonRequest(stat_url, outFile, message)
        if data is None:
            #TODO: Throw an error
            print("")
            continue

        #This part does the heavy lifting of table building
        #PvP first
        pvpTotalDict = {}
        pvpAvgDict = {}
        pveTotalDict = {}
        pveAvgDict = {}
        
        def fillDict(avgDict, totalDict, pvpOrPve):
            #We need to check if stats exist (if mode hasn't been played, there will be no stats
            allTime = data['Response']['mergedAllCharacters']['results'][pvpOrPve]
            if not 'allTime' in allTime:
                return None
            stats = allTime['allTime']
            for stat in stats:
                if 'pga' in stats[stat]:
                    avgDict[stat] = stats[stat]['pga']['value']
                totalDict[stat] = stats[stat]['basic']['value']

        fillDict(pvpAvgDict, pvpTotalDict, 'allPvP')
        fillDict(pveAvgDict, pveTotalDict, 'allPvE')
        
        #Now we just need to tack on the membershipId
        pvpTotalDict['id'] = membershipId
        pvpAvgDict['id'] = membershipId
        pveTotalDict['id'] = membershipId
        pveAvgDict['id'] = membershipId
        pvpTotalDict['last_updated'] = datetime.now()
        pvpAvgDict['last_updated'] = datetime.now()
        pveTotalDict['last_updated'] = datetime.now()
        pveAvgDict['last_updated'] = datetime.now()
        #And put these in the database. Double **s unpack a dictionary into the row.
        new_pvp_total = PvPTotal(**pvpTotalDict)
        new_pvp_avg = PvPAverage(**pvpAvgDict)
        new_pve_total = PvETotal(**pveTotalDict)
        new_pve_avg = PvEAverage(**pveAvgDict)
        insertOrUpdate(PvPTotal, new_pvp_total, session)
        insertOrUpdate(PvPAverage, new_pvp_avg, session)
        insertOrUpdate(PvETotal, new_pve_total, session)
        insertOrUpdate(PvEAverage, new_pve_avg, session)

def handleCharacters(session):
    """Retrieve JSONs for accounts, listing their Destiny characters. Builds characters table."""
    accounts = session.query(Account).all()
    for account in accounts:
        membershipId = account.id
        displayName = account.display_name
        kwargs = {"membership_id" : membershipId}
        if not needsUpdate(Character, kwargs, session):
            print(f"Not updating character table for user: {displayName}")
            continue
        membershipType = account.membership_type
        account_url = f"{URL_START}/Destiny/{membershipType}/Account/{membershipId}"
        message = f"Fetching character data for: {displayName}"
        outFile = f"{displayName}_characters.json"
        data = jsonRequest(account_url, outFile, message)
        if data is None:
            #TODO: Throw an error
            continue

        #Grab all of the individual accounts and put them in the Account table
        characters = data['Response']['data']['characters']
        for character in characters:
            characterDict = {}
            characterDict['last_updated'] = datetime.now()
            characterDict['id'] = character['characterBase']['characterId']
            characterDict['minutes_played'] = character['characterBase']['minutesPlayedTotal']
            characterDict['light_level'] = character['characterBase']['powerLevel']
            characterDict['membership_id'] = membershipId
            characterDict['class_hash'] = character['characterBase']['classHash']
            new_character = Character(**characterDict)
            insertOrUpdate(Character, new_character, session)

#TODO: Next 2 functions are basically identical (and can be written identically). Abstract out.
def handleAggregateActivities(session):
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
        
        #This part does the heavy lifting of table building
        aggStatDict = {}
        aggStatDict['last_updated'] = datetime.now()
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
        kwargs = {"id" : characterId}
        if not needsUpdate(CharacterUsesWeapon, kwargs, session):
            print(f"Not updating CharacterUsesWeapon table for user: {displayName}")
            continue
        membershipType = session.query(Account).filter_by(id=membershipId).first().membership_type
        stat_url = f"{URL_START}/Destiny/Stats/UniqueWeapons/{membershipType}/{membershipId}/{characterId}"
        message = f"Fetching weapon usage stats for: {displayName}"
        outFile =f"{displayName}_weapons.json"
        data = jsonRequest(stat_url, outFile, message)
        if data is None:
            #TODO: Throw an error
            print("")
        elif data['Response']['data'] == {}:
            continue

        #This part does the heavy lifting of table building
        weapons = data['Response']['data']['weapons']
        for weapon in weapons:
            weaponDict = {}
            weaponDict['last_updated'] = datetime.now()
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

def handleReferenceTables(session):
    """Connects to the manifest.content database and builds the necessary reference tables."""
    
    con = sqlite3.connect(os.environ['MANIFEST_CONTENT'])
    cur = con.cursor()

    #First, characters
    print("Building class reference table...")
    cur.execute('SELECT * FROM DestinyClassDefinition')
    classes = cur.fetchall()
    for classdef in classes:
        classinfo = json.loads(classdef[1])
        classDict = {}
        classDict['id'] = classinfo['classHash']
        classDict['class_name'] = classinfo['className']
        new_class_def = ClassReference(**classDict)
        insertOrUpdate(ClassReference, new_class_def, session)
    
    #Next, weapons
    print("Building weapon reference table...")
    cur.execute("SELECT * FROM DestinyInventoryItemDefinition")
    #Can easily be adjusted to pull info for all items (don't filter on weapon types)
    weapon_types = ['Rocket Launcher', 'Scout Rifle', 'Fusion Rifle', 'Sniper Rifle', 'Shotgun', 'Machine Gun', 'Pulse Rifle', 'Auto Rifle', 'Hand Cannon', 'Sidearm']
    weapons = cur.fetchall()
    for weapon in weapons:
        weaponinfo = json.loads(weapon[1])
        weaponDict = {}
        if not ("itemTypeName" in weaponinfo and weaponinfo['itemTypeName'] in weapon_types):
            continue
        weaponDict['id'] = weaponinfo['itemHash']
        weaponDict['weapon_name'] = weaponinfo['itemName']
        weaponDict['weapon_type'] = weaponinfo['itemTypeName']
        weaponDict['weapon_rarity'] = weaponinfo['tierTypeName']
        new_weapon_def = WeaponReference(**weaponDict)
        insertOrUpdate(WeaponReference, new_weapon_def, session)
    
    #Finally, activities
    print("Building activity reference table...")
    cur.execute("SELECT * FROM DestinyActivityDefinition")
    activities = cur.fetchall()
    for activity in activities:
        activityinfo = json.loads(activity[1])
        activityDict = {}
        if not ("activityName" in activityinfo):
            continue
        activityDict['id'] = activityinfo['activityHash']
        activityDict['activity_name'] = activityinfo['activityName']
        activityDict['activity_type_hash'] = activityinfo['activityTypeHash']
        new_activity_def = ActivityReference(**activityDict)
        insertOrUpdate(ActivityReference, new_activity_def, session)

    #Actually finallly, activity types
    print("Building activity type reference table...")
    cur.execute("SELECT * FROM DestinyActivityTypeDefinition")
    activities = cur.fetchall()
    for activity in activities:
        activityinfo = json.loads(activity[1])
        activityDict = {}
        if not ("activityTypeName" in activityinfo):
            continue
        activityDict['id'] = activityinfo['activityTypeHash']
        activityDict['activity_type_name'] = activityinfo['activityTypeName']
        new_activity_def = ActivityTypeReference(**activityDict)
        insertOrUpdate(ActivityTypeReference, new_activity_def, session)

def jsonRequest(url, outFile, message=""):
    print(f"Connecting to Bungie: {url}")
    print(message)
    res = requests.get(url, headers=makeHeader())
    data = res.json()
    error_stat = data['ErrorStatus']
    if error_stat == "Success":
    #    with open(outFile,"w+") as f:
    #        json.dump(data, f)
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
    #import time
    #start_time = time.time()
    buildDB()
    #print("--- %s seconds ---" % (time.time() - start_time))
