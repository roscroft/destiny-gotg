#!/usr/bin/python3.6
import os, re, sys
import discord, asyncio
from datetime import datetime
from destinygotg import Session, loadConfig
from initdb import PvPTotal, PvETotal, PvPAverage, PvEAverage, Base, Discord, Account
from sqlalchemy import exists

def runBot(engine):
    # The regular bot definition things
    client = discord.Client()

    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')

    @client.event
    async def queryDatabase(channel, statement, connection):
        result = connection.execute(statement)
        resultList = [row for row in result]
        await client.send_message(channel, resultList)
    
    @client.event
    async def registerHandler(discordAuthor):
        discId = discordAuthor.id
        session = Session()
        userIsRegistered = session.query(exists().where(Discord.id == discId)).scalar()
        if userIsRegistered:
            destinyName = session.query(Account.display_name).filter(Account.discord_id == discId)
        else:
            destinyName = await registerUser(discordAuthor)
        return destinyName

    @client.event
    async def registerUser(discordAuthor):
        session = Session()
        def checkIfValidUser(userName):
            return session.query(exists().where(Account.display_name == userName)).scalar()
        #Need to send a DM requesting the PSN name
        destination = discordAuthor
        discName = discordAuthor.name
        await client.send_message(destination, discName+", please enter your PSN display name.")
        nameMsg = await client.wait_for_message(author=discordAuthor,check=checkIfValidUser(discName))
        destName = nameMsg.content
        discordDict = {}
        discordDict['id'] = discordAuthor.id
        discordDict['discord_name'] = discordAuthor.name
        new_discord_user = Discord(**discordDict)
        session.add(new_discord_user)
        session.commit()
        await client.send_message(destination, discName+", you have been successfully registered!")
        return destName

    @client.event
    async def on_message(message):
        if message.content.startswith('!timeleft'):
            output = timeLeft()
            await client.send_message(message.channel, output)
        #elif message.content.startswith('!help'):
        #    await client.send_message(message.channel, 'Commands: !timeleft, !stat.')
        elif message.content.startswith('Right Gary?'):
            await client.send_message(message.channel, 'Right.')
        elif message.content.startswith('Say goodbye'):
            await client.send_message(message.channel, 'beep boop')
        elif message.content.startswith('!sql'):
            roleList = [role.name for role in message.author.roles]
            if "@administrator" in roleList and "@bot-developer" in roleList:
                statement = message.content[5:]
                connection = engine.connect()
                channel = message.channel
                await queryDatabase(channel, statement, connection)
            else:
                await client.send_message(message.channel, "Permission denied!")
        elif message.content.startswith('!stat'):
            discordAuthor = message.author
            destName = await registerHandler(discordAuthor)
            #req = message.content
            #output = statCommand(req, destName)
            #await client.send_message(message.channel, embed=output)
            output = f"Your destiny username is: {destName}"
            await client.send_message(message.channel, output)
        elif message.author.name == "Roscroft" and message.channel.is_private:
            if not message.content == "Roscroft":
                await client.send_message(discord.Object(id='322173351059521537'), message.content)
        elif message.content.startswith('!channel-id'):
            print(message.channel.id)

    client.run(os.environ['DISCORD_APIKEY'])


