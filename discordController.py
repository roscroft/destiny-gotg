#!/usr/bin/python3.6
import os, re, sys
import discord, asyncio
from datetime import datetime
from destinygotg import Session, loadConfig
from initdb import PvPTotal, PvETotal, PvPAverage, PvEAverage, Base, Discord, Account, MedalsCharacter
from sqlalchemy import exists
from decimal import *

playerList = [item[0] for item in Session().query(Account.display_name).all()]

statDict = { "kd"           :(PvPTotal, "killsDeathsRatio", "'s kill/death ratio is: ")
            ,"kda"          :(PvPTotal, "killsDeathsAssists", "'s kills/assists/death ratio is: ")
            ,"wl"           :(PvPTotal, "winLossRatio", "'s win/loss ratio is: ")
            ,"bgs"          :(PvPTotal, "bestSingleGameScore", "'s best single game score is: ")
            ,"lks"          :(PvPTotal, "longestKillSpree", "'s longest kill spree is: ")
            ,"suicides"     :(PvPTotal, "suicides", "'s total number of suicides is: ")
            ,"spg"          :(PvPAverage, "suicides", "'s average suicides per game is: ")
            ,"mk"           :(PvPTotal, "bestSingleGameKills", "'s best single game kill score is: ")
            ,"kills"        :(PvPTotal, "kills", "'s total number of kills is: ")
            ,"kpg"          :(PvPAverage, "kills", "'s average kills per game is: ")
            ,"deaths"       :(PvPTotal, "deaths", "'s total number of deaths is: ")
            ,"dpg"          :(PvPAverage, "deaths", "'s average deaths per game is: ")
            ,"assists"      :(PvPTotal, "assists", "'s total number of assists is: ")
            ,"apg"          :(PvPAverage, "assists", "'s average assists per game is: ")
            ,"cr"           :(PvPTotal, "combatRating", "'s combat rating is: ")
            ,"pkills"       :(PvPTotal, "precisionKills", "'s total number of precision kills is: ")
            ,"score"        :(PvPTotal, "score", "'s total score is: ")
            ,"scpg"         :(PvPAverage, "score", "'s average score per game is: ")
            ,"crucibletime" :(PvPTotal, "secondsPlayed", "'s total playtime in seconds is: ")
            ,"akills"       :(PvPTotal, "abilityKills", "'s total number of ability kills is: ")
            ,"akpg"         :(PvPAverage, "abilityKills", "'s average ability kills per game is: ")
            ,"games"        :(PvPTotal, "activitiesEntered", "'s total number of activities entered is: ")
            ,"wins"         :(PvPTotal, "activitiesWon", "'s total number of activities won is: ")
            ,"lsl"          :(PvPTotal, "longestSingleLife", "'s longest single life in seconds is: ")
            ,"mercy"        :(MedalsCharacter, "medalsActivityCompleteVictoryMercy", "'s total number of mercy medals is: ")
            }

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
        elif message.author.name == "Roscroft" and message.channel.is_private:
            if not message.content == "Roscroft":
                await client.send_message(discord.Object(id='322173351059521537'), message.content)
        elif message.content.startswith('!channel-id'):
            print(message.channel.id)
        elif message.content.startswith("!stat"):
            author = message.author.name
            content = message.content
            #if message.channel.id is not '342754108534554624':
           #     await client.send_message(message.channel, "Please use the #stat channel for stat requests.")
            #else:
            valid, stat, players = validate(author, content)
            if valid and len(players) == 0:
                output = singleStatRequest(author, stat)
                #await client.send_message(discord.Object(id='342754108534554624'), output)
                await client.send_message(message.channel, output)# embed=output)
            elif valid and len(players) > 0:
                players.append(author)
                players.sort()
                #print(f"Full player list: {players}")
                output = multiStatRequest(stat, players)
                await client.send_message(message.channel, embed=output)
            else:
                await client.send_message(message.channel, "```Invalid stat request.```")

    def validate(author, content):
        statList = content.split(" ")
        statList = statList[1:]
        stat = statList[0]
        isTracked = stat in statDict.keys()
        isValid = isTracked
        players = []
        if len(statList) > 1:
            isVs = statList[1] == "vs"
            players = statList[2:]
            #print(f"Players: {players}")
            areValidPlayers = [player in playerList for player in players]
            #print(f"Players are valid: {areValidPlayers}")
            isValid = isValid and isVs and (False not in areValidPlayers)
        return (isValid, stat, players)

    def singleStatRequest(author, stat):
        """Actually retrieves the stat and returns the stat info in an embed"""
        session = Session()
        (table, col, message) = statDict[stat]
        columns = [col]
        #res = session.query(display_name, *(getattr(table, column) for column in columns)).join(Account).filter(Account.display_name == author).first()
        res = session.query(*(getattr(table, column) for column in columns)).join(Account).filter(Account.display_name == author).first()
        #Returns a tuple containing the stat, but only the first element is defined for some reason.
        result = truncateDecimals(res[0])
        #em = discord.Embed(title = f"{author}{message}{result}", colour=0xADD8E6)
        em = f"```{author}{message}{result}```"
        return em
    
    def multiStatRequest(stat, players):
        session = Session()
        (table, col, message) = statDict[stat]
        columns = [col]
        res = session.query(*(getattr(table, column) for column in columns)).join(Account).filter(Account.display_name.in_(players)).order_by(Account.display_name).all()
        nums = [truncateDecimals(item[0]) for item in res]
        #print(f"Nums: {nums}")
        #em = discord.Embed(title = f"{author}{message}{result}", colour=0xADD8E6)
        em = discord.Embed(title = f"{message}", colour=0xADD8E6)
        for i in range(len(nums)):
            em.add_field(name=players[i], value=nums[i])
        return em

    def timeLeft():
        release = datetime.date(2017,9,6)
        today = datetime.date.today()
        untilRelease = str((release-today).days)
        output = "There are "+untilRelease+" days until release!"
        return output
    
    def truncateDecimals(num):
        #Apparently I have to write my own damn significant figures checker
        if num%1==0:
            result = num
        elif num > 10000:
            result = Decimal(num).quantize(Decimal('1.'))
        else:
            def firstPowerOfTen(power, num):
                if num > power:
                    return power
                else:
                    return firstPowerOfTen(power/10, num)
            power = firstPowerOfTen(1000, num)
            prec = power/1000
            result = Decimal(num).quantize(Decimal(str(prec)))
        return result

    client.run(os.environ['DISCORD_APIKEY'])
