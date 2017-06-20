import requests
import json
import sqlite3 as lite
import sys
import os

def getHeader():
    with open('header.txt','r') as f:
        header = f.readline().strip()
    return {"X-API-KEY":header}

def getUsersFromBungieTable():
    con = lite.connect('guardians.db')
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Bungie")
        while True:
            row = cur.fetchone()
            if row == None:
                break
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

def parseUserJSON():
    players = []
    characters = []
    for filename in os.listdir('./Users/'):
        if filename.endswith(".json"):
            with open('./Users/'+filename) as data_file:
                data = json.load(data_file)
                characters = data['Response']['destinyAccounts'][0]
                membershipId = str(characters['userInfo']['membershipId'])
                membershipType = str(characters['userInfo']['membershipType'])
                players.append((membershipId, membershipType))
                # Should grab all character Ids. Seems like I don't actually grab anything, and not used currently, so commented out
                #characters = data['Response']['destinyAccounts'][0]
                #for character in characters:
                #    characterIds.append(['characterId'])
    for player in players:
        print player
    return tuple(players)

if __name__ == "__main__":
    getUsersFromBungieTable()
    parseUserJSON()
