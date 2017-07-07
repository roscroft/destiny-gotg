#!/usr/bin/python
import json
import requests
import sys
sys.path.append('../')
sys.path.append('../../')
import DatabaseModules.databaseStatements as db
import APIRequests.jsonRequester as jr

def getIndividualUserJSONs(path, databasePath, header):
    def getUsersFromBungieTable():
        request = "SELECT * FROM Bungie"
        users = db.select(request)
        for user in users:
            retrieveDestinyUserJSON(user[0], user[1])

    def retrieveDestinyUserJSON(bungieID, displayName):
        user_url = "https://bungie.net/platform/User/GetBungieAccount/"+str(bungieID)+"/254/"
        message = "Fetching user data for: "+displayName
        dumpFileName = path+displayName+'.json'
        jr.singleJSONRequest(user_url, header, dumpFileName, message)
    
    getUsersFromBungieTable()

if __name__ == "__main__":
    path = '../Users/'
    #getIndividualUserJSONs()
