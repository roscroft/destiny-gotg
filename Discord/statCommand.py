from validateRequest import validateRequest
import re
import discord
import sys
sys.path.append('../../')
sys.path.append('../')
import DatabaseModules.databaseStatements as db

databasePath = '../Leaderboard/guardians.db'

#Manages single user stat requests
#Request is read in as a list, always in the following order:
#[pvp|pve], [total|avg], [stat (aliases discussed below)], ([vs], [user1], [user2], ...)

def statCommand(req, auth):
    def handleRequest(request, reqCode):
        #Removes !stat
        request = request.split(" ")
        realm = request[0]
        style = request[1]
        if style == "avg":
            style = "pga"
        tableName = realm+style
        stat = request[2]
        if reqCode == 1 or reqCode == 2:
            return (tableName, stat, [])
        elif reqCode == 3 or reqCode == 4:
            usersCommas = request[4:]
            reg = re.compile('\W+')
            users = [re.sub(reg,'',i) for i in usersCommas]
            users.append(auth)
            return (tableName, stat, users)
        elif reqCode == 5 or reqCode == 6:
            users = getAllDestUsers()
            return (tableName, stat, users)

    def statEmbed(resultList, statTitle):
        if statTitle == "Request not valid.":
            em = discord.Embed(title = "Request not valid.")
        else:
            userList = [i[0] for i in resultList]
            userTitle = ", ".join(userList)
            if len(userList)==18:
                userTitle = "Top 18"
            em = discord.Embed(title = statTitle + "for: "+userTitle, colour=0xADD8E6)
            for result in resultList:
                em.add_field(name=result[0],value=result[1])
        return em

    def singleStatReq(tableName, stat, author):
        statRequest = "SELECT Name, " + stat + " FROM " + tableName + " WHERE Name = ?"
        params = (author,)
        output = db.select(statRequest, params)
        return [output]

    def getDestUser(user):
        destRequest = "SELECT EXISTS(SELECT destName FROM Discord WHERE discName = ?"
        params = (user,)
        output = db.select(destRequest, params)
        
        if output[0] != 0:
            destRequest = "SELECT destName FROM Discord WHERE discName = ?"
            output = db.select(destRequest, params)
            return output
        else:
            destRequest = "SELECT EXISTS(SELECT destName FROM Discord WHERE destName = ?"
            output = db.select(destRequest, params)
            if output[0] != 0:
                return user
            else:
                return "" 
        
        
        #con = lite.connect(databasePath)
        #with con:
        #    cur = con.cursor()
        #    cur.execute("SELECT EXISTS(SELECT destName FROM Discord WHERE discName = ?)",(user,))
        #    row = cur.fetchone()
        #    if row[0] != 0:
        #        cur.execute("SELECT destName FROM Discord WHERE discName = ?",(user,))
        #        return cur.fetchone()[0]
        #    else:
        #        cur.execute("SELECT EXISTS(SELECT destName FROM Discord WHERE destName = ?)",(user,))
        #        row = cur.fetchone()
        #        if row[0] != 0:
        #            return user
       #         else:
       #             return ""

    def getAllDestUsers():
        userRequest = "SELECT Name FROM Bungie"
        names = db.select(userRequest)
        return names
        #con = lite.connect(databasePath)
        #with con:
           # cur = con.cursor()
           # cur.execute("SELECT Name FROM Bungie")
           # names = []
           # while True:
           #     row = cur.fetchone()
           #     if row == None:
           #         break
           #     else:
           #         names.append(row[0])
        #return names

    def multiStatReq(tableName, stat, users):
        sqlString = "SELECT Name, " + stat + " FROM " + tableName + " WHERE"
        whereString = ""
        for user in users:
            destUser = getDestUser(user)
            if destUser == "":
                continue
            else:
                whereString += " Name = '" + destUser + "' OR"
        sqlString += whereString[:-3]
        sqlString += " ORDER BY " + stat + " DESC LIMIT 18"
        
        output = db.select(sqlString)
        return output


       # con = lite.connect(databasePath)
       # with con:
       #     cur = con.cursor()
       #     cur.execute(sqlString)
       #     output = []
       #     while True:
       #         row = cur.fetchone()
       #         if row == None:
       #             break
       #         else:
       #             output.append(row)
       # return output
    #Grab request code - 0 is invalid, 1 is pvp, 2 is pve, 3 is pvpVs, 4 is pveVs
    req = " ".join(req.split(" ")[1:])
    reqCode = validateRequest(req)
    
    if reqCode == 0:
        embed = statEmbed([], "Request not valid.")
        return embed
    (table, stat, users) = handleRequest(req, reqCode)
    
    if "pga" in table:
        start = "Average"
    else:
        start = "Total"
    statTitle = start + " " + stat + " "
    if users == []:
        output = singleStatReq(table, stat, auth)
    else:
        output = multiStatReq(table, stat, users)
    embed = statEmbed(output, statTitle) 
    return embed

