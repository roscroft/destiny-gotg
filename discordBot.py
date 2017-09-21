#!/usr/bin/python3.6
import os
import sys
import discord
import asyncio
from datetime import datetime
from destinygotg import SESSION
from initdb import Base, Discord, Account, Character, Bungie
from sqlalchemy import exists, desc, func, and_
from decimal import *
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt; plt.rcdefaults()
from statDicts import stat_dict, mode_dict


def run_bot():
    # The regular bot definition things
    client = discord.Client()
    session = SESSION()

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
        def check_if_valid_user(message):
            player = message.content
            print(player)
            # valid = session.query(exists().where(and_(Account.display_name == message.content, Account.membership_type == 2))).scalar()
            all_players = [item[0].lower() for item in SESSION().query(Account.display_name).all()]
            valid = player.lower() in all_players
            print(valid)
            return valid
        #Need to send a DM requesting the PSN name
        destination = discord_author
        disc_name = discord_author.name
        message = await client.send_message(destination, f"{disc_name}, please enter your PSN display name.")
        valid = False 
        while not valid:
            name_msg = await client.wait_for_message(author=discord_author, channel=message.channel)
            valid = check_if_valid_user(name_msg)
            if not valid:
                await client.send_message(destination, "Please enter your PSN display name, and nothing else.")
        # Next line does the whole loop by itself
        # name_msg = await client.wait_for_message(author=discord_author,check=check_if_valid_user)
        dest_name = name_msg.content
        discord_dict = {'id' : discord_author.id, 'discord_name' : disc_name}
        discord_dict['membership_id'] = session.query(Account.id).filter(Account.display_name == dest_name).first()[0]
        new_discord_user = Discord(**discord_dict)
        session.add(new_discord_user)
        session.commit()
        await client.send_message(destination, f"{disc_name}, you have been successfully registered!")
        return dest_name

    @client.event
    async def on_message(message):
        if message.content.startswith('!timeleft'):
            output = time_left()
            await client.send_message(message.channel, output)

        elif message.content.startswith('!help'):
            await client.send_message(message.channel, 'See the #command-list channel for a list of commands.')

        elif message.content.startswith('Right Gary?'):
            await client.send_message(message.channel, 'Right.')

        elif message.content.startswith('Say goodbye'):
            await client.send_message(message.channel, 'beep boop')

        # elif message.content.startswith('!sql'):
        #     role_list = [role.name for role in message.author.roles]
        #     if "@administrator" in role_list and "bot developer" in role_list:
        #         statement = message.content[5:]
        #         connection = engine.connect()
        #         channel = message.channel
        #         await query_database(channel, statement, connection)
        #     else:
        #         await client.send_message(message.channel, "Permission denied!")

        # elif message.author.name == "Roscroft" and message.channel.is_private:
        #     if not message.content == "Roscroft":
        #         await client.send_message(discord.Object(id='322173351059521537'), message.content)

        elif message.content.startswith('!channel-id'):
            print(message.channel.id)

        elif message.content.startswith("!stat"):
            player = await register_handler(message.author)
            content = message.content
            return_dict, error_msg = validate(content, player)
            if return_dict == None:
                await client.send_message(message.channel, error_msg)
            else:
                data, msg, players = stat_request(return_dict)
                if len(data) == 1:
                    output = single_stat_format(data, msg, players)
                    await client.send_message(message.channel, output)
                else:
                    output = multi_stat_format(data, msg)
                    await client.send_message(message.channel, embed=output)
            #if message.channel.id is not '342754108534554624':
           #     await client.send_message(message.channel, "Please use the #stat channel for stat requests.")
            #else:
            # valid, players, code, stat = validate(player, content)
            # if valid and len(players) == 0:
            #     output = single_stat_request(player, code, stat)
            #     #await client.send_message(discord.Object(id='342754108534554624'), output)
            #     await client.send_message(message.channel, output)# embed=output)

        elif message.content.startswith("!clangraph"):
            player = await register_handler(message.author)
            all_players = [item[0] for item in SESSION().query(Account.display_name).all()]
            all_players = [p.replace(" ", "%") for p in all_players]
            content = message.content
            content += " vs "
            content += " ".join(all_players)
            return_dict, error_msg = validate(content, player)
            if return_dict == None:
                await client.send_message(message.channel, error_msg)
            else:
                data, msg, players = stat_request(return_dict)
                clan_graph_request(data, msg)
                await client.send_file(message.channel, './Figures/hist.png')

        elif message.content.startswith("!clanstat"):
            pass

        elif message.content.startswith("!members"):
            num_members = SESSION().query(func.count(Bungie.id)).first()[0]
            await client.send_message(message.channel, num_members)

        elif message.content.startswith('!light'):
            player = await register_handler(message.author)
            data = light_level_request(player)
            output = ""
            for item in data:
                output += f"{item[1]}: {item[0]} "
            await client.send_message(message.channel, output)

    client.run(os.environ['DISCORD_APIKEY'])
    
