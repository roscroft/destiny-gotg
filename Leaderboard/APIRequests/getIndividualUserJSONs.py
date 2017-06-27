#!/usr/bin/python
import json
import requests
import sys
sys.path.append('../')
sys.path.append('../../')
import DatabaseModules.databaseStatements as db

def getIndividualUserJSONs(path, databasePath, header):
    def getUsersFromBungieTable():
        request = "SELECT * FROM Bungie"
        users = db.select(request)
        for user in users:
            retrieveDestinyUserJSON(user[0], user[1])

    def retrieveDestinyUserJSON(bungieID, displayName):
        user_url = "https://bungie.net/platform/User/GetBungieAccount/"+str(bungieID)+"/254/"
        print "Connecting to Bungie: " + user_url
        print "Fetching user data for " + displayName
        userRequest = requests.get(user_url, header)
        userData = userRequest.json()
        error_stat = userData['ErrorStatus']
        if error_stat != "Success":
            print "Can't fetch user data for " + displayName
            print "Error Status: " + error_stat
        else:
            with open(path+displayName+'.json','w') as f:
                json.dump(userData, f)
    
    getUsersFromBungieTable()

if __name__ == "__main__":
    path = '../Users/'
    #getIndividualUserJSONs()