##Manages single user stat requests
##Request is read in as a list, always in the following order:
##[pvp|pve], [total|avg], [stat (aliases discussed below)], ([vs], [user1], [user2], ...)
#
#def statCommand(req, auth):
#    def handleRequest(request, reqCode):
#        #Removes !stat
#        request = request.split(" ")
#        realm = request[0]
#        style = request[1]
#        if style == "avg":
#            style = "pga"
#        tableName = realm+style
#        stat = request[2]
#        if reqCode == 1 or reqCode == 2:
#            return (tableName, stat, [])
#        elif reqCode == 3 or reqCode == 4:
#            usersCommas = request[4:]
#            reg = re.compile('\W+')
#            users = [re.sub(reg,'',i) for i in usersCommas]
#            users.append(auth)
#            return (tableName, stat, users)
#        elif reqCode == 5 or reqCode == 6:
#            users = getAllDestUsers()
#            return (tableName, stat, users)
#
#    def statEmbed(resultList, statTitle):
#        if statTitle == "Request not valid.":
#            em = discord.Embed(title = "Request not valid.")
#        else:
#            userList = [i[0] for i in resultList]
#            userTitle = ", ".join(userList)
#            if len(userList)==18:
#                userTitle = "Top 18"
#            em = discord.Embed(title = statTitle + "for: "+userTitle, colour=0xADD8E6)
#            for result in resultList:
#                em.add_field(name=result[0],value=result[1])
#        return em
#
#    def singleStatReq(tableName, stat, author):
#        statRequest = "SELECT Name, " + stat + " FROM " + tableName + " WHERE Name = ?"
#        params = (author,)
#        output = db.select(statRequest, params)
#        return [output]
#
#    def getDestUser(user):
#        destRequest = "SELECT EXISTS(SELECT destName FROM Discord WHERE discName = ?)"
#        params = (user,)
#        output = db.select(destRequest, params)
#        if output[0][0] == 1:
#            destRequest = "SELECT destName FROM Discord WHERE discName = ?"
#            output = db.select(destRequest, params)
#            return output[0][0]
#        else:
#            destRequest = "SELECT EXISTS(SELECT destName FROM Discord WHERE destName = ?)"
#            output = db.select(destRequest, params)
#            if output[0][0] == 1:
#                return user
#            else:
#                return "" 
#
#    def getAllDestUsers():
#        userRequest = "SELECT Name FROM Bungie"
#        names = db.select(userRequest)
#        nameList = [i[0] for i in names]
#        return nameList
#
#    def multiStatReq(tableName, stat, users):
#        sqlString = "SELECT Name, " + stat + " FROM " + tableName + " WHERE"
#        whereString = ""
#        for user in users:
#            destUser = getDestUser(user)
#            if destUser == "":
#                continue
#            else:
#                whereString += " Name = '" + destUser + "' OR"
#        sqlString += whereString[:-3]
#        sqlString += " ORDER BY " + stat + " DESC LIMIT 18"
#        
#        output = db.select(sqlString)
#        return output
#    
#    req = " ".join(req.split(" ")[1:])
#    reqCode = validateRequest(req)
#    
#    if reqCode == 0:
#        embed = statEmbed([], "Request not valid.")
#        return embed
#    (table, stat, users) = handleRequest(req, reqCode)
#    if "pga" in table:
#        start = "Average"
#    else:
#        start = "Total"
#    statTitle = start + " " + stat + " "
#    if users == []:
#        output = singleStatReq(table, stat, auth)[0]
#    else:
#        output = multiStatReq(table, stat, users)
#    embed = statEmbed(output, statTitle) 
#    return embed
#
#def timeLeft():
#    beta = datetime.date(2017,7,18)
#    release = datetime.date(2017,9,6)
#    today = datetime.date.today()
#    untilBeta = str((beta-today).days)
#    untilRelease = str((release-today).days)
#    output = "There are "+untilBeta+" days until the beta, and "+untilRelease+" days until release!"
#    return output
#
#if __name__ == "__main__":
#    print (timeLeft())
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#def validateRequest(session, request):
#    pvptotals = PvPTotal.__table__.columns.keys()
#    pvetotals = PvETotal.__table__.columns.keys()
#    pvpavgs = PvPAvg.__table__.columns.keys()
#    pveavgs = PvEAvg.__table__.columns.keys()
#
#    clanNames = session.query(Account, Account.display_name).all()
#
#
#
#
#    req = "SELECT destName FROM Discord"
#    destNames2 = db.select(req)
#    #This is a list of tuples, so we want to extract the first element from each
#    destNames2 = [i[0] for i in destNames2]
#    #print(destNames2)
#    req = "SELECT discName FROM Discord"
#    discNames2 = db.select(req)
#    discNames2 = [i[0] for i in discNames2]
#    #print(discNames2)    
#    nameString1 = "|".join(destNames2)
#    nameString2 = "|".join(discNames2)
#
#    def getValidStats(statPath):
#        with open(statPath,'r') as f:
#            return "|".join(f.read().split('\n'))[:-1]
#
#    pvpStatString = getValidStats(pvpStatPath)
#    pveStatString = getValidStats(pveStatPath)
#
#    pvpRegex = "^pvp (total|avg) ("+pvpStatString+")$"
#    pveRegex = "^pve (total|avg) ("+pveStatString+")$"
#    pvpVsRegex = "^pvp (total|avg) ("+pvpStatString+") vs (("+nameString1+")|("+nameString2+"))(, (("+nameString1+")|("+nameString2+")))*$"
#    pveVsRegex = "^pve (total|avg) ("+pveStatString+") vs (("+nameString1+")|("+nameString2+"))(, (("+nameString1+")|("+nameString2+")))*$"
#    pvpAllRegex = "^pvp (total|avg) ("+pvpStatString+") vs all$"
#    pveAllRegex = "^pve (total|avg) ("+pveStatString+") vs all$"
#
#    pvp = re.compile(pvpRegex)
#    pve = re.compile(pveRegex)
#    pvpVs = re.compile(pvpVsRegex)
#    pveVs = re.compile(pveVsRegex)
#    pvpAll = re.compile(pvpAllRegex)
#    pveAll = re.compile(pveAllRegex)
#
#    m = pvp.match(request)
#    n = pve.match(request)
#    o = pvpVs.match(request)
#    p = pveVs.match(request)
#    q = pvpAll.match(request)
#    r = pveAll.match(request)
#
#    if m:
#        return 1
#    elif n:
#        return 2
#    elif o:
#        return 3
#    elif p:
#        return 4
#    elif q:
#        return 5
#    elif r:
#        return 6
#    else:
#        return 0
#
#if __name__ == "__main__":
#    request = "!stat pvp total kills"
#    out = validateRequest(request)
#    print(out)

#if __name__ == "__main__":
#    # loadConfig for testing purposes
#    APP_PATH = "/etc/destinygotg"
#    loadConfig()
