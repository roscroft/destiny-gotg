#!/usr/bin/python3.6
import os, re, sys
import discord, asyncio
from datetime import datetime
from destinygotg import Session, loadConfig
from initdb import PvPAggregate, PvEAggregate, Base, Discord, Account, AccountMedals, Character, ClassReference
from sqlalchemy import exists, desc, func, and_
from decimal import *
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt; plt.rcdefaults()

playerList = [item[0] for item in Session().query(Account.display_name).all()]

statDict = { "kd"           :(PvPAggregate, "killsDeathsRatio", "Kill/Death Ratio")
            ,"kda"          :(PvPAggregate, "killsDeathsAssists", "Kill/Assists/Death Ratio")
            ,"wl"           :(PvPAggregate, "winLossRatio", "Win/Loss Ratio")
            ,"bgs"          :(PvPAggregate, "bestSingleGameScore", "Best Single Game Score")
            ,"lks"          :(PvPAggregate, "longestKillSpree", "Longest Kill Spree")
            ,"suicides"     :(PvPAggregate, "suicides", "Total Number of Suicides")
            ,"spg"          :(PvPAggregate, "suicidespg", "Suicides per Game")
            ,"mk"           :(PvPAggregate, "bestSingleGameKills", "Best Single Game Kills")
            ,"kills"        :(PvPAggregate, "kills", "Total Number of Kills")
            ,"kpg"          :(PvPAggregate, "killspg", "Kills per Game")
            ,"deaths"       :(PvPAggregate, "deaths", "Total Number of Deaths")
            ,"dpg"          :(PvPAggregate, "deathspg", "Deaths per Game")
            ,"assists"      :(PvPAggregate, "assists", "Total Number of Assists")
            ,"apg"          :(PvPAggregate, "assistspg", "Assists Per Game")
            ,"cr"           :(PvPAggregate, "combatRating", "Combat Rating")
            ,"pkills"       :(PvPAggregate, "precisionKills", "Total Number of Precision Kills")
            ,"score"        :(PvPAggregate, "score", "Total score")
            ,"scpg"         :(PvPAggregate, "scorepg", "Score per Game")
            ,"crucibletime" :(PvPAggregate, "secondsPlayed", "Total Seconds in the Crucible")
            ,"akills"       :(PvPAggregate, "abilityKills", "Total Number of Ability Kills")
            ,"akpg"         :(PvPAggregate, "abilityKillspg", "Ability Kills per Game")
            ,"games"        :(PvPAggregate, "activitiesEntered", "Total Number of Activities Entered")
            ,"wins"         :(PvPAggregate, "activitiesWon", "Total Number of Activities Won")
            ,"lsl"          :(PvPAggregate, "longestSingleLife", "Longest Single Life")
            }

