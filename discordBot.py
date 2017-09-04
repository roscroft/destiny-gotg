#!/usr/bin/python3.6
import os
import sys
import discord
import asyncio
from datetime import datetime
from destinygotg import Session, load_config
from initdb import PvPAggregate, PvEAggregate, Base, Discord, Account, AccountMedals, Character, ClassReference
from sqlalchemy import exists, desc, func, and_
from decimal import *
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt; plt.rcdefaults()
from statDicts import stat_dict, medal_dict, character_dict

player_list = [item[0] for item in Session().query(Account.display_name).all()]

def run_bot(engine):
    # The regular bot definition things
    client = discord.Client()
    session = Session()

    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')

    @client.event
    async def query_database(channel, statement, connection):
        result = connection.execute(statement)
        result_list = [row for row in result]
        await client.send_message(channel, result_list)
    
    @client.event
    async def register_handler(discord_author):
        disc_id = discord_author.id
        user_is_registered = session.query(exists().where(Discord.id == disc_id)).scalar()
        if user_is_registered:
            destiny_name = session.query(Account.display_name).join(Discord).filter(Discord.id == disc_id).first()[0]
        else:
            destiny_name = await register_user(discord_author)
        return destiny_name

    @client.event
    async def register_user(discord_author):
        def check_if_valid_user(user_name):
            print(user_name)
            return session.query(exists().where(Account.display_name == user_name)).scalar()
        #Need to send a DM requesting the PSN name
        destination = discord_author
        disc_name = discord_author.name
        await client.send_message(destination, disc_name+", please enter your PSN display name.")
        name_msg = await client.wait_for_message(author=discord_author,check=check_if_valid_user(disc_name))
        dest_name = name_msg.content
        discord_dict = {}
        discord_dict['id'] = discord_author.id
        discord_dict['discord_name'] = disc_name
        print(dest_name)
        discord_dict['membership_id'] = session.query(Account.id).filter(Account.display_name == dest_name).first()[0]
        new_discord_user = Discord(**discord_dict)
        session.add(new_discord_user)
        session.commit()
        await client.send_message(destination, disc_name+", you have been successfully registered!")
        return dest_name

    @client.event
    async def on_message(message):
        if message.content.startswith('!timeleft'):
            output = time_left()
            await client.send_message(message.channel, output)
        #elif message.content.startswith('!help'):
        #    await client.send_message(message.channel, 'Commands: !timeleft, !stat.')
        elif message.content.startswith('Right Gary?'):
            await client.send_message(message.channel, 'Right.')
        elif message.content.startswith('Say goodbye'):
            await client.send_message(message.channel, 'beep boop')
        elif message.content.startswith('!sql'):
            role_list = [role.name for role in message.author.roles]
            if "@administrator" in role_list and "bot developer" in role_list:
                statement = message.content[5:]
                connection = engine.connect()
                channel = message.channel
                await query_database(channel, statement, connection)
            else:
                await client.send_message(message.channel, "Permission denied!")
        elif message.author.name == "Roscroft" and message.channel.is_private:
            if not message.content == "Roscroft":
                await client.send_message(discord.Object(id='322173351059521537'), message.content)
        elif message.content.startswith('!channel-id'):
            print(message.channel.id)
        elif message.content.startswith("!stat"):
            player = await register_handler(message.author)
            content = message.content
            #if message.channel.id is not '342754108534554624':
           #     await client.send_message(message.channel, "Please use the #stat channel for stat requests.")
            #else:
            valid, players, code, stat = validate(player, content)
            if valid and len(players) == 0:
                output = single_stat_request(player, code, stat)
                #await client.send_message(discord.Object(id='342754108534554624'), output)
                await client.send_message(message.channel, output)# embed=output)
            elif valid and len(players) > 0:
                players.append(player)
                output = multi_stat_request(players, code, stat)
                await client.send_message(message.channel, embed=output)
            else:
                await client.send_message(message.channel, "```Invalid stat request.```")
        elif message.content.startswith("!clangraph"):
            content = message.content
            player = await register_handler(message.author)
            valid, authplayer, code, stat = validate_clan_stat(player, content)
            output = clan_graph_request(authplayer, code, stat)
            await client.send_file(message.channel, './Figures/hist.png')
        elif message.content.startswith("!clanstat"):
            pass
        elif message.content.startswith('!light'):
            player = await register_handler(message.author)
            data = light_level_request(player)
            output = ""
            for item in data:
                output += f"{item[1]}: {item[0]} "
            await client.send_message(message.channel, output)

    client.run(os.environ['DISCORD_APIKEY'])
    
