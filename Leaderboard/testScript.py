#!/usr/bin/python
import json
import requests
import sys
sys.path.append('../')
sys.path.append('../../')
import DatabaseModules.databaseStatements as db
import apiRequests as ar
import Tokens.getHeader as gh

#Path to header file
headerPath = './Tokens/header.txt'

#Header
header = gh.getHeader(headerPath)

def getUser():
    request = "SELECT * FROM Bungie"
    users = db.select(request)
    for user in users:
        if user[1] == "MAPD":
            getJSON(user[0], user[1])

def getJSON(bungieID, displayName):
    #url = "https://www.bungie.net/Platform/User/GetMembershipsById/"+str(bungieID)+"/2/"
    #url = "https://www.bungie.net/Platform/Destiny/2/Account/"+str(bungieID)+"/Summary/"
    #url = "https://www.bungie.net/Platform/User/GetBungieAccount/"+str(bungieID)+"/2/"
    #url = "https://www.bungie.net/Platform/Destiny/2/Account/"+str(bungieID)+"/Character/2305843009379090568/"
    #url = "https://www.bungie.net/Platform/Destiny/Stats/AggregateActivityStats/2/"+str(bungieID)+"/2305843009379090568/"
    #url = "https://www.bungie.net/Platform/Destiny/Stats/AggregateActivityStats/2/"+str(bungieID)+"/2305843009265556749/"
    #url = "https://www.bungie.net/Platform/Destiny/Stats/ActivityHistory/2/"+str(bungieID)+"/2305843009379090568/?mode=MayhemClash"
    url = "https://www.bungie.net/Platform/Destiny/Stats/ActivityHistory/2/"+str(bungieID)+"/2305843009265556749/?mode=MayhemClash"

    dumpFileName = 'outFile.json'
    ar.singleJSONRequest(url, header, dumpFileName)

if __name__ == "__main__":
    path = './Users/'
    getUser()





