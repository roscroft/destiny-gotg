#!/usr/bin/python
import os
import json
import sys
sys.path.append('../../')
sys.path.append('../')
import DatabaseModules.databaseStatements as db

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
        table = "Bungie"
        fields = "(Id INT, Name TEXT)"
        db.initializeTable(table, fields)
        for player in players:
            request = "INSERT INTO Bungie VALUES(?,?)"
            db.insert(request, player)

    players = parseClanUserJSON()
    addToDatabase(players)

if __name__ == "__main__":
    path = '../Clan/'
    databasePath = '../guardians.db'
    buildBungieTable(path, databasePath)
