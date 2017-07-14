#!/usr/bin/python
import sys
sys.path.append('../../')
sys.path.append('../')
import DatabaseModules.databaseStatements as db
import os
import json

def buildCharactersTable(path, databasePath):
    def parseUserJSON():
        players = set()
        characterIds = []
        for filename in os.listdir(path):
            if filename.endswith(".json"):
                with open(path+filename) as data_file:
                    data = json.load(data_file)
                    characters = data['Response']['destinyAccounts']
                    for character in characters:
                        characterId = str(character['userInfo']['characterId'])
                        players.add((membershipId, membershipType))
                    # Should grab all character Ids. Seems like I don't actually grab anything, and not used currently, so commented out
                    #characters = data['Response']['destinyAccounts'][0]
                    #for character in characters:
                    #    characterIds.append(['characterId'])
        return tuple(players)

    def addToDatabase(players):
        table = "Destiny"
        fields = "(Id INT, Type INT)"
        db.initializeTable(table, fields)
        for player in players:
            request = "INSERT INTO Destiny VALUES(?,?)"
            db.insert(request,player)

    players = parseUserJSON()
    addToDatabase(players)

if __name__ == "__main__":
    path = '../Users/'
    databasePath = '../guardians.db'	 
    buildDestinyTable(path, databasePath)
