import discord
import asyncio
import sqlite3 as lite
import sys
from statCommand import statCommand
from timeLeft import timeLeft
import sys
sys.path.append('../../')
sys.path.append('../')
import DatabaseModules.databaseStatements as db
import re

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!timeleft'):
        output = timeLeft()
        await client.send_message(message.channel, output)
    elif message.content.startswith('!help'):
        await client.send_message(message.channel, 'Commands: !timeleft, !stat.')
    elif message.content.startswith('Right Gary?'):
        await client.send_message(message.channel, 'Right.')
    elif message.content.startswith('Say goodbye'):
        await client.send_message(message.channel, 'beep boop')
    elif message.content.startswith('!sql'):
        roles = message.author.roles
        if "@administrator" in [role.name for role in roles]:
            statement = message.content[5:]
            output = queryDatabase(statement)
            await client.send_message(message.channel, output)
        else:
            await client.send_message(message.channel, "Unauthorized user!")
    elif message.content.startswith('!stat'):
        discordAuthor = message.author
        destName = await registerHandler(discordAuthor)
        req = message.content
        output = statCommand(req, destName)
        await client.send_message(message.channel, embed=output)
        
def queryDatabase(statement):
    request = statement
    output = db.select(request)
    if len(output)==1:
        if len(output[0])==1:
            return output[0][0]
        else:
            return output[0]
    else:
        return output

@client.event
async def registerUser(discordAuthor):

    def checkIfValidUser(msg):
        request = "SELECT EXISTS(SELECT Name FROM Bungie WHERE Name=?)"
        params = (msg.content,)
        output = db.select(request, params)
        return output[0][0]

    #Need to send a DM requesting the PSN name
    destination = discordAuthor
    discName = discordAuthor.name
    await client.send_message(destination, discName+", please enter your PSN display name.")
    nameMsg = await client.wait_for_message(author=discordAuthor,check=checkIfValidUser)
    destName = nameMsg.content
    print(destName, discName)
    request = "UPDATE Discord SET discName=? WHERE destName=?"
    params = (discName, destName)
    db.update(request, params)
    
    await client.send_message(destination, discName+", you have been successfully registered!")
    return destName

@client.event
async def registerHandler(discordAuthor):
    discName = discordAuthor.name
    request = "SELECT EXISTS(SELECT destName FROM Discord WHERE discName=?)"
    params = (discName,)
    output = db.select(request, params)
    if output[0][0]:
        request = "SELECT destName FROM Discord WHERE discName=?"
        output = db.select(request, params)
        return output[0][0]
    else:
        destNamea = await registerUser(discordAuthor)
        return destName

with open('botToken.txt','r') as f:
    botToken = f.readline().strip()

client.run(botToken)