medalDict = { "activities"        :(AccountMedals, "activitiesEntered", "Activities Entered")
             ,"totalmedals"       :(AccountMedals, "allMedalsEarned", "Total Number of Medals")
             ,"totalscore"        :(AccountMedals, "allMedalsScore", "Total Medal Score")
             ,"stormbringer"      :(AccountMedals, "medalsAbilityArcLightningKillMulti", "Storm Bringer")
             ,"wayofthegun"       :(AccountMedals, "medalsAbilityGhostGunKillMulti", "Way of the Gun")
             ,"cryhavoc"          :(AccountMedals, "medalsAbilityHavocKillMulti", "Cry Havoc")
             ,"spacemagic"        :(AccountMedals, "medalsAbilityNovaBombKillMulti", "Space Magic")
             ,"scorchedearth"     :(AccountMedals, "medalsAbilityRadianceGrenadeKillMulti", "Scorched Earth")
             ,"gutted"            :(AccountMedals, "medalsAbilityShadowStrikeKillMulti", "Gutted")
             ,"hammerandtongs"    :(AccountMedals, "medalsAbilityThermalHammerKillMulti", "Hammer and Tongs")
             ,"wildhunt"          :(AccountMedals, "medalsAbilityVoidBowKillMulti", "Wild Hunt")
             ,"blastshield"       :(AccountMedals, "medalsAbilityWardDeflect", "Blast Shield")
             ,"objectivelycorrect":(AccountMedals, "medalsActivityCompleteControlMostCaptures", "Objectively Correct")
             ,"thecycle"          :(AccountMedals, "medalsActivityCompleteCycle", "The Cycle")
             ,"unbroken"          :(AccountMedals, "medalsActivityCompleteDeathless", "Mark of the Unbroken")
             ,"onthebrightside"   :(AccountMedals, "medalsActivityCompleteHighestScoreLosing", "On the Bright Side...")
             ,"thebestaround"     :(AccountMedals, "medalsActivityCompleteHighestScoreWinning", "The Best... Around")
             ,"lonewolf"          :(AccountMedals, "medalsActivityCompleteLonewolf", "Lone Wolf")
             ,"saboteur"          :(AccountMedals, "medalsActivityCompleteSalvageMostCancels", "Saboteur")
             ,"shutout"           :(AccountMedals, "medalsActivityCompleteSalvageShutout", "Shutout")
             ,"perfectrunner"     :(AccountMedals, "medalsActivityCompleteSingularityPerfectRunner", "Perfect Runner")
             ,"decisivevictory"   :(AccountMedals, "medalsActivityCompleteVictoryBlowout", "Decisive Victory")
             ,"victory"           :(AccountMedals, "medalsActivityCompleteVictory", "Victory")
             ,"trialbyfire"       :(AccountMedals, "medalsActivityCompleteVictoryElimination", "Trial by Fire")
             ,"bulletproof"       :(AccountMedals, "medalsActivityCompleteVictoryEliminationPerfect", "Bulletproof")
             ,"annihilation"      :(AccountMedals, "medalsActivityCompleteVictoryEliminationShutout", "Annihilation")
             ,"clutch"            :(AccountMedals, "medalsActivityCompleteVictoryExtraLastSecond", "Clutch")
             ,"comeback"          :(AccountMedals, "medalsActivityCompleteVictoryLastSecond", "Comeback")
             ,"nomercy"           :(AccountMedals, "medalsActivityCompleteVictoryMercy", "No Mercy")
             ,"sumofalltears"     :(AccountMedals, "medalsActivityCompleteVictoryRumbleBlowout", "Sum of all Tears")
             ,"aloneatthetop"     :(AccountMedals, "medalsActivityCompleteVictoryRumble", "Alone at the Top")
             ,"wontbebeat"        :(AccountMedals, "medalsActivityCompleteVictoryRumbleLastSecond", "Won't be Beat")
             ,"heartbreaker"      :(AccountMedals, "medalsActivityCompleteVictoryRumbleSuddenDeath", "Heartbreaker")
             ,"zerohour"          :(AccountMedals, "medalsActivityCompleteVictorySuddenDeath", "Zero Hour")
             ,"avenger"           :(AccountMedals, "medalsAvenger", "Avenger")
             ,"medic"             :(AccountMedals, "medalsBuddyResurrectionMulti", "Medic!")
             ,"angeloflight"      :(AccountMedals, "medalsBuddyResurrectionSpree", "Angel of Light")
             ,"narrowescape"      :(AccountMedals, "medalsCloseCallTalent", "Narrow Escape")
             ,"backinaction"      :(AccountMedals, "medalsComebackKill", "Back in Action")
             ,"domination"        :(AccountMedals, "medalsDominationKill", "Domination")
             ,"hattrick"          :(AccountMedals, "medalsDominionZoneCapturedSpree", "Hat Trick")
             ,"defender"          :(AccountMedals, "medalsDominionZoneDefenseKillSpree", "Defender")
             ,"atanycost"         :(AccountMedals, "medalsDominionZoneOffenseKillSpree", "At any Cost")
             ,"neversaydie"       :(AccountMedals, "medalsEliminationLastStandKill", "Never Say Die")
             ,"fromthebrink"      :(AccountMedals, "medalsEliminationLastStandRevive", "From the Brink")
             ,"ace"               :(AccountMedals, "medalsEliminationWipeQuick", "Ace")
             ,"wreckingball"      :(AccountMedals, "medalsEliminationWipeSolo", "Wrecking Ball")
             ,"firstblood"        :(AccountMedals, "medalsFirstBlood", "First Blood")
             ,"uprising"          :(AccountMedals, "medalsFirstPlaceKillSpree", "Uprising")
             ,"getitoff"          :(AccountMedals, "medalsGrenadeKillStick", "Get it Off!")
             ,"hazardpay"         :(AccountMedals, "medalsHazardKill", "Hazard Pay")
             ,"iseeyou"           :(AccountMedals, "medalsHunterKillInvisible", "I See You")
             ,"unsunghero"        :(AccountMedals, "medalsKillAssistSpree", "Unsung Hero")
             ,"enemyofmyenemy"    :(AccountMedals, "medalsKillAssistSpreeFfa", "Enemy of my Enemy")
             ,"bullseye"          :(AccountMedals, "medalsKillHeadshot", "Bullseye")
             ,"enforcer"          :(AccountMedals, "medalsKilljoy", "Enforcer")
             ,"endoftheline"      :(AccountMedals, "medalsKilljoyMega", "End of the Line")
             ,"doubledown"        :(AccountMedals, "medalsKillMulti2", "Double Down")
             ,"tripledown"        :(AccountMedals, "medalsKillMulti3", "Triple Down")
             ,"breaker"           :(AccountMedals, "medalsKillMulti4", "Breaker")
             ,"slayer"            :(AccountMedals, "medalsKillMulti5", "Slayer")
             ,"reaper"            :(AccountMedals, "medalsKillMulti6", "Reaper")
             ,"seventhcolumn"     :(AccountMedals, "medalsKillMulti7", "Seventh Column")
             ,"postmortem"        :(AccountMedals, "medalsKillPostmortem", "Postmortem")
             ,"merciless"         :(AccountMedals, "medalsKillSpree1", "Merciless")
             ,"relentless"        :(AccountMedals, "medalsKillSpree2", "Relentless")
             ,"reignofterror"     :(AccountMedals, "medalsKillSpree3", "Reign of Terror")
             ,"weranoutofmedals"  :(AccountMedals, "medalsKillSpreeAbsurd", "We Ran Out of Medals")
             ,"phantom"           :(AccountMedals, "medalsKillSpreeNoDamage", "Phantom")
             ,"stickaround"       :(AccountMedals, "medalsMeleeKillHunterThrowingKnifeHeadshot", "Stick Around")
             ,"payback"           :(AccountMedals, "medalsPaybackKill", "Payback")
             ,"andstaydown"       :(AccountMedals, "medalsRadianceShutdown", "...And Stay Down!")
             ,"overwatch"         :(AccountMedals, "medalsRescue", "Overwatch")
             ,"disruption"        :(AccountMedals, "medalsSalvageProbeCanceled", "Disruption")
             ,"salvagecrew"       :(AccountMedals, "medalsSalvageProbeCompleteSpree", "Salvage Crew")
             ,"improbeable"       :(AccountMedals, "medalsSalvageProbeDefenseKill", "Im-probe-able")
             ,"cleansweep"        :(AccountMedals, "medalsSalvageProbeOffenseKillMulti", "Clean Sweep")
             ,"relichunter"       :(AccountMedals, "medalsSalvageZoneCapturedSpree", "Relic Hunter")
             ,"unstoppableforce"  :(AccountMedals, "medalsSingularityFlagCaptureMulti", "Unstoppable Force")
             ,"denied"            :(AccountMedals, "medalsSingularityFlagHolderKilledClose", "Denied")
             ,"immovableobject"   :(AccountMedals, "medalsSingularityFlagHolderKilledMulti", "Immovable Object")
             ,"clearapath"        :(AccountMedals, "medalsSingularityRunnerDefenseMulti", "Clear a Path")
             ,"afistfulofcrests"  :(AccountMedals, "medalsSupremacy", "A Fistful of Crests...")
             ,"forafewcrestsmore" :(AccountMedals, "medalsSupremacyConfirmStreakLarge", "And For a Few Crests More")
             ,"honorguard"        :(AccountMedals, "medalsSupremacyDenyMulti", "Honor Guard")
             ,"mineallmine"       :(AccountMedals, "medalsSupremacyMostConfirms", "Mine! All Mine!")
             ,"handsoff"          :(AccountMedals, "medalsSupremacyMostDenies", "Hands Off")
             ,"illdoitmyself"     :(AccountMedals, "medalsSupremacyMostSelfConfirms", "I'll Do It Myself")
             ,"pickupthepieces"   :(AccountMedals, "medalsSupremacyMulti", "Pick Up the Pieces")
             ,"nevergonnagetit"   :(AccountMedals, "medalsSupremacyNeverCollected", "Never Gonna Get It")
             ,"nevermindfoundit"  :(AccountMedals, "medalsSupremacySelfDeny", "Never Mind, Found It")
             ,"lockdown"          :(AccountMedals, "medalsTeamDominationHold1m", "Lockdown")
             ,"strengthofthewolf" :(AccountMedals, "medalsTeamKillSpree", "Strength of the Wolf")
             ,"unknown"           :(AccountMedals, "medalsUnknown", "Unknown")
             ,"gunner"            :(AccountMedals, "medalsVehicleFotcTurretKillSpree", "Gunner")
             ,"bulldozer"         :(AccountMedals, "medalsVehicleInterceptorKillSplatter", "Bulldozer")
             ,"chariotoffire"     :(AccountMedals, "medalsVehicleInterceptorKillSpree", "Chariot of Fire")
             ,"skewered"          :(AccountMedals, "medalsVehiclePikeKillSplatter", "Skewered")
             ,"fallenangel"       :(AccountMedals, "medalsVehiclePikeKillSpree", "Fallen Angel")
             ,"neverspeakofthis"  :(AccountMedals, "medalsVehicleSparrowKillSplatter", "Never Speak of This Again")
             ,"automatic"         :(AccountMedals, "medalsWeaponAutoRifleKillSpree", "Automatic")
             ,"masterblaster"     :(AccountMedals, "medalsWeaponFusionRifleKillSpree", "Master Blaster")
             ,"deadmanshand"      :(AccountMedals, "medalsWeaponHandCannonHeadshotSpree", "Dead Man's Hand")
             ,"machinelord"       :(AccountMedals, "medalsWeaponMachineGunKillSpree", "Machine Lord")
             ,"fingeronthepulse"  :(AccountMedals, "medalsWeaponPulseRifleKillSpree", "Finger on the Pulse")
             ,"splashdamage"      :(AccountMedals, "medalsWeaponRocketLauncherKillSpree", "Splash Damage")
             ,"scoutshonor"       :(AccountMedals, "medalsWeaponScoutRifleKillSpree", "Scout's Honor")
             ,"buckshotbruiser"   :(AccountMedals, "medalsWeaponShotgunKillSpree", "Buckshot Bruiser")
             ,"sidekick"          :(AccountMedals, "medalsWeaponSidearmKillSpree", "Sidekick")
             ,"marksman"          :(AccountMedals, "medalsWeaponSniperRifleHeadshotSpree", "Marksman")
             ,"swordatagunfight"  :(AccountMedals, "medalsWeaponSwordKillSpree", "Sword at a Gun Fight")
             ,"nailinthecoffin"   :(AccountMedals, "medalsWinningScore", "Nail in the Coffin")
             ,"bline"             :(AccountMedals, "medalsZoneCapturedBInitial", "B-Line")
             }

