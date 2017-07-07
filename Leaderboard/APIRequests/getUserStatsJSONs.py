#!/usr/bin/python
#Only grabs PS4 records
import json
import requests
import sys
sys.path.append('../')
sys.path.append('../../')
from DatabaseModules import databaseStatements as db
import APIRequests.jsonRequester as jr
import timeit

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
        jr.singleJSONRequest(stats_url, header, dumpFileName, message)
    
    getUsersFromDestinyTable()

if __name__ == "__main__":
    path = '../Stats/'
    #getUserStatsJSONs()
