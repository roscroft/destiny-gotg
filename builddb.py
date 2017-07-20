#!/usr/bin/python
#This file (with update option set) is run daily; it pulls new clan members and new accounts. For existing members, it adds newly created characters, and updates all existing stats.
#Perhaps most importantly, it pulls in new activities completed by all members.
import os
import json
import requests
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from initdb import Base, Bungie, Account, PvPTotal, PvPAverage, PvETotal, PvEAverage, Character, CharacterUsesWeapon, AggregateStatsCharacter, ActivityReference, ClassReference, WeaponReference

#load env vars for testing purposes
APP_PATH = "/etc/destinygotg"
URL_START = "https://bungie.net/Platform"

def loadConfig(): 
    """Load configs from the config file""" 
    config = open(f"{APP_PATH}/config", "r").readlines() 
    for value in config: 
        value = value.strip().split(":") 
        os.environ[value[0]] = value[1]

def makeHeader():
    return {'X-API-KEY':os.environ['BUNGIE_APIKEY']}

def buildDB():
    """Main function to build the full database"""
    engine = create_engine(f"sqlite:///{os.environ['DBPATH']}")
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    handleBungieUsers(session)
    handleDestinyUsers(session)
    handleAggregateStats(session)
    handleCharacters(session)
    handleAggregateActivities(session)
    handleWeaponUsage(session)

def handleBungieUsers(session):
    """Retrieve JSON containing all clan users, and build the Bungie table from the JSON"""
    clan_url = f"{URL_START}/Group/{os.environ['BUNGIE_CLANID']}/Membersv3/?lc=en&fmt=true&currentPage=1&platformType=2"
    outFile = "clanUser_p1.json"
    message = "Fetching page 1 of clan users."
    data = jsonRequest(clan_url, outFile, message)
    if data is None:
        #TODO: Throw some error or something
        print("We fucked up")
    
    #This section stores all clan users in the Bungie table 
    for result in data['Response']['results']:
        bungieDict = {}
        bungieDict['membership_type']=254
        bungieDict['id'] = result['user']['membershipId']
        #Some people have improperly linked accounts, this will handle those by setting bungieId as their PSN id
        if bungieDict['id'] == '0':
            bungieDict['id'] = result['membershipId']
            bungieDict['membership_type'] = result['membershipType']
        bungieDict['bungie_name'] = result['user']['displayName']
        new_bungie_user = Bungie(**bungieDict)
        session.add(new_bungie_user)
        session.commit()

def handleDestinyUsers(session):
    """Retrieve JSONs for users, listing their Destiny accounts. Builds account table."""
    users = session.query(Bungie).all()
    for user in users:
        bungieId = user.id
        bungieName = user.bungie_name
        membershipType = user.membership_type
        user_url = f"{URL_START}/User/GetMembershipsById/{bungieId}/{membershipType}/"
        message = f"Fetching membership data for: {bungieName}"
        outFile = f"{bungieName}.json"
        data = jsonRequest(user_url, outFile, message)
        if data is None:
            #TODO: Throw an error
            print("We fucked up")
            continue

        #Grab all of the individual accounts and put them in the Account table
        accounts = data['Response']['destinyMemberships']
        for account in accounts:
            accountDict = {}
            accountDict['id'] = account['membershipId']
            accountDict['membership_type'] = account['membershipType']
            accountDict['display_name'] = account['displayName']
            accountDict['bungie_id'] = bungieId
            new_account = Account(**accountDict)
            session.add(new_account)
            session.commit()

def handleAggregateStats(session):
    """Retrieve aggregate stats for users. Builds PvP and PvE average and total tables."""
    accounts = session.query(Account).all()
    for account in accounts:
        membershipType = account.membership_type
        membershipId = account.id
        displayName = account.display_name
        stat_url = f"{URL_START}/Destiny/Stats/Account/{membershipType}/{membershipId}"
        message = f"Fetching aggregate historical stats for: {displayName}"
        outFile =f"{displayName}_stats.json"
        data = jsonRequest(stat_url, outFile, message)
        if data is None:
            #TODO: Throw an error
            print("Not good hombre")
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
        pvpTotalDict['membership_id'] = membershipId
        pvpAvgDict['membership_id'] = membershipId
        pveTotalDict['membership_id'] = membershipId
        pveAvgDict['membership_id'] = membershipId
        #And put these in the database. Double **s unpack a dictionary into the row.
        new_pvp_total = PvPTotal(**pvpTotalDict)
        new_pvp_avg = PvPAverage(**pvpAvgDict)
        new_pve_total = PvETotal(**pveTotalDict)
        new_pve_avg = PvEAverage(**pveAvgDict)
        session.add(new_pvp_total)
        session.add(new_pvp_avg)
        session.add(new_pve_total)
        session.add(new_pve_avg)
        session.commit()