def runBot(engine):
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
    async def queryDatabase(channel, statement, connection):
        result = connection.execute(statement)
        resultList = [row for row in result]
        await client.send_message(channel, resultList)
    
    @client.event
    async def registerHandler(discordAuthor):
        discId = discordAuthor.id
        userIsRegistered = session.query(exists().where(Discord.id == discId)).scalar()
        if userIsRegistered:
            destinyName = session.query(Account.display_name).join(Discord).filter(Discord.id == discId).first()[0]
        else:
            destinyName = await registerUser(discordAuthor)
        return destinyName

    @client.event
    async def registerUser(discordAuthor):
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
        discordDict['discord_name'] = discName
        discordDict['membership_id'] = session.query(Account.id).filter(Account.display_name == destName).first()[0]
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
            player = await registerHandler(message.author)
            content = message.content
            #if message.channel.id is not '342754108534554624':
           #     await client.send_message(message.channel, "Please use the #stat channel for stat requests.")
            #else:
            valid, players, code, stat = validate(player, content)
            if valid and len(players) == 0:
                output = singleStatRequest(player, code, stat)
                #await client.send_message(discord.Object(id='342754108534554624'), output)
                await client.send_message(message.channel, output)# embed=output)
            elif valid and len(players) > 0:
                players.append(player)
                output = multiStatRequest(players, code, stat)
                await client.send_message(message.channel, embed=output)
            else:
                await client.send_message(message.channel, "```Invalid stat request.```")
        elif message.content.startswith("!clangraph"):
            content = message.content
            player = await registerHandler(message.author)
            valid, authplayer, code, stat = validateClanStat(player, content)
            output = clanGraphRequest(authplayer, code, stat)
            await client.send_file(message.channel, './Figures/hist.png')
        elif message.content.startswith("!clanstat"):
            pass
        elif message.content.startswith('!light'):
            player = await registerHandler(message.author)
            data = lightLevelRequest(player)
            output = ""
            for item in data:
                output += f"{item[1]}: {item[0]} "
            await client.send_message(message.channel, output)

    client.run(os.environ['DISCORD_APIKEY'])
    
