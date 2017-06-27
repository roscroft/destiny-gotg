import sqlite3 as lite
import sys

databasePath = '../Leaderboard/guardians.db'

def select(request, params=()):
    singleStatement(request, params, True)

def update(request, params=()):
    singleStatement(request, params)

def insert(request, params=()):
    singleStatement(request, params)

def singleStatement(request, params, outputBool=False):
    def onlyContains(row, value):
        return row.count(None) == len(row)
    con = lite.connect(databasePath)
    with con:
        cur = con.cursor()
        cur.execute(request, params)
        output = None
        if outputBool:
            output = []
            while True:
                row = cur.fetchone()
                if row == None:
                    break
                elif onlyContains(row, None):
                    continue
                else:
                    output.append(row)
    return output

def initializeTable(table, fields):
    con = lite.connect(databasePath)
    with con:
        cur = con.cursor()
        dropStatement = "DROP TABLE IF EXISTS " + table
#        print "Drop: ", dropStatement
        createStatement = "CREATE TABLE " + table + fields
#        print "Create: ", createStatement
        cur.execute(dropStatement)
        cur.execute(createStatement)
