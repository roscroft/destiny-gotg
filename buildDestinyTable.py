#!/usr/bin/python

import sqlite3 as lite
import sys
import os
import json

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
#    for player in players:
#        print player
    return tuple(players)

def addToDatabase(players):
    con = lite.connect('guardians.db')
    with con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS Destiny")
        cur.execute("CREATE TABLE Destiny(Id INT, Type INT)")
        cur.executemany("INSERT INTO Destiny VALUES(?, ?)", players)

def buildDestinyTable():
    players = parseUserJSON()
    addToDatabase(players)

if __name__ == "__main__":
    buildDestinyTable()