# Stat number codes - 0: Not a stat, 1: PvP/PvE aggregate, 2: Medal
def validate(player, content):
    stat_list = content.split(" ")[1:]
    stat = stat_list[0]
    track_code = 0
    if stat in stat_dict.keys():
        track_code = 1
    elif stat in medal_dict.keys():
        track_code = 2
    elif stat[:-2] in medal_dict.keys() and stat[-2:] == "pg":
        track_code = 3
        stat = stat[:-2]
    elif stat in character_dict.keys():
        track_code = 4
    players = []
    is_valid = (track_code != 0)
    if len(stat_list) > 1:
        is_vs = stat_list[1] == "vs"
        players = stat_list[2:]
        if players == ["all"]:
            players = player_list
        are_valid_players = [player in player_list for player in players]
        is_valid = (track_code != 0) and is_vs and (False not in are_valid_players)
    return (is_valid, players, track_code, stat)

def validate_clan_stat(player, content):
    stat = content.split(" ")[1]
    track_code = 0
    if stat in stat_dict.keys():
        track_code = 1
    elif stat in medal_dict.keys():
        track_code = 2
    elif stat[:-2] in medal_dict.keys() and stat[-2:] == "pg":
        track_code = 3
        stat = stat[:-2]
    elif stat in character_dict.keys():
        track_code = 4
    is_valid_player = player in player_list
    player_name = ""
    if is_valid_player:
        player_name = player
    return ((track_code != 0), player_name, track_code, stat)
    
def single_stat_request(player, code, stat):
    """Actually retrieves the stat and returns the stat info in an embed"""
    session = Session()
    message = ""
    if code == 1:
        (table, col, message) = stat_dict[stat]
        columns = [col]
        res = session.query(*(getattr(table, column) for column in columns), Account.display_name).join(Account).filter(Account.display_name == player).first()
        #Returns a tuple containing the stat, but only the first element is defined for some reason.
        num = truncate_decimals(res[0])
        name = res[1]
    elif code == 2 or code == 3:
        (table, col, message) = medal_dict[stat]
        columns = [col]
        res = session.query(func.sum(*(getattr(table, column) for column in columns))).join(Account).filter(Account.display_name == player).group_by(AccountMedals.id).first()
        num = float(res[0])
        name = player
        if message != "Activities Entered" and message != "Total Number of Medals" and message != "Total Medal Score":
            message = f"Total {message} Medals"
        if code == 3:
            denominator = session.query(PvPAggregate.activitiesEntered).join(Account).filter(Account.display_name == player).first()
            act = denominator[0]
            num = num/act
            if message != "Activities Entered" and message != "Total Number of Medals" and message != "Total Medal Score":
                message = f"{message} Medals per Game"
    elif code == 4:
        (table, col, message) = character_dict[stat]
        columns = [col]
        res = session.query(func.max(*(getattr(table, column) for column in columns)), Account.display_name).join(Account).filter(Account.display_name == player).first()
        #Returns a tuple containing the stat, but only the first element is defined for some reason.
        num = truncate_decimals(res[0])
        name = res[1]
    #em = discord.Embed(title = f"{author}{message}{result}", colour=0xADD8E6)
    em = f"```{message} for {name}: {num}```"
    return em

def multi_stat_request(players, code, stat):
    session = Session()
    data = []
    if code == 1:
        (table, col, message) = stat_dict[stat]
        columns = [col]
        res = session.query(*(getattr(table, column) for column in columns), Account.display_name).join(Account).filter(Account.display_name.in_(players)).order_by(Account.display_name).all()
        data = [(item[1], truncate_decimals(item[0])) for item in res if item[0] is not None]
    elif code == 2 or code == 3:
        (table, col, message) = medal_dict[stat]
        columns = [col]
        res = session.query(func.sum(*(getattr(table, column) for column in columns)), Account.display_name).join(Account).filter(Account.display_name.in_(players)).group_by(AccountMedals.id).order_by(Account.display_name).all()
        data = [(item[1], truncate_decimals(item[0])) for item in res if item[0] is not None]
        if code == 3:
            num_activities = session.query(PvPAggregate.activitiesEntered).join(Account).filter(Account.display_name.in_(players)).order_by(Account.display_name).all()
            data = [(res[i][1], truncate_decimals(float(res[i][0])/num_activities[i][0])) for i in range(len(res)) if res[i][0] is not None]
    elif code == 4:
        (table, col, message) = pveStatDict[stat]
        columns = [col]
        res = session.query(*(getattr(table, column) for column in columns), Account.display_name).join(Account).filter(Account.display_name.in_(players)).order_by(Account.display_name).all()
        data = [(item[1], truncate_decimals(item[0])) for item in res if item[0] is not None]
    data = sorted(data, key=lambda x: x[1], reverse=True)
    if (code == 2 or code == 3) and message != "Activities Entered" and message != "Total Number of Medals" and message != "Total Medal Score":
        message = f"Total {message} Medals"
    em = discord.Embed(title = f"{message}", colour=0xADD8E6)
    if len(data) > 10:
        data = data[:9]
    for (name, num) in data:
        em.add_field(name=name, value=num)
    return em

