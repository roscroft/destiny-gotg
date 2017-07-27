#!/usr/bin/python
import json
import requests
import sys
sys.path.append('../')
sys.path.append('../../')
import DatabaseModules.databaseStatements as db
import Tokens.getHeader as h
import APIRequests.jsonRequester as jr

def getMissingUserJSONs(path, header):
    def getMissingUsers():
        request = "SELECT Bungie.Name FROM Bungie LEFT JOIN Discord ON Bungie.Name = Discord.Name WHERE Destiny.Id IS NULL"
        users = db.select(request)
        print users
        return users


