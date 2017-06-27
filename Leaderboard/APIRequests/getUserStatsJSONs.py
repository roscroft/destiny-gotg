#!/usr/bin/python
#Only grabs PS4 records
import json
import requests
import sys
sys.path.append('../')
sys.path.append('../../')
from DatabaseModules import databaseStatements as db

def getUserStatsJSONs(path, databasePath, header):
    def getUsersFromDestinyTable():
        request = "SELECT Destiny.Type, Destiny.Id, Bungie.Name FROM Destiny INNER JOIN Bungie ON Destiny.Id = Bungie.Id"
        users = db.select(request)
        for user in users:
            retrieveUserStatsJSON(user[0], user[1], user[2])

    def retrieveUserStatsJSON(memType, memId, dispName):
        stats_url = "https://bungie.net/platform/Destiny/Stats/Account/"+str(memType)+"/"+str(memId)
        print "Connecting to Bungie: " + stats_url
        print "Fetching aggregate historical stats for " + dispName
        statsres = requests.get(stats_url, header)
        statsdata = statsres.json()
        filename = path+dispName+".json" 
        with open(filename,'w') as f:
            json.dump(statsdata, f)
    
    getUsersFromDestinyTable()

if __name__ == "__main__":
    path = '../Stats/'
    #getUserStatsJSONs()