# Stat number codes - 0: Not a stat, 1: PvP/PvE aggregate, 2: Medal
def validate(player, content):
    statList = content.split(" ")[1:]
    stat = statList[0]
    trackCode = 0
    if stat in statDict.keys():
        trackCode = 1
    elif stat in medalDict.keys():
        trackCode = 2
    elif stat[:-2] in medalDict.keys() and stat[-2:] == "pg":
        trackCode = 3
        stat = stat[:-2]
    players = []
    isValid = (trackCode != 0)
    if len(statList) > 1:
        isVs = statList[1] == "vs"
        players = statList[2:]
        if players == ["all"]:
            players = playerList
        areValidPlayers = [player in playerList for player in players]
        isValid = (trackCode != 0) and isVs and (False not in areValidPlayers)
    return (isValid, players, trackCode, stat)

def validateClanStat(player, content):
    stat = content.split(" ")[1]
    trackCode = 0
    if stat in statDict.keys():
        trackCode = 1
    elif stat in medalDict.keys():
        trackCode = 2
    elif stat[:-2] in medalDict.keys() and stat[-2:] == "pg":
        trackCode = 3
        stat = stat[:-2]
    isValidPlayer = player in playerList
    playerName = ""
    if isValidPlayer:
        playerName = player
    return ((trackCode != 0), playerName, trackCode, stat)
    