def clan_graph_request(player, code, stat):
    session = Session()
    rawdata = []
    message = ""
    if code == 1:
        (table, col, message) = stat_dict[stat]
        columns = [col]
        res = session.query(*(getattr(table, column) for column in columns), Account.display_name).join(Account).all()
        rawdata = [(item[1], truncate_decimals(item[0])) for item in res if item[0] is not None]
    elif code == 2 or code == 3:
        (table, col, message) = medal_dict[stat]
        columns = [col]
        res = session.query(func.sum(*(getattr(table, column) for column in columns)), Account.display_name).join(Account).group_by(AccountMedals.id).all()
        rawdata = [(item[1], truncate_decimals(item[0])) for item in res if item[0] is not None]
        if code == 3:
            num_activities = session.query(PvPAggregate.activitiesEntered, Account.display_name).join(Account).all()
            #Need to associate num_activities with the correct username
            rawdata = sorted(rawdata, key=lambda x: x[0])
            num_activities = sorted(num_activities, key=lambda x: x[1])
            rawdata = [(rawdata[i][0], rawdata[i][1]/float(num_activities[i][0])) for i in range(len(res)) if res[i][0] is not None]
            # rawdata = [(item[1], truncate_decimals(item[0])/float(activity[0])) for item in res for activity in num_activities if item[1] == activity[1] and item[0] is not None and activity[0] is not None]
    elif code == 4:
        (table, col, message) = pveStatDict[stat]
        columns = [col]
        res = session.query(*(getattr(table, column) for column in columns), Account.display_name).join(Account).all()
        rawdata = [(item[1], truncate_decimals(item[0])) for item in res if item[0] is not None]
    if (code == 2 or code == 3) and message != "Activities Entered" and message != "Total Number of Medals" and message != "Total Medal Score":
        message = f"Total {message} Medals"
    data = sorted(rawdata, key=lambda x: x[1])
    plt.clf()
    #num_bins = 45
    #n, bins, patches = plt.hist(nums, num_bins, facecolor='blue', alpha=0.5)
    #plt.xlabel('Kill/Death Ratio')
    #plt.ylabel('Guardians')
    #plt.title('Histogram of K/D')
    objects = [item[0] for item in data]
    #objects = [" " if item != player else item for item in objects]
    values = [item[1] for item in data]
    
    fig, ax = plt.subplots(figsize=(14,6))
    ax.set_facecolor("#F3F3F3")
    index = np.arange(len(objects))
    plt.bar(index, values, alpha=0.4, color="gold", edgecolor="black", align='center')
    #0096DB
    #7E8082
    plt.xlabel("Guardians")
    plt.ylabel(f"{message}")
    plt.title(f"Clan {message} Comparison")
    plt.xticks(index, objects)
    fig.autofmt_xdate()
    plt.tight_layout()
    plt.savefig('./Figures/hist.png')

def light_level_request(player):
    """Retrieves the character light levels of a player"""
    session = Session()
    data = session.query(Character.light_level, ClassReference.class_name).join(Account).join(ClassReference, and_(ClassReference.id==Character.class_hash)).filter(Account.display_name == player).all()
    return data

def truncate_decimals(num):
    #Apparently I have to write my own damn significant figures checker
    if num%1==0:
        result = num
    elif num > 10000:
        result = Decimal(num).quantize(Decimal('1.'))
    else:
        def first_power_of_ten(power, num):
            if num > power:
                return power
            else:
                return first_power_of_ten(power/10, num)
        power = first_power_of_ten(1000, num)
        prec = power/1000
        result = Decimal(num).quantize(Decimal(str(prec)))
    return result

def time_left():
    release = datetime.date(2017,9,6)
    today = datetime.date.today()
    until_release = str((release-today).days)
    output = "There are "+until_release+" days until release!"
    return output
