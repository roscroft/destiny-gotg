#!/usr/bin/python

import sqlite3 as lite
import sys
import os
import json

def buildDestinyTable(path, databasePath):
    def parseUserJSON():
        players = set()
        characters = []
        for filename in os.listdir(path):
            if filename.endswith(".json"):
                with open(path+filename) as data_file:
                    data = json.load(data_file)
                    characters = data['Response']['destinyAccounts']
                    for character in characters:
                        membershipId = str(character['userInfo']['membershipId'])
                        membershipType = str(character['userInfo']['membershipType'])
                        players.add((membershipId, membershipType))
                    # Should grab all character Ids. Seems like I don't actually grab anything, and not used currently, so commented out
                    #characters = data['Response']['destinyAccounts'][0]
                    #for character in characters:
                    #    characterIds.append(['characterId'])
        return tuple(players)

    def addToDatabase(players):
        con = lite.connect(databasePath)
        with con:
            cur = con.cursor()
            cur.execute("DROP TABLE IF EXISTS Destiny")
            cur.execute("CREATE TABLE Destiny(Id INT, Type INT)")
            cur.executemany("INSERT INTO Destiny VALUES(?, ?)", players)

    players = parseUserJSON()
    addToDatabase(players)

if __name__ == "__main__":
    path = '../Users/'
    databasePath = '../guardians.db'	 
    buildDestinyTable(path, databasePath)
