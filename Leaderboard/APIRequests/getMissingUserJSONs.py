#!/usr/bin/python
import json
import requests
import sys
sys.path.append('../')
sys.path.append('../../')
import DatabaseModules.databaseStatements as db
import Tokens.getHeader as h
import APIRequests.jsonRequester as jr

def getMissingUserJSONs(path, header):
    def getMissingUsers():
        request = "SELECT Bungie.Id, Bungie.Name FROM Bungie LEFT JOIN Destiny ON Bungie.Id = Destiny.Id WHERE Destiny.Id IS NULL"
        users = db.select(request)
        print users
        return users

    def retrieveDestinyUserJSON(bungieID, displayName):
        user_url = "https://bungie.net/platform/User/GetBungieAccount/"+str(bungieID)+"/254/"
        dumpFileName = path+displayName+'.json'
        obj = displayName
        jr.singleJSONRequest(user_url, header, dumpFileName, obj)
    
    missing = getMissingUsers()
    if missing == []:
        return False, []
    else:
        updatedUsers = []
        for missed in missing:
            bid, name = missed
            exitCode = retrieveDestinyUserJSON(bid, name)
            if exitCode:
                updatedUsers += missed
        return True, updatedUsers

if __name__ == "__main__":
    path = "../Users/"
    header = h.getHeader("../Tokens/header.txt")
    getMissingUserJSONs(path, header)