def singleStatRequest(player, code, stat):
    """Actually retrieves the stat and returns the stat info in an embed"""
    session = Session()
    message = ""
    if code == 1:
        (table, col, message) = statDict[stat]
        columns = [col]
        res = session.query(*(getattr(table, column) for column in columns), Account.display_name).join(Account).filter(Account.display_name == player).first()
        #Returns a tuple containing the stat, but only the first element is defined for some reason.
        num = truncateDecimals(res[0])
        name = res[1]
    elif code == 2 or code == 3:
        (table, col, message) = medalDict[stat]
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
    #em = discord.Embed(title = f"{author}{message}{result}", colour=0xADD8E6)
    em = f"```{message} for {name}: {num}```"
    return em

def multiStatRequest(players, code, stat):
    session = Session()
    data = []
    if code == 1:
        (table, col, message) = statDict[stat]
        columns = [col]
        res = session.query(*(getattr(table, column) for column in columns), Account.display_name).join(Account).filter(Account.display_name.in_(players)).order_by(Account.display_name).all()
        data = [(item[1], truncateDecimals(item[0])) for item in res if item[0] is not None]
    elif code == 2 or code == 3:
        (table, col, message) = medalDict[stat]
        columns = [col]
        res = session.query(func.sum(*(getattr(table, column) for column in columns)), Account.display_name).join(Account).filter(Account.display_name.in_(players)).group_by(AccountMedals.id).order_by(Account.display_name).all()
        data = [(item[1], truncateDecimals(item[0])) for item in res if item[0] is not None]
        if code == 3:
            numActivities = session.query(PvPAggregate.activitiesEntered).join(Account).filter(Account.display_name.in_(players)).order_by(Account.display_name).all()
            data = [(res[i][1], truncateDecimals(float(res[i][0])/numActivities[i][0])) for i in range(len(res)) if res[i][0] is not None]
    data = sorted(data, key=lambda x: x[1], reverse=True)
    if (code == 2 or code == 3) and message != "Activities Entered" and message != "Total Number of Medals" and message != "Total Medal Score":
        message = f"Total {message} Medals"
    em = discord.Embed(title = f"{message}", colour=0xADD8E6)
    if len(data) > 10:
        data = data[:9]
    for (name, num) in data:
        em.add_field(name=name, value=num)
    return em

