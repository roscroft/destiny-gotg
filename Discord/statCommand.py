import sqlite3 as lite
import sys
from validateRequest import validateRequest
import re

databasePath = '../Leaderboard/guardians.db'

#Manages single user stat requests
#Request is read in as a list, always in the following order:
#[pvp|pve], [total|avg], [stat (aliases discussed below)], ([vs], [user1], [user2], ...)

def statCommand(request, author):
    def handleRequest(request, author):
        #Removes !stat
        request = " ".join(request.split(" ")[1:])
        valid = validateRequest(request)
        if valid == 0:
            return "Request not valid."
        request = request.split(" ")
        
        realm = request[0]
        style = request[1]
        if style == "avg":
            style = "pga"
        tableName = realm+style
        stat = request[2]
        if valid == 1 or valid == 2:
            output = singleStatReq(tableName, stat, author)
        elif valid == 3 or valid == 4:
            usersCommas = request[4:]
            reg = re.compile('\W+')
            users = [re.sub(reg,'',i) for i in usersCommas]
            users.append(author)
            output = multiStatReq(tableName, stat, users)
        return output

    def singleStatReq(tableName, stat, author):
        con = lite.connect(databasePath)
        with con:
            cur = con.cursor()
            cur.execute("SELECT " + stat + " FROM " + tableName + " WHERE Name = ?",(author,))
            row = cur.fetchone()
            if not row:
                return "Value does not exist."    
            value = row[0]
            #output = author+", your " + tableName[3:] + " " + stat + " are: " + str(value)
            if "pga" in tableName:
                start = "Average "
            else:
                start = "Total "
            output = start + stat + " for " + author + ": " + str(value)
            return output

    def multiStatReq(tableName, stat, users):
        con = lite.connect(databasePath)
        sqlString = "SELECT Name, " + stat + " FROM " + tableName + " WHERE"
        whereString = ""
        for user in users:
            whereString += " Name = '" + user + "' OR"
        sqlString += whereString[:-3]
        sqlString += " ORDER BY " + stat + " DESC"
        with con:
            cur = con.cursor()
            cur.execute(sqlString)
            output = []
            while True:
                row = cur.fetchone()
                if row == None:
                    break
                else:
                    output.append(row)
        return output

    output = handleRequest(request, author)
    return output
