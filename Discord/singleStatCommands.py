import sqlite3 as lite
import sys
from validateRequest import validateRequest

databasePath = '../Leaderboard/guardians.db'

#Manages single user stat requests
#Request is read in as a list, always in the following order:
#[pvp|pve], [total|avg], [stat (aliases discussed below)], ([vs], [user1], [user2], ...)

def singleStatCommands(request, author):
    def handleRequest(request, author):
        #Removes !stat
        request = " ".join(request.split(" ")[1:])
        valid = validateRequest(request)
        if not valid:
            return "Request not valid."
        request = request.split(" ")
        #Builds table name from pvp|pve and total|avg
        realm = request[0]
        style = request[1]
        stat = request[2]
        
        if style == "avg":
            style = "pga"
        tableName = realm+style

        output = singleStatReq(tableName, stat, author)
        return output

    def singleStatReq(tableName, stat, author):
        con = lite.connect('../Leaderboard/guardians.db')
        with con:
            cur = con.cursor()
            cur.execute("SELECT " + stat + " FROM " + tableName + " WHERE Name = ?",(author,))
            row = cur.fetchone()
            value = row[0]
            output = author+", your " + tableName[3:] + " " + stat + " are: " + str(value)
            return output

    output = handleRequest(request, author)
    return output
