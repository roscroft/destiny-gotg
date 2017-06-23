import discord
import asyncio
import sqlite3 as lite
import sys
from singleStatCommands import singleStatCommands
from timeLeft import timeLeft

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
        req = message.content
        discordAuthor = message.author
        destName = registerHandler(discordAuthor)
        output = singleStatCommands(req, destName)
        await client.send_message(message.channel, output)

def queryDatabase(statement):
    output = []
    con = lite.connect(databasePath)
    cur = con.cursor()

    if statement.startswith("DROP"):
        return "No way pal"
    else:
        cur.execute(statement)
        rows = cur.fetchall()
        for row in rows:
            output.append(row)
    if len(output)==1:
        if len(output[0])==1:
            return output[0][0]
        else:
            return output[0]
    else:
        return output

@client.event
async def registerUser(discordAuthor):
    #Need to send a DM requesting the PSN name
    dest = discordAuthor
    discName = discordAuthor.name
    await client.send_message(dest, author+", please enter your PSN display name.")
    destName = await client.wait_for_message(author=message.author)

    con = lite.connect(databasePath)
    with con:
        cur = con.cursor()
            cur.execute("UPDATE Discord SET destName=? WHERE discName=?",(destName, discName))

def registerHandler(discordAuthor):
    discName = discordAuthor.name
    con = lite.connect(databasePath)
    with con:
        cur = con.cursor()
        cur.execute("SELECT EXISTS(SELECT destName FROM Discord WHERE discName=?)",(author,))
        if cur.fetchone():
            cur.execute("SELECT destName FROM Discord WHERE discName=?",(author,))
            row = cur.fetchone()
            return row[0]
        else:
            destName = registerUser(discordAuthor)
            return destName

with open('botToken.txt','r') as f:
    botToken = f.readline().strip()

client.run(botToken)
