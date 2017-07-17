#!/usr/bin/python
import os
import json
import requests
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from initdb import Base, Bungie, Account, PvPAccountStatsTotal, PvPAccountStatsAverage, PvEAccountStatsTotal, PvEAccountStatsAverage

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
        new_pvp_total = PvPAccountStatsTotal(**pvpTotalDict)
        new_pvp_avg = PvPAccountStatsAverage(**pvpAvgDict)
        new_pve_total = PvEAccountStatsTotal(**pveTotalDict)
        new_pve_avg = PvEAccountStatsAverage(**pveAvgDict)
        session.add(new_pvp_total)
        session.add(new_pvp_avg)
        session.add(new_pve_total)
        session.add(new_pve_avg)
        session.commit()

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
