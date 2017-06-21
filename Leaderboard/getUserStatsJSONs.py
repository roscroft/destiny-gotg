#!/usr/bin/python

import json
import requests
import sqlite3 as lite
import sys
from getHeader import getHeader

#Only grabs PS4 records
def getUsersFromDestinyTable():
    con = lite.connect('guardians.db')
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
    statsres = requests.get(stats_url, headers=getHeader())
    statsdata = statsres.json()
    filename = "./Stats/"+dispName+".json" 
    with open(filename,'w') as f:
        json.dump(statsdata, f)

def getUserStatsJSONs():
    getUsersFromDestinyTable()

if __name__ == "__main__":
    getUserStatsJSONs()