def clanGraphRequest(player, code, stat):
    session = Session()
    rawdata = []
    message = ""
    if code == 1:
        (table, col, message) = statDict[stat]
        columns = [col]
        res = session.query(*(getattr(table, column) for column in columns), Account.display_name).join(Account).all()
        rawdata = [(item[1], truncateDecimals(item[0])) for item in res if item[0] is not None]
    elif code == 2 or code == 3:
        (table, col, message) = medalDict[stat]
        columns = [col]
        res = session.query(func.sum(*(getattr(table, column) for column in columns)), Account.display_name).join(Account).group_by(AccountMedals.id).all()
        rawdata = [(item[1], truncateDecimals(item[0])) for item in res if item[0] is not None]
        if code == 3:
            numActivities = session.query(PvPAggregate.activitiesEntered, Account.display_name).join(Account).all()
            #Need to associate numActivities with the correct username
            rawdata = [(item[1], truncateDecimals(item[0])/float(activity[0])) for item in res for activity in numActivities if item[1] == activity[1] and item[0] is not None and activity[0] is not None]
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
    index = np.arange(len(objects))
    plt.bar(index, values, alpha=0.4, color='b', align='center')
    plt.xlabel("Guardians")
    plt.ylabel(f"{message}")
    plt.title(f"Clan {message} Comparison")
    plt.xticks(index, objects)
    fig.autofmt_xdate()
    plt.tight_layout()
    plt.savefig('./Figures/hist.png')

def lightLevelRequest(player):
    """Retrieves the character light levels of a player"""
    session = Session()
    data = session.query(Character.light_level, ClassReference.class_name).join(Account).join(ClassReference, and_(ClassReference.id==Character.class_hash)).filter(Account.display_name == player).all()
    return data

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

def timeLeft():
    release = datetime.date(2017,9,6)
    today = datetime.date.today()
    untilRelease = str((release-today).days)
    output = "There are "+untilRelease+" days until release!"
    return output
