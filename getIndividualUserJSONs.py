#!/usr/bin/python

import json
import requests
import sqlite3 as lite
import sys

def getHeader():
    with open('header.txt','r') as f:
        header = f.readline().strip()
    return {"X-API-KEY":header}

def getUsersFromBungieTable():
    con = lite.connect('guardians.db')
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Bungie;")
        while True:
            row = cur.fetchone()
            if row == None:
                print "We found a none row..."
                break
            else:
                print row[0], row[1]
                retrieveDestinyUserJSON(row[0],row[1])

def retrieveDestinyUserJSON(bungieID, displayName):
    user_url = "https://bungie.net/platform/User/GetBungieAccount/"+str(bungieID)+"/254/"
    print "Connecting to Bungie: " + user_url
    print "Fetching user data for " + displayName
    userRequest = requests.get(user_url, headers=getHeader())
    userData = userRequest.json()
    error_stat = userData['ErrorStatus']
    if error_stat != "Success":
        print "Can't fetch user data for " + displayName
        print "Error Status: " + error_stat
    else:
        with open('./Users/'+displayName+'.json','w') as f:
            json.dump(userData, f)

def getIndividualUserJSONs():
    getUsersFromBungieTable()

if __name__ == "__main__":
    getIndividualUserJSONs()
