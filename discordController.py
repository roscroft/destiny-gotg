#!/usr/bin/python3.6
import os, re, sys
import discord, asyncio
from datetime import datetime
from destinygotg import Session, loadConfig
from initdb import PvPTotal, PvETotal, PvPAverage, PvEAverage, Base, Discord, Account, MedalsCharacter
from sqlalchemy import exists, desc, func
from decimal import *
import numpy as np
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt; plt.rcdefaults()

#playerList = [item[0] for item in Session().query(Account.display_name).all()]

statDict = { "kd"           :(PvPTotal, "killsDeathsRatio", "Kill/Death Ratio")
            ,"kda"          :(PvPTotal, "killsDeathsAssists", "Kill/Assists/Death Ratio")
            ,"wl"           :(PvPTotal, "winLossRatio", "Win/Loss Ratio")
            ,"bgs"          :(PvPTotal, "bestSingleGameScore", "Best Single Game Score")
            ,"lks"          :(PvPTotal, "longestKillSpree", "Longest Kill Spree")
            ,"suicides"     :(PvPTotal, "suicides", "Total Number of Suicides")
            ,"spg"          :(PvPAverage, "suicides", "Suicides per Game")
            ,"mk"           :(PvPTotal, "bestSingleGameKills", "Best Single Game Kills")
            ,"kills"        :(PvPTotal, "kills", "Total Number of Kills")
            ,"kpg"          :(PvPAverage, "kills", "Kills per Game")
            ,"deaths"       :(PvPTotal, "deaths", "Total Number of Deaths")
            ,"dpg"          :(PvPAverage, "deaths", "Deaths per Game")
            ,"assists"      :(PvPTotal, "assists", "Total Number of Assists")
            ,"apg"          :(PvPAverage, "assists", "Assists Per Game")
            ,"cr"           :(PvPTotal, "combatRating", "Combat Rating")
            ,"pkills"       :(PvPTotal, "precisionKills", "Total Number of Precision Kills")
            ,"score"        :(PvPTotal, "score", "Total score")
            ,"scpg"         :(PvPAverage, "score", "Score per Game")
            ,"crucibletime" :(PvPTotal, "secondsPlayed", "Total Seconds in the Crucible")
            ,"akills"       :(PvPTotal, "abilityKills", "Total Number of Ability Kills")
            ,"akpg"         :(PvPAverage, "abilityKills", "Ability Kills per Game")
            ,"games"        :(PvPTotal, "activitiesEntered", "Total Number of Activities Entered")
            ,"wins"         :(PvPTotal, "activitiesWon", "Total Number of Activities Won")
            ,"lsl"          :(PvPTotal, "longestSingleLife", "Longest Single Life")
            }

