#!/usr/bin/python
#Only grabs PS4 records

import json
import requests
import sqlite3 as lite
import sys

def getUsersStatsJSONs(path, databasePath, header):
    def getUsersFromDestinyTable():
        con = lite.connect(databasePath)
        with con:
            cur = con.cursor()
            cur.execute("SELECT Destiny.Type, Destiny.Id, Bungie.Name FROM Destiny INNER JOIN Bungie ON Destiny.Id = Bungie.Id;")
            while True:
                row = cur.fetchone()
                if row == None:
                    break
                else:
                    retrieveUserStatsJSON(row[0], row[1], row[2])

    def retrieveUserStatsJSON(memType, memId, dispName):
        stats_url = "https://bungie.net/platform/Destiny/Stats/Account/"+str(memType)+"/"+str(memId)
        print "Connecting to Bungie: " + stats_url
        print "Fetching aggregate historical stats for " + dispName
        statsres = requests.get(stats_url, header)
        statsdata = statsres.json()
        filename = path+dispName+".json" 
        with open(filename,'w') as f:
            json.dump(statsdata, f)

if __name__ == "__main__":
    path = '../Stats/'
    #getUserStatsJSONs()