def handleCharacters(session):
    """Retrieve JSONs for accounts, listing their Destiny characters. Builds characters table."""
    accounts = session.query(Account).all()
    for account in accounts:
        membershipId = account.id
        displayName = account.display_name
        membershipType = account.membership_type
        account_url = f"{URL_START}/Destiny/{membershipType}/Account/{membershipId}"
        message = f"Fetching character data for: {displayName}"
        outFile = f"{displayName}_characters.json"
        data = jsonRequest(account_url, outFile, message)
        if data is None:
            #TODO: Throw an error
            print("We fucked up")
            continue

        #Grab all of the individual accounts and put them in the Account table
        characters = data['Response']['data']['characters']
        for character in characters:
            characterDict = {}
            characterDict['id'] = character['characterBase']['characterId']
            characterDict['minutes_played'] = character['characterBase']['minutesPlayedTotal']
            characterDict['light_level'] = character['characterBase']['powerLevel']
            characterDict['membership_id'] = membershipId
            characterDict['class_hash'] = character['characterBase']['classHash']
            new_character = Character(**characterDict)
            session.add(new_character)
            session.commit()
#TODO: Next 2 functions are basically identical (and can be written identically). Abstract out.
def handleAggregateActivities(session):
    """Retrieve aggregate activity stats for users. Builds aggregateStatsCharacter table."""
    characters = session.query(Character).all()
    for character in characters:
        membershipId = character.membership_id
        characterId = character.id
        displayName = session.query(Account).filter_by(id=membershipId).first().display_name
        membershipType = session.query(Account).filter_by(id=membershipId).first().membership_type
        stat_url = f"{URL_START}/Destiny/Stats/AggregateActivityStats/{membershipType}/{membershipId}/{characterId}"
        message = f"Fetching aggregate activity stats for: {displayName}"
        outFile =f"{displayName}_activities.json"
        data = jsonRequest(stat_url, outFile, message)
        if data is None:
            #TODO: Throw an error
            print("Not good hombre")
        
        #This part does the heavy lifting of table building
        aggStatDict = {}
        aggStatDict['character_id'] = characterId
        activities = data['Response']['data']['activities']
        for activity in activities:
            aggStatDict['activity_hash'] = activity['activityHash']
            for value in activity['values']:
                aggStatDict[value] = activity['values'][value]['basic']['value']
        new_aggregate_statistics = AggregateStatsCharacter(**aggStatDict)
        session.add(new_aggregate_statistics)
        session.commit()

def handleWeaponUsage(session):
    """Retrieve weapon usage for characters. Builds characterUsesWeapon table."""
    characters = session.query(Character).all()
    for character in characters:
        membershipId = character.membership_id
        characterId = character.id
        displayName = session.query(Account).filter_by(id=membershipId).first().display_name
        membershipType = session.query(Account).filter_by(id=membershipId).first().membership_type
        stat_url = f"{URL_START}/Destiny/Stats/UniqueWeapons/{membershipType}/{membershipId}/{characterId}"
        message = f"Fetching weapon usage stats for: {displayName}"
        outFile =f"{displayName}_weapons.json"
        data = jsonRequest(stat_url, outFile, message)
        if data is None:
            #TODO: Throw an error
            print("Not good hombre")
        elif data['Response']['data'] == {}:
            continue

        #This part does the heavy lifting of table building
        weaponDict = {}
        weaponDict['character_id'] = characterId
        weapons = data['Response']['data']['weapons']
        for weapon in weapons:
            weaponDict['weapon_hash'] = weapon['referenceId']
            weaponValues = weapon['values']
            weaponDict['kills'] = weaponValues['uniqueWeaponKills']['basic']['value']
            weaponDict['precision_kills'] = weaponValues['uniqueWeaponPrecisionKills']['basic']['value']
            weaponDict['precision_kill_percentage'] = weaponValues['uniqueWeaponKillsPrecisionKills']['basic']['value']
        new_weapon_stats = CharacterUsesWeapon(**weaponDict)
        session.add(new_weapon_stats)
        session.commit()

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

if __name__ == "__main__":
    loadConfig()
    buildDB()