medalDict = { "activities"        :(MedalsCharacter, "activitiesEntered", "Activities Entered")
             ,"totalmedals"       :(MedalsCharacter, "allMedalsEarned", "Total Number of Medals")
             ,"totalscore"        :(MedalsCharacter, "allMedalsScore", "Total Medal Score")
             ,"stormbringer"      :(MedalsCharacter, "medalsAbilityArcLightningKillMulti", "Storm Bringer")
             ,"wayofthegun"       :(MedalsCharacter, "medalsAbilityGhostGunKillMulti", "Way of the Gun")
             ,"cryhavoc"          :(MedalsCharacter, "medalsAbilityHavocKillMulti", "Cry Havoc")
             ,"spacemagic"        :(MedalsCharacter, "medalsAbilityNovaBombKillMulti", "Space Magic")
             ,"scorchedearth"     :(MedalsCharacter, "medalsAbilityRadianceGrenadeKillMulti", "Scorched Earth")
             ,"gutted"            :(MedalsCharacter, "medalsAbilityShadowStrikeKillMulti", "Gutted")
             ,"hammerandtongs"    :(MedalsCharacter, "medalsAbilityThermalHammerKillMulti", "Hammer and Tongs")
             ,"wildhunt"          :(MedalsCharacter, "medalsAbilityVoidBowKillMulti", "Wild Hunt")
             ,"blastshield"       :(MedalsCharacter, "medalsAbilityWardDeflect", "Blast Shield")
             ,"objectivelycorrect":(MedalsCharacter, "medalsActivityCompleteControlMostCaptures", "Objectively Correct")
             ,"thecycle"          :(MedalsCharacter, "medalsActivityCompleteCycle", "The Cycle")
             ,"unbroken"          :(MedalsCharacter, "medalsActivityCompleteDeathless", "Mark of the Unbroken")
             ,"onthebrightside"   :(MedalsCharacter, "medalsActivityCompleteHighestScoreLosing", "On the Bright Side...")
             ,"thebestaround"     :(MedalsCharacter, "medalsActivityCompleteHighestScoreWinning", "The Best... Around")
             ,"lonewolf"          :(MedalsCharacter, "medalsActivityCompleteLonewolf", "Lone Wolf")
             ,"saboteur"          :(MedalsCharacter, "medalsActivityCompleteSalvageMostCancels", "Saboteur")
             ,"shutout"           :(MedalsCharacter, "medalsActivityCompleteSalvageShutout", "Shutout")
             ,"perfectrunner"     :(MedalsCharacter, "medalsActivityCompleteSingularityPerfectRunner", "Perfect Runner")
             ,"decisivevictory"   :(MedalsCharacter, "medalsActivityCompleteVictoryBlowout", "Decisive Victory")
             ,"victory"           :(MedalsCharacter, "medalsActivityCompleteVictory", "Victory")
             ,"trialbyfire"       :(MedalsCharacter, "medalsActivityCompleteVictoryElimination", "Trial by Fire")
             ,"bulletproof"       :(MedalsCharacter, "medalsActivityCompleteVictoryEliminationPerfect", "Bulletproof")
             ,"annihilation"      :(MedalsCharacter, "medalsActivityCompleteVictoryEliminationShutout", "Annihilation")
             ,"clutch"            :(MedalsCharacter, "medalsActivityCompleteVictoryExtraLastSecond", "Clutch")
             ,"comeback"          :(MedalsCharacter, "medalsActivityCompleteVictoryLastSecond", "Comeback")
             ,"nomercy"           :(MedalsCharacter, "medalsActivityCompleteVictoryMercy", "No Mercy")
             ,"sumofalltears"     :(MedalsCharacter, "medalsActivityCompleteVictoryRumbleBlowout", "Sum of all Tears")
             ,"aloneatthetop"     :(MedalsCharacter, "medalsActivityCompleteVictoryRumble", "Alone at the Top")
             ,"wontbebeat"        :(MedalsCharacter, "medalsActivityCompleteVictoryRumbleLastSecond", "Won't be Beat")
             ,"heartbreaker"      :(MedalsCharacter, "medalsActivityCompleteVictoryRumbleSuddenDeath", "Heartbreaker")
             ,"zerohour"          :(MedalsCharacter, "medalsActivityCompleteVictorySuddenDeath", "Zero Hour")
             ,"avenger"           :(MedalsCharacter, "medalsAvenger", "Avenger")
             ,"medic"             :(MedalsCharacter, "medalsBuddyResurrectionMulti", "Medic!")
             ,"angeloflight"      :(MedalsCharacter, "medalsBuddyResurrectionSpree", "Angel of Light")
             ,"narrowescape"      :(MedalsCharacter, "medalsCloseCallTalent", "Narrow Escape")
             ,"backinaction"      :(MedalsCharacter, "medalsComebackKill", "Back in Action")
             ,"domination"        :(MedalsCharacter, "medalsDominationKill", "Domination")
             ,"hattrick"          :(MedalsCharacter, "medalsDominionZoneCapturedSpree", "Hat Trick")
             ,"defender"          :(MedalsCharacter, "medalsDominionZoneDefenseKillSpree", "Defender")
             ,"atanycost"         :(MedalsCharacter, "medalsDominionZoneOffenseKillSpree", "At any Cost")
             ,"neversaydie"       :(MedalsCharacter, "medalsEliminationLastStandKill", "Never Say Die")
             ,"fromthebrink"      :(MedalsCharacter, "medalsEliminationLastStandRevive", "From the Brink")
             ,"ace"               :(MedalsCharacter, "medalsEliminationWipeQuick", "Ace")
             ,"wreckingball"      :(MedalsCharacter, "medalsEliminationWipeSolo", "Wrecking Ball")
             ,"firstblood"        :(MedalsCharacter, "medalsFirstBlood", "First Blood")
             ,"uprising"          :(MedalsCharacter, "medalsFirstPlaceKillSpree", "Uprising")
             ,"getitoff"          :(MedalsCharacter, "medalsGrenadeKillStick", "Get it Off!")
             ,"hazardpay"         :(MedalsCharacter, "medalsHazardKill", "Hazard Pay")
             ,"iseeyou"           :(MedalsCharacter, "medalsHunterKillInvisible", "I See You")
             ,"unsunghero"        :(MedalsCharacter, "medalsKillAssistSpree", "Unsung Hero")
             ,"enemyofmyenemy"    :(MedalsCharacter, "medalsKillAssistSpreeFfa", "Enemy of my Enemy")
             ,"bullseye"          :(MedalsCharacter, "medalsKillHeadshot", "Bullseye")
             ,"enforcer"          :(MedalsCharacter, "medalsKilljoy", "Enforcer")
             ,"endoftheline"      :(MedalsCharacter, "medalsKilljoyMega", "End of the Line")
             ,"doubledown"        :(MedalsCharacter, "medalsKillMulti2", "Double Down")
             ,"tripledown"        :(MedalsCharacter, "medalsKillMulti3", "Triple Down")
             ,"breaker"           :(MedalsCharacter, "medalsKillMulti4", "Breaker")
             ,"slayer"            :(MedalsCharacter, "medalsKillMulti5", "Slayer")
             ,"reaper"            :(MedalsCharacter, "medalsKillMulti6", "Reaper")
             ,"seventhcolumn"     :(MedalsCharacter, "medalsKillMulti7", "Seventh Column")
             ,"postmortem"        :(MedalsCharacter, "medalsKillPostmortem", "Postmortem")
             ,"merciless"         :(MedalsCharacter, "medalsKillSpree1", "Merciless")
             ,"relentless"        :(MedalsCharacter, "medalsKillSpree2", "Relentless")
             ,"reignofterror"     :(MedalsCharacter, "medalsKillSpree3", "Reign of Terror")
             ,"weranoutofmedals"  :(MedalsCharacter, "medalsKillSpreeAbsurd", "We Ran Out of Medals")
             ,"phantom"           :(MedalsCharacter, "medalsKillSpreeNoDamage", "Phantom")
             ,"stickaround"       :(MedalsCharacter, "medalsMeleeKillHunterThrowingKnifeHeadshot", "Stick Around")
             ,"payback"           :(MedalsCharacter, "medalsPaybackKill", "Payback")
             ,"andstaydown"       :(MedalsCharacter, "medalsRadianceShutdown", "...And Stay Down!")
             ,"overwatch"         :(MedalsCharacter, "medalsRescue", "Overwatch")
             ,"disruption"        :(MedalsCharacter, "medalsSalvageProbeCanceled", "Disruption")
             ,"salvagecrew"       :(MedalsCharacter, "medalsSalvageProbeCompleteSpree", "Salvage Crew")
             ,"improbeable"       :(MedalsCharacter, "medalsSalvageProbeDefenseKill", "Im-probe-able")
             ,"cleansweep"        :(MedalsCharacter, "medalsSalvageProbeOffenseKillMulti", "Clean Sweep")
             ,"relichunter"       :(MedalsCharacter, "medalsSalvageZoneCapturedSpree", "Relic Hunter")
             ,"unstoppableforce"  :(MedalsCharacter, "medalsSingularityFlagCaptureMulti", "Unstoppable Force")
             ,"denied"            :(MedalsCharacter, "medalsSingularityFlagHolderKilledClose", "Denied")
             ,"immovableobject"   :(MedalsCharacter, "medalsSingularityFlagHolderKilledMulti", "Immovable Object")
             ,"clearapath"        :(MedalsCharacter, "medalsSingularityRunnerDefenseMulti", "Clear a Path")
             ,"afistfulofcrests"  :(MedalsCharacter, "medalsSupremacy", "A Fistful of Crests...")
             ,"forafewcrestsmore" :(MedalsCharacter, "medalsSupremacyConfirmStreakLarge", "And For a Few Crests More")
             ,"honorguard"        :(MedalsCharacter, "medalsSupremacyDenyMulti", "Honor Guard")
             ,"mineallmine"       :(MedalsCharacter, "medalsSupremacyMostConfirms", "Mine! All Mine!")
             ,"handsoff"          :(MedalsCharacter, "medalsSupremacyMostDenies", "Hands Off")
             ,"illdoitmyself"     :(MedalsCharacter, "medalsSupremacyMostSelfConfirms", "I'll Do It Myself")
             ,"pickupthepieces"   :(MedalsCharacter, "medalsSupremacyMulti", "Pick Up the Pieces")
             ,"nevergonnagetit"   :(MedalsCharacter, "medalsSupremacyNeverCollected", "Never Gonna Get It")
             ,"nevermindfoundit"  :(MedalsCharacter, "medalsSupremacySelfDeny", "Never Mind, Found It")
             ,"lockdown"          :(MedalsCharacter, "medalsTeamDominationHold1m", "Lockdown")
             ,"strengthofthewolf" :(MedalsCharacter, "medalsTeamKillSpree", "Strength of the Wolf")
             ,"unknown"           :(MedalsCharacter, "medalsUnknown", "Unknown")
             ,"gunner"            :(MedalsCharacter, "medalsVehicleFotcTurretKillSpree", "Gunner")
             ,"bulldozer"         :(MedalsCharacter, "medalsVehicleInterceptorKillSplatter", "Bulldozer")
             ,"chariotoffire"     :(MedalsCharacter, "medalsVehicleInterceptorKillSpree", "Chariot of Fire")
             ,"skewered"          :(MedalsCharacter, "medalsVehiclePikeKillSplatter", "Skewered")
             ,"fallenangel"       :(MedalsCharacter, "medalsVehiclePikeKillSpree", "Fallen Angel")
             ,"neverspeakofthis"  :(MedalsCharacter, "medalsVehicleSparrowKillSplatter", "Never Speak of This Again")
             ,"automatic"         :(MedalsCharacter, "medalsWeaponAutoRifleKillSpree", "Automatic")
             ,"masterblaster"     :(MedalsCharacter, "medalsWeaponFusionRifleKillSpree", "Master Blaster")
             ,"deadmanshand"      :(MedalsCharacter, "medalsWeaponHandCannonHeadshotSpree", "Dead Man's Hand")
             ,"machinelord"       :(MedalsCharacter, "medalsWeaponMachineGunKillSpree", "Machine Lord")
             ,"fingeronthepulse"  :(MedalsCharacter, "medalsWeaponPulseRifleKillSpree", "Finger on the Pulse")
             ,"splashdamage"      :(MedalsCharacter, "medalsWeaponRocketLauncherKillSpree", "Splash Damage")
             ,"scoutshonor"       :(MedalsCharacter, "medalsWeaponScoutRifleKillSpree", "Scout's Honor")
             ,"buckshotbruiser"   :(MedalsCharacter, "medalsWeaponShotgunKillSpree", "Buckshot Bruiser")
             ,"sidekick"          :(MedalsCharacter, "medalsWeaponSidearmKillSpree", "Sidekick")
             ,"marksman"          :(MedalsCharacter, "medalsWeaponSniperRifleHeadshotSpree", "Marksman")
             ,"swordatagunfight"  :(MedalsCharacter, "medalsWeaponSwordKillSpree", "Sword at a Gun Fight")
             ,"nailinthecoffin"   :(MedalsCharacter, "medalsWinningScore", "Nail in the Coffin")
             ,"bline"             :(MedalsCharacter, "medalsZoneCapturedBInitial", "B-Line")
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
            destinyName = session.query(Account.display_name).filter(Account.discord_id == discId).first()[0]
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
        session.query(Account).filter(Account.display_name == destName).update({"discord_id":discordAuthor.id})
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
    elif code == 2:
        (table, col, message) = medalDict[stat]
        columns = [col]
        res = session.query(func.sum(*(getattr(table, column) for column in columns))).join(Account).filter(Account.display_name == player).group_by(MedalsCharacter.membership_id).first()
        num = res[0]
        name = player
        if message != "Activities Entered" and message != "Total Number of Medals" and message != "Total Medal Score":
            message = f"Total {message} Medals"
    elif code == 3:
        (table, col, message) = medalDict[stat]
        columns = [col]
        res = session.query(func.sum(*(getattr(table, column) for column in columns))).join(Account).filter(Account.display_name == player).group_by(MedalsCharacter.membership_id).first()
        num = float(res[0])
        denominator = session.query(PvPTotal.activitiesEntered).join(Account).filter(Account.display_name == player).first()
        act = denominator[0]
        num = num/act
        name = player
        if message != "Activities Entered" and message != "Total Number of Medals" and message != "Total Medal Score":
            message = f"{message} Medals per Game"
        else:
            message = f"{message} per Game"
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
    elif code == 2:
        (table, col, message) = medalDict[stat]
        columns = [col]
        res = session.query(func.sum(*(getattr(table, column) for column in columns)), Account.display_name).join(Account).filter(Account.display_name.in_(players)).group_by(MedalsCharacter.membership_id).order_by(Account.display_name).all()
        data = [(item[1], truncateDecimals(item[0])) for item in res if item[0] is not None]
    elif code == 3:
        (table, col, message) = medalDict[stat]
        columns = [col]
        res = session.query(func.sum(*(getattr(table, column) for column in columns)), Account.display_name).join(Account).filter(Account.display_name.in_(players)).group_by(MedalsCharacter.membership_id).order_by(Account.display_name).all()
        numActivities = session.query(PvPTotal.activitiesEntered).join(Account).filter(Account.display_name.in_(players)).order_by(Account.display_name).all()
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
    elif code == 2:
        (table, col, message) = medalDict[stat]
        columns = [col]
        res = session.query(func.sum(*(getattr(table, column) for column in columns)), Account.display_name).join(Account).group_by(MedalsCharacter.membership_id).all()
        rawdata = [(item[1], truncateDecimals(item[0])) for item in res if item[0] is not None]
    elif code == 3:
        (table, col, message) = medalDict[stat]
        
        columns = [col]
        res = session.query(func.sum(*(getattr(table, column) for column in columns)), Account.display_name).join(Account).group_by(MedalsCharacter.membership_id).all()
        numActivities = session.query(PvPTotal.activitiesEntered, Account.display_name).join(Account).all()
        #Need to associate numActivities with the correct username
        rawdata = [(item[1], truncateDecimals(item[0])/float(activity[0])) for item in res for activity in numActivities if item[1] == activity[1] and item[0] is not None and activity[0] is not None]
        print(rawdata)
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
