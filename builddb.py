#!/usr/bin/python
import os
import json
import requests
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from initdb import Base, Bungie, Account

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
        membershipType = 254
        bungieId = result['user']['membershipId']
        #Some people have improperly linked accounts, this will handle those by setting bungieId
        #To be their PSN id
        if bungieId == '0':
            bungieId = result['membershipId']
            membershipType = result['membershipType']
        bungieName = str(result['user']['displayName'])
        new_bungie_user = Bungie(id=bungieId, bungie_name=bungieName, membership_type=membershipType)
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
        
        #Grab all of the individual accounts and put them in the Account table
        accounts = data['Response']['destinyMemberships']
        for account in accounts:
            membershipId = str(account['membershipId'])
            membershipType = str(account['membershipType'])
            displayName = str(account['displayName'])
            new_account = Account(id = membershipId, display_name=displayName, membership_type=membershipType, bungie_id=bungieId)
            session.add(new_account)
            session.commit()

def getMissingUserJSONs(path, header):
    def getMissingUsers():
        request = "SELECT Bungie.Id, Bungie.Name FROM Bungie LEFT JOIN Destiny ON Bungie.Id = Destiny.Id WHERE Destiny.Id IS NULL"
        users = db.select(request)
        print("Missing users: ",users)
        return users

    def retrieveDestinyUserJSON(bungieID, displayName):
        user_url = "https://bungie.net/platform/User/GetBungieAccount/"+str(bungieID)+"/254/"
        dumpFileName = path+displayName+'.json'
        obj = displayName
        singleJSONRequest(user_url, header, dumpFileName, obj)
        return obj

    missing = getMissingUsers()
    if missing == []:
        return False, []
    else:
        updatedUsers = []
        for missed in missing:
            bid, name = missed
            missedName = retrieveDestinyUserJSON(bid, name)
            updatedUsers.append(missedName)
        return True, updatedUsers

def buildCharactersTable(path, databasePath):
    def parseUserJSON():
        players = set()
        characterIds = []
        for filename in os.listdir(path):
            if filename.endswith(".json"):
                with open(path+filename) as data_file:
                    data = json.load(data_file)
                    characters = data['Response']['destinyAccounts']
                    for character in characters:
                        characterId = str(character['userInfo']['characterId'])
                        players.add((membershipId, membershipType))
                    # Should grab all character Ids. Seems like I don't actually grab anything, and not used currently, so commented out
                    #characters = data['Response']['destinyAccounts'][0]
                    #for character in characters:
                    #    characterIds.append(['characterId'])
        return tuple(players)

    def addToDatabase(players):
        table = "Destiny"
        fields = "(Id INT, Type INT)"
        db.initializeTable(table, fields)
        for player in players:
            request = "INSERT INTO Destiny VALUES(?,?)"
            db.insert(request,player)

    players = parseUserJSON()
    addToDatabase(players)

