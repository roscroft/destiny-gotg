#!/usr/bin/python

import sqlite3 as lite
import sys
import os
import json

def parseClanUserJSON():
    players = []
    for filename in os.listdir('./Clan/'):
        if filename.endswith(".json"):
            with open('./Clan/'+filename) as data_file:
                data = json.load(data_file)
                for result in data['Response']['results']:
                    name = str(result['user']['displayName'])
                    players.append((result['membershipId'],name))
#    for player in players:
#        print player
    return tuple(players)

def addToDatabase(players):
    con = lite.connect('guardians.db')
    with con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS Bungie")
        cur.execute("CREATE TABLE Bungie(Id INT, Name TEXT)")
        cur.executemany("INSERT INTO Bungie VALUES(?, ?)", players)

def buildBungieTable():
    players = parseClanUserJSON()
    addToDatabase(players)

if __name__ == "__main__":
    buildBungieTable()
