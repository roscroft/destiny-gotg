import sqlite3 as lite
import sys
sys.path.append('../../')
sys.path.append('../')
import DatabaseModules.databaseStatements as db

databasePath = '../Leaderboard/guardians.db'

table = "Discord"
fields = "(discName TEXT, destName TEXT)"
db.initialize(table, fields)

request = "SELECT Name FROM Bungie"
nameList = db.select(request)

for name in nameList:
    request = "INSERT INTO Discord VALUES(?, ?)"
    toInsert = (None, name)
    db.insert(request, toInsert)