def check_players(player_list):
    player_list = [p.replace("%", " ") for p in player_list]
    all_players = [item[0].lower() for item in SESSION().query(Account.display_name).all()]
    players_are_valid = [True if player.lower() in all_players else False for player in player_list]
    return all(players_are_valid)

def validate(request, player):
    #Table name, primary keys (id and mode), column name(s), player name(s), message
    #TODO: update this with other modes
    info = request.split(" ")
    try:
        command = info[0]
        c_mode = info[1]
        c_stat = info[2]
        multi = False
        if len(info) > 3:
            multi = True
            vs = info[3]
            player_list = info[4:]
    except IndexError:
        error = "Improperly formatted request. Please see the #command-list channel."
        return None, error
    # valid_command = c_command in command_dict.keys()
    valid_command = True
    valid_mode = c_mode in mode_dict.keys()
    valid_stat = c_stat in stat_dict.keys()
    if multi:
        valid_vs = vs == "vs"
        valid_player_list = check_players(player_list)
    if not valid_command:
        error = "Invalid command. Try !help for a list of possible commands."
        return None, error
    elif not valid_mode:
        error = f"Invalid mode. Available modes are {mode_dict.keys()}."
        return None, error
    elif not valid_stat:
        error = "Invalid stat. See the #command-list channel for a list of valid stats."
        return None, error
    if multi:
        if not valid_vs:
            error = "Use 'vs' without quotes to compare stats with others."
            return None, error
        elif not valid_player_list:
            error = "One or more of the players you listed is not in the clan, or is not spelled properly."
            return None, error
    return_dict = {}
    return_dict["mode"] = mode_dict[c_mode]
    return_dict["table"] = stat_dict[c_stat]["table"]
    return_dict["column"] = stat_dict[c_stat]["column"]
    return_dict["message"] = stat_dict[c_stat]["message"]
    return_dict["players"] = [player]
    if multi:
        return_dict["players"] = return_dict["players"] + player_list
    return return_dict, ""

def stat_request(request_dict):
    mode = request_dict["mode"]
    table = request_dict["table"]
    column = request_dict["column"]
    message = request_dict["message"]
    players = request_dict["players"]
    players = [player.lower() for player in players]
    
    session = SESSION()
    res = session.query(*(getattr(table, col) for col in [column]), Account.display_name).join(Account).filter(func.lower(Account.display_name).in_(players), table.mode == mode).all()
    data = [(item[1], truncate_decimals(item[0])) for item in res if item[0] is not None]
    data = sorted(data, key=lambda x: x[1], reverse=True)
    return (data, message, players)

def single_stat_format(data, message, players):
    return f"```{message} for {players[0]}: {data[0][1]}```"

def multi_stat_format(data, message):
    em = discord.Embed(title = f"{message}", colour=0xADD8E6)
    if len(data) > 10:
        data = data[:9]
    for (name, num) in data:
        em.add_field(name=name, value=num)
    return em

def clan_graph_request(data, message):
    plt.clf()
    #num_bins = 45
    #n, bins, patches = plt.hist(nums, num_bins, facecolor='blue', alpha=0.5)
    #plt.xlabel('Kill/Death Ratio')
    #plt.ylabel('Guardians')
    #plt.title('Histogram of K/D')
    objects = [item[0] for item in data]
    #objects = [" " if item != player else item for item in objects]
    values = [item[1] for item in data]
    
    fig, ax = plt.subplots(figsize=(20,6))
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
    session = SESSION()
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
