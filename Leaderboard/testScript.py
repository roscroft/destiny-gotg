#!/usr/bin/python
import json
import requests
import sys
sys.path.append('../')
sys.path.append('../../')
import DatabaseModules.databaseStatements as db
import APIRequests.jsonRequester as jr
import Tokens.getHeader as gh

#Path to header file
headerPath = './Tokens/header.txt'

#Header
header = gh.getHeader(headerPath)

def getUser():
    request = "SELECT * FROM Bungie"
    users = db.select(request)
    for user in users:
        if user[1] == "LutherArkwright":
            getJSON(user[0], user[1])

def getJSON(bungieID, displayName):
    url = "https://www.bungie.net/Platform/User/GetMembershipsById/"+str(bungieID)+"/2/"
    dumpFileName = 'RoscroftWorkFile.json'
    jr.singleJSONRequest(url, header, dumpFileName)

if __name__ == "__main__":
    path = './Users/'
    getUser()





