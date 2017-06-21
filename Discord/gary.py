import discord
import asyncio
import datetime
import sqlite3 as lite
import sys

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!messages'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    #elif message.content.startswith('!sleep'):
    #    await asyncio.sleep(5)
    #    await client.send_message(message.channel, 'Done sleeping')
    elif message.content.startswith('!timeleft'):
        beta = datetime.date(2017, 7, 18)
        release = datetime.date(2017, 9, 6)
        today = datetime.date.today()
        diff1 = beta-today
        diff2 = release-today
        await client.send_message(message.channel, 'There are '+str(diff1.days)+' days until the beta, and '+str(diff2.days)+' until release!')
    elif message.content.startswith('!help'):
        await client.send_message(message.channel, 'Current commands: !messages, !timeleft, !help.')
    elif message.content.startswith('Right Gary?'):
        await client.send_message(message.channel, 'Right.')
    elif message.content.startswith('!leaderboard'):
        with open('leaderboard.txt','r') as f:
            for line in f:
                await client.send_message(message.channel, line)
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

def queryDatabase(statement):
    output = []
    con = lite.connect("../Leaderboard/guardians.db")
    
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

with open('botToken.txt','r') as f:
    botToken = f.readline().strip()

client.run(botToken)
