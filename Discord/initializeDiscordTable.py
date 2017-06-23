import sqlite3 as lite
import sys

databasePath = '../Leaderboard/guardians.db'

con = lite.connect(databasePath)
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Discord")
    cur.execute("CREATE TABLE Discord(discName TEXT, destName TEXT)")

    cur.execute("SELECT Name FROM Bungie")
    nameList = []
    while True:
        row = cur.fetchone()

        if row == None:
            break

        else:
            nameList.append(row[0])
    for name in nameList:
        cur.execute("INSERT INTO Discord VALUES(?, ?)", (None, name))
