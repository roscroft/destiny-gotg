#!/usr/bin/python

import sqlite3 as lite
import sys
import os
import json

def buildBungieTable(path, databasePath):
    def parseClanUserJSON():
        players = []
        for filename in os.listdir(path):
            if filename.endswith(".json"):
                with open(path+filename) as data_file:
                    data = json.load(data_file)
                    for result in data['Response']['results']:
                        name = str(result['user']['displayName'])
                        players.append((result['membershipId'],name))
        return tuple(players)

    def addToDatabase(players):
        con = lite.connect(databasePath)
        with con:
            cur = con.cursor()
            cur.execute("DROP TABLE IF EXISTS Bungie")
            cur.execute("CREATE TABLE Bungie(Id INT, Name TEXT)")
            cur.executemany("INSERT INTO Bungie VALUES(?, ?)", players)

    players = parseClanUserJSON()
    addToDatabase(players)

if __name__ == "__main__":
    path = '../Clan/'
    databasePath = '../guardians.db'
    buildBungieTable(path, databasePath)