def buildStatTables(path, databasePath):
    
    def initializeTables():
        pvpTotal = "PvPTotal"
        pvpPGA = "PvPPGA"
        pveTotal = "PvETotal"
        pvePGA = "PvEPGA"

        pvefields = "(Name TEXT, abilityKills REAL, activitiesCleared REAL, activitiesEntered REAL, allParticipantsCount REAL, allParticipantsTimePlayed REAL, assists REAL, averageDeathDistance REAL, averageKillDistance REAL, averageLifespan REAL, bestSingleGameKills REAL, courtOfOryxAttempts REAL, courtOfOryxCompletions REAL, courtOfOryxWinsTier1 REAL, courtOfOryxWinsTier2 REAL, courtOfOryxWinsTier3 REAL, deaths REAL, fastestCompletion REAL, highestCharacterLevel REAL, highestLightLevel REAL, kills REAL, killsDeathAssists REAL, killsDeathsRatio REAL, longestKillDistance REAL, longestKillSpree REAL, longestSingleLife REAL, mostPrecisionKills REAL, objectivesCompleted REAL, orbsDropped REAL, orbsGathered REAL, precisionKills REAL, publicEventsCompleted REAL, publicEventsJoined REAL, remainingTimeAfterQuitSeconds REAL, resurrectionsPerformed REAL, resurrectionsReceived REAL, secondsPlayed REAL, suicides REAL, totalActivityDurationSeconds REAL, totalDeathDistance REAL, totalKillDistance REAL, weaponBestType TEXT, weaponKillsAutoRifle REAL, weaponKillsFusionRifle REAL, weaponKillsGrenade REAL, weaponKillsHandCannon REAL, weaponKillsMachinegun REAL, weaponKillsMelee REAL, weaponKillsPulseRifle REAL, weaponKillsRelic REAL, weaponKillsRocketLauncher REAL, weaponKillsScoutRifle REAL, weaponKillsShotgun REAL, weaponKillsSideArm REAL, weaponKillsSniper REAL, weaponKillsSubmachinegun REAL, weaponKillsSuper REAL, weaponKillsSword REAL)"
        
        pvpfields = "(Name TEXT, abilityKills REAL, activitiesEntered REAL, activitiesWon REAL, allParticipantsCount REAL, allParticipantsScore REAL, allParticipantsTimePlayed REAL, assists REAL, averageDeathDistance REAL, averageKillDistance REAL, averageLifespan REAL, averageScorePerKill REAL, averageScorePerLife REAL, bestSingleGameKills REAL, bestSingleGameScore REAL, closeCalls REAL, combatRating REAL, deaths REAL, defensiveKills REAL, dominationKills REAL, highestCharacterLevel REAL, highestLightLevel REAL, kills REAL, killsDeathAssists REAL, killsDeathsRatio REAL, longestKillDistance REAL, longestKillSpree REAL, longestSingleLife REAL, mostPrecisionKills REAL, objectivesCompleted REAL, offensiveKills REAL, orbsDropped REAL, orbsGathered REAL, precisionKills REAL, relicsCaptured REAL, remainingTimeAfterQuitSeconds REAL, resurrectionsPerformed REAL, resurrectionsReceived REAL, score REAL, secondsPlayed REAL, suicides REAL, teamScore REAL, totalActivityDurationSeconds REAL, totalDeathDistance REAL, totalKillDistance REAL, weaponBestType TEXT, weaponKillsAutoRifle REAL, weaponKillsFusionRifle REAL, weaponKillsGrenade REAL, weaponKillsHandCannon REAL, weaponKillsMachinegun REAL, weaponKillsMelee REAL, weaponKillsPulseRifle REAL, weaponKillsRelic REAL, weaponKillsRocketLauncher REAL, weaponKillsScoutRifle REAL, weaponKillsShotgun REAL, weaponKillsSideArm REAL, weaponKillsSniper REAL, weaponKillsSubmachinegun REAL, weaponKillsSuper REAL, weaponKillsSword REAL, winLossRatio REAL, zonesCaptured REAL, zonesNeutralized REAL)"

        db.initializeTable(pveTotal, pvefields)
        db.initializeTable(pvePGA, pvefields)
        db.initializeTable(pvpTotal, pvpfields)
        db.initializeTable(pvpPGA, pvpfields)

    def parseStatsJSON(versus):
        totalTable = versus + "Total"
        pgaTable = versus + "PGA"
        for filename in os.listdir(path):
            if filename.endswith(".json"):
                with open(path+filename) as data_file:
                    data = json.load(data_file)
                    dispName = filename[:-5]
                    totalStatTuple = parseData(data,'basic', dispName, versus)
                    pgaStatTuple = parseData(data, 'pga', dispName, versus)
                    addToDatabase(totalStatTuple, totalTable, versus)
                    addToDatabase(pgaStatTuple, pgaTable, versus)

    def parseData(data, mode, dispName, versus):
        allVersus = "all"+versus
        path = data['Response']['mergedAllCharacters']['results'][allVersus]['allTime']
        stats = []
        for stat in path:
            if mode not in path[stat]:
                stats.append((stat, None))
            else:
                stats.append((stat, path[stat][mode]['value']))
        #Sorts on first item (alphabetical list of stats)
        stats.sort(key=lambda x: x[0])
        values = [x[1] for x in stats]
        return (dispName,)+tuple(values)

    def addToDatabase(stats, table, versus):
        if versus == "PvP":
            request = "INSERT INTO "+table+" VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        elif versus == "PvE":
            request = "INSERT INTO "+table+" VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        db.insert(request, stats)

    initializeTables()
    pvp = "PvP"
    pve = "PvE"
    parseStatsJSON(pvp)
    parseStatsJSON(pve)

def updateDestinyTable(path, filename, databasePath):
    def parseUserJSON():
        players = set()
        with open(path+filename+'.json') as data_file:
            data = json.load(data_file)
            characters = data['Response']['destinyAccounts']
            for character in characters:
                membershipId = str(character['userInfo']['membershipId'])
                membershipType = str(character['userInfo']['membershipType'])
                players.add((membershipId, membershipType))
                    # Should grab all character Ids. Seems like I don't actually grab anything, and not used currently, so commented out
                    #characters = data['Response']['destinyAccounts'][0]
                    #for character in characters:
                    #    characterIds.append(['characterId'])
        return tuple(players)

    def addToDatabase(players):
        for player in players:
            request = "INSERT INTO Destiny VALUES(?,?)"
            db.insert(request,player)

    players = parseUserJSON()
    addToDatabase(players)

def jsonRequest(url, outFile, message=""):
    print(f"Connecting to Bungie: {url}")
    print(message)
    res = requests.get(url, headers=makeHeader())
    data = res.json()
    error_stat = data['ErrorStatus']
    print("Error Status: " + error_stat)
    if error_stat == "Success":
    #    with open(outFile,"w+") as f:
    #        json.dump(data, f)
        return data
    else:
        return None

if __name__ == "__main__":
    loadConfig()
    buildDB()
