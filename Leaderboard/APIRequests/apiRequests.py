#!/usr/bin/python
import json
import requests
import sys
sys.path.append('../')
sys.path.append('../../')
import DatabaseModules.databaseStatements as db
import Tokens.getHeader as h
import Tokens.getClanId as c

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

def getClanUserJSONs(path, header, clanId):
    def retrieveClanUserJSON():
        morePages = True
        pageCounter = 1
        while morePages:
            clan_url = "https://bungie.net/Platform/Group/"+clanId+"/Membersv3/?lc=en&fmt=true&currentPage="+str(pageCounter)+"&platformType=2"
            print "Connecting to Bungie: " + clan_url
            print "Fetching page " + str(pageCounter) + " of users."
            res = requests.get(clan_url, headers=header)
            data = res.json()
            error_stat = data['ErrorStatus']
            print "Error Stats: " + error_stat
            #Stores each page of clan user responses as a different .json
            with open(path+'clanUsersPage'+str(pageCounter)+'.json','w') as f:
                json.dump(data,f)
            hasMore = res.json()['Response']['hasMore']
            morePages = hasMore
            pageCounter+=1
    
    retrieveClanUserJSON()

def getMissingUserJSONs(path, header):
    def getMissingUsers():
        request = "SELECT Bungie.Id, Bungie.Name FROM Bungie LEFT JOIN Destiny ON Bungie.Id = Destiny.Id WHERE Destiny.Id IS NULL"
        users = db.select(request)
        print "Missing users: ",users
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
    print "Connecting to Bungie: " + url
    print message
    pageCounter = 1
    hasMore = True
    exitCodes = []
    while hasMore:
        #print "Fetching page " + str(pageCounter)
        res = requests.get(url, headers=header)
        data = res.json()
        error_stat = data['ErrorStatus']
        print "Error Status: " + error_stat
        if error_stat != "Success":
            print "Error fetching data"
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
