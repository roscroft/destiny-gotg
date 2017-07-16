#!/usr/bin/python
import os
import json
import requests
import sys

def buildDB():
    """Main function to build the full database"""
    getClanUserJSONs()

def getClanUserJSONs():
    """Gather a list of the clan members through the Bungie API"""
    pageCount = 1
    while pageCount:
        clan_url = f"https://bungie.net/Platform/Group/{os.environ['BUNGIE_CLANID']}/Membersv3/?lc=en&fmt=true&currentPage={pageCount}&platformType=2"
        #print("Connecting to Bungie: " + clan_url)
        #print("Fetching page " + str(pageCounter) + " of users.")
        res = requests.get(clan_url, headers={"X-API-KEY":os.environ['BUNGIE_APIKEY']})
        data = res.json()
        err = data['ErrorStatus']
        if not err.lower() == "success":
            print(f"Error Stats: {err}")
        #Stores each page of clan user responses as a different .json
        f = open(f"clanUser_p{pageCount}.json", "w+")
        json.dump(data,f)
        f.close()
        if res.json()['Response']['hasMore']:
            pageCount += 1
        else:
            pageCount = 0

def getIndividualUserJSONs(path, databasePath, header):
    def getUsersFromBungieTable():
        request = "SELECT * FROM Bungie"
        users = db.select(request)
        for user in users:
            retrieveDestinyUserJSON(user[0], user[1])

    def retrieveDestinyUserJSON(bungieID, displayName):
        user_url = "https://www.bungie.net/Platform/User/GetMembershipsById/"+str(bungieID)+"/2/"
        message = "Fetching membership data for: "+displayName
        dumpFileName = path+displayName+'.json'
        singleJSONRequest(user_url, header, dumpFileName, message)
    
    getUsersFromBungieTable()

def getUserStatsJSONs(path, databasePath, header):
    def getUsersFromDestinyTable():
        request = "SELECT Destiny.Type, Destiny.Id, Bungie.Name FROM Destiny INNER JOIN Bungie ON Destiny.Id = Bungie.Id"
        users = db.select(request)
        for user in users:
            retrieveUserStatsJSON(user[0], user[1], user[2])

    def retrieveUserStatsJSON(memType, memId, dispName):
        stats_url = "https://bungie.net/platform/Destiny/Stats/Account/"+str(memType)+"/"+str(memId)
        message = "Fetching aggregate historical stats for: " + dispName
        dumpFileName = path+dispName+".json"
        singleJSONRequest(stats_url, header, dumpFileName, message)
    
    getUsersFromDestinyTable()

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

def singleJSONRequest(url, header, dumpFileName, message=""):
    return jSONRequest(url, header, dumpFileName, message)

def multiJSONRequest(url, header, dumpFileName, message=""):
    return jSONRequest(url, header, dumpFileName, message, True)

def jSONRequest(url, header, dumpFileName, message, multi=False):
    print("Connecting to Bungie: " + url)
    print(message)
    pageCounter = 1
    hasMore = True
    exitCodes = []
    while hasMore:
        #print("Fetching page " + str(pageCounter))
        res = requests.get(url, headers=header)
        data = res.json()
        error_stat = data['ErrorStatus']
        print("Error Status: " + error_stat)
        if error_stat != "Success":
            print("Error fetching data")
            with open("errorExample.json",'w') as f:
                json.dump(data,f)
            exitCodes.append(0)
        else:
            with open(dumpFileName,'w') as f:
                json.dump(data, f)
            exitCodes.append(1)
        if multi:
            hasMore = res.json()['Response']['hasMore']
            morePages = hasMore
            pageCounter+=1
        else:
            hasMore = False
    if len(exitCodes) == 1:
        return exitCodes[0]
    return exitCodes

def buildBungieTable(path, databasePath):
    def parseClanUserJSON():
        players = []
        for filename in os.listdir(path):
            if filename.endswith(".json"):
                with open(path+filename) as data_file:
                    data = json.load(data_file)
                    for result in data['Response']['results']:
                        name = str(result['user']['displayName'])
                        players.append((result['membershipId'],name))
        return tuple(players)

    def addToDatabase(players):
        table = "Bungie"
        fields = "(Id INT, Name TEXT)"
        db.initializeTable(table, fields)
        for player in players:
            request = "INSERT INTO Bungie VALUES(?,?)"
            db.insert(request, player)

    players = parseClanUserJSON()
    addToDatabase(players)

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

def buildDestinyTable(path, databasePath):
    def parseUserJSON():
        players = set()
        characters = []
        for filename in os.listdir(path):
            if filename.endswith(".json"):
                with open(path+filename) as data_file:
                    data = json.load(data_file)
                    accounts = data['Response']['destinyMemberships']
                    for account in accounts:
                        membershipId = str(account['membershipId'])
                        membershipType = str(account['membershipType'])
                        players.add((membershipId, membershipType))
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

