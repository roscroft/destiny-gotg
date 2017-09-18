from initdb import AccountTotalStats, AccountWeaponStats

def check_players(player_list):
    players_are_valid = [True if player in all_players else False for player in player_list]
    return all(players_are_valid)

def return_info(request, player):
    #Table name, primary keys (id and mode), column name(s), player name(s), message
    #TODO: update this with other modes
    info = request.split(" ")
    command = info[0]
    c_mode = info[1]
    c_stat = info[2]
    multi = False
    if len(info) > 3:
        multi = True
        vs = info[3]
        player_list = info[4:]
    valid_command = c_command in command_dict.keys()
    valid_mode = c_mode in mode_dict.keys()
    valid_stat = c_stat in stat_dict.keys()
    if multi:
        valid_vs = vs == "vs"
        valid_player_list = check_players(player_list)
    if not valid_command:
        print "Invalid command. Try !help for a list of possible commands."
        return None
    elif not valid_mode:
        print f"Invalid mode. Available modes are {mode_dict.keys()}."
        return None
    elif not valid_stat:
        print "Invalid stat. See the #command-list channel for a list of valid stats."
        return None
    if multi:
        elif not valid_vs:
            print "Use 'vs' without quotes to compare stats with others."
            return None
        elif not valid_player_list:
            print "One or more of the players you listed is not in the clan, or is not spelled proPerly."
            return None
    return_dict = {}
    return_dict["mode"] = mode_dict[c_mode]
    return_dict["table"] = stat_dict[c_stat][table]
    return_dict["column"] = stat_dict[c_stat][column]
    return_dict["message"] = stat_dict[c_stat][message]
    return_dict["players"] = [player]
    if multi:
        return_dict["players"] = players + player_list
    return return_dict

mode_dict = {"pvp": "allPvP"
            ,"strike": "allStrikes"
            ,"story": "story"
            ,"patrol": "patrol"}

stat_dict = {"clears": {"table": AccountTotalStats, "column": "activitiesCleared", "message": "Total Activities Cleared"}
            ,"games": {"table": AccountTotalStats, "column": "activitiesEntered", "message": "Total Activities Entered"}
            ,"wins": {"table": AccountTotalStats, "column": "activitiesWon", "message": "Total Activities Won"}
            ,"adventures": {"table": AccountTotalStats, "column": "adventuresCompleted", "message": "Total Activities Won"}
            ,"participants": {"table": AccountTotalStats, "column": "allParticipantsCount", "message": "Total Participant Count"}
            ,"totalscore": {"table": AccountTotalStats, "column": "allParticipantsScore", "message": "Total Participant Score"}
            ,"totaltime": {"table": AccountTotalStats, "column": "allParticipantsTimePlayed", "message": "Total Participant Playtime"}
            ,"assists": {"table": AccountTotalStats, "column": "assists", "message": "Total Assists"}
            ,"avgdeathdist": {"table": AccountTotalStats, "column": "averageDeathDistance", "message": "Average Death Distance"}
            ,"avgkilldist": {"table": AccountTotalStats, "column": "averageKillDistance", "message": "Average Kill Distance"}
            ,"avglife": {"table": AccountTotalStats, "column": "averageLifespan", "message": "Average Lifespan"}
            ,"scorePerkill": {"table": AccountTotalStats, "column": "averageScorePerKill", "message": "Average Score Per Kill"}
            ,"scorePerlife": {"table": AccountTotalStats, "column": "averageScorePerLife", "message": "Average Score Per Life"}
            ,"bgk": {"table": AccountTotalStats, "column": "bestSingleGameKills", "message": "Best Single Game Kills"}
            ,"bgs": {"table": AccountTotalStats, "column": "bestSingleGameScore", "message": "Best Single Game Score"}
            ,"cbr": {"table": AccountTotalStats, "column": "combatRating", "message": "Combat Rating"}
            ,"deaths": {"table": AccountTotalStats, "column": "deaths", "message": "Total Deaths"}
            ,"fastestcomp": {"table": AccountTotalStats, "column": "fastestCompletionMs", "message": "Fastest Completion (ms)"}
            ,"heroics": {"table": AccountTotalStats, "column": "heroicPublicEventsCompleted", "message": "Heroic Public Events Completed"}
            ,"maxlevel": {"table": AccountTotalStats, "column": "highestCharacterLevel", "message": "Highest Character Level"}
            ,"maxlight": {"table": AccountTotalStats, "column": "highestLightLevel", "message": "Highest Light Level"}
            ,"kills": {"table": AccountTotalStats, "column": "kills", "message": "Total Kills"}
            ,"kda": {"table": AccountTotalStats, "column": "killsDeathsAssists", "message": "Kills Deaths Assists Ratio"}
            ,"kd": {"table": AccountTotalStats, "column": "killsDeathsRatio", "message": "Kills Deaths Ratio"}
            ,"lkd": {"table": AccountTotalStats, "column": "longestKillDistance", "message": "Longest Kill Distance"}
            ,"lks": {"table": AccountTotalStats, "column": "longestKillSpree", "message": "Longest Kill Spree"}
            ,"lsl": {"table": AccountTotalStats, "column": "longestSingleLife", "message": "Longest Single Life"}
            ,"mpk": {"table": AccountTotalStats, "column": "mostPrecisionKills", "message": "Most Precision Kills"}
            ,"obj": {"table": AccountTotalStats, "column": "objectivesCompleted", "message": "Objectives Completed"}
            ,"orbdrop": {"table": AccountTotalStats, "column": "orbsDropped", "message": "Total Orbs Dropped"}
            ,"orbgather": {"table": AccountTotalStats, "column": "orbsGathered", "message": "Total Orbs Gathered"}
            ,"publics": {"table": AccountTotalStats, "column": "publicEventsCompleted", "message": "Public Events Completed"}
            ,"precisions": {"table": AccountTotalStats, "column": "precisionKills", "message": "Total Precision Kills"}
            ,"timeleft": {"table": AccountTotalStats, "column": "remainingTimeAfterQuitSeconds", "message": "Time Left After Quitting (s)"}
            ,"resPerformed": {"table": AccountTotalStats, "column": "resurrectionsPerformed", "message": "Total Resurrections Performed"}
            ,"resreceived": {"table": AccountTotalStats, "column": "resurrectionsReceived", "message": "Total Resurrections Received"}
            ,"score": {"table": AccountTotalStats, "column": "score", "message": "Total Score"}
            ,"time": {"table": AccountTotalStats, "column": "secondsPlayed", "message": "Time Played (s)"}
            ,"suicides": {"table": AccountTotalStats, "column": "suicides", "message": "Total Suicides"}
            ,"teamscore": {"table": AccountTotalStats, "column": "teamScore", "message": "Total Team Score"}
            ,"activitytime": {"table": AccountTotalStats, "column": "totalActivityDurationSeconds", "message": "Total Activity Time (s)"}
            ,"deathdist": {"table": AccountTotalStats, "column": "totalDeathDistance", "message": "Total Death Distance"}
            ,"killdist": {"table": AccountTotalStats, "column": "totalKillDistance", "message": "Total Kill Distance"}
            ,"bestweapon": {"table": AccountTotalStats, "column": "weaponBestType", "message": "Best Weapon Type"}
            ,"wlr": {"table": AccountTotalStats, "column": "winLossRatio", "message": "Win Loss Ratio"}
            ,"akillspg": {"table": AccountTotalStats, "column": "abilityKillspg", "message": "Ability Kills Per Game"}
            ,"apg": {"table": AccountTotalStats, "column": "assistspg", "message": "Assists Per Game"}
            ,"dpg": {"table": AccountTotalStats, "column": "deathspg", "message": "Deaths Per Game"}
            ,"kpg": {"table": AccountTotalStats, "column": "killspg", "message": "Kills Per Game"}
            ,"objpg": {"table": AccountTotalStats, "column": "objectivesCompletedpg", "message": "Objectives Completed Per Game"}
            ,"odpg": {"table": AccountTotalStats, "column": "orbsDroppedpg", "message": "Orbs Dropped Per Game"}
            ,"ogpg": {"table": AccountTotalStats, "column": "orbsGatheredpg", "message": "Orbs Gathered Per Game"}
            ,"pkpg": {"table": AccountTotalStats, "column": "precisionKillspg", "message": "Precision Kills Per Game"}
            ,"pecpg": {"table": AccountTotalStats, "column": "publicEventsCompletedpg", "message": "Public Events Completed Per Game"}
            ,"pejpg": {"table": AccountTotalStats, "column": "publicEventsJoinedpg", "message": "Public Events Joined Per Game"}
            ,"timeleftpg": {"table": AccountTotalStats, "column": "remainingTimeAfterQuitSecondspg", "message": "Time Left After Quitting (s) Per Game"}
            ,"resppg": {"table": AccountTotalStats, "column": "resurrectionsPerformedpg", "message": "Resurrections Performed Per Game"}
            ,"resrpg": {"table": AccountTotalStats, "column": "resurrectionsReceivedpg", "message": "Resurrections Received Per Game"}
            ,"scpg": {"table": AccountTotalStats, "column": "scorepg", "message": "Score Per Game"}
            ,"timepg": {"table": AccountTotalStats, "column": "secondsPlayedpg", "message": "Seconds Played Per Game"}
            ,"spg": {"table": AccountTotalStats, "column": "suicidespg", "message": "Suicides Per Game"}
            ,"tscpg": {"table": AccountTotalStats, "column": "teamScorepg", "message": "Team Score Per Game"}
            ,"acttimepergame": {"table": AccountTotalStats, "column": "totalActivityDurationSecondspg", "message": "Total Activity Time (s) Per Game"}
            ,"zcpg": {"table": AccountTotalStats, "column": "zonesCapturedpg", "message": "Zones Captured Per Game"}
            ,"znpg": {"table": AccountTotalStats, "column": "zonesNeutralizedpg", "message": "Zones Neutralized Per Game"}
            ,"akills": {"table": AccountWeaponStats, "column": "weaponKillsAbility", "message": ""}
            ,"arkills": {"table": AccountWeaponStats, "column": "weaponKillsAutoRifle", "message": ""}
            ,"frkills": {"table": AccountWeaponStats, "column": "weaponKillsFusionRifle", "message": ""}
            ,"gkills": {"table": AccountWeaponStats, "column": "weaponKillsGrenade", "message": ""}
            ,"glkills": {"table": AccountWeaponStats, "column": "weaponKillsGrenadeLauncher", "message": ""}
            ,"hckills": {"table": AccountWeaponStats, "column": "weaponKillsHandCannon", "message": ""}
            ,"mgkills": {"table": AccountWeaponStats, "column": "weaponKillsMachinegun", "message": ""}
            ,"mkills": {"table": AccountWeaponStats, "column": "weaponKillsMelee", "message": ""}
            ,"arpkillpct": {"table": AccountWeaponStats, "column": "weaponKillsPrecisionKillsAutoRifle", "message": ""}
            ,"frpkillpct": {"table": AccountWeaponStats, "column": "weaponKillsPrecisionKillsFusionRifle", "message": ""}
            ,"gpkillpct": {"table": AccountWeaponStats, "column": "weaponKillsPrecisionKillsGrenade", "message": ""}
            ,"glpkillpct": {"table": AccountWeaponStats, "column": "weaponKillsPrecisionKillsGrenadeLauncher", "message": ""}
            ,"hcpkillpct": {"table": AccountWeaponStats, "column": "weaponKillsPrecisionKillsHandCannon", "message": ""}
            ,"mgpkillpct": {"table": AccountWeaponStats, "column": "weaponKillsPrecisionKillsMachinegun", "message": ""}
            ,"mpkillpct": {"table": AccountWeaponStats, "column": "weaponKillsPrecisionKillsMelee", "message": ""}
            ,"prpkillpct": {"table": AccountWeaponStats, "column": "weaponKillsPrecisionKillsPulseRifle", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponKillsPrecisionKillsRelic", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponKillsPrecisionKillsRocketLauncher", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponKillsPrecisionKillsScoutRifle", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponKillsPrecisionKillsShotgun", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponKillsPrecisionKillsSideArm", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponKillsPrecisionKillsSniper", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponKillsPrecisionKillsSubmachinegun", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponKillsPrecisionKillsSuper", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponKillsPulseRifle", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponKillsRelic", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponKillsRocketLauncher", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponKillsScoutRifle", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponKillsShotgun", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponKillsSideArm", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponKillsSniper", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponKillsSubmachinegun", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponKillsSuper", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponKillsSword", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsAutoRifle", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsFusionRifle", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsGrenade", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsGrenadeLauncher", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsHandCannon", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsMachinegun", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsMelee", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsPulseRifle", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsRelic", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsRocketLauncher", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsScoutRifle", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsShotgun", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsSideArm", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsSniper", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsSubmachinegun", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsSuper", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponKillsAbilitypg", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponKillsAutoRiflepg", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponKillsFusionRiflepg", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponKillsGrenadepg", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponKillsGrenadeLauncherpg", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponKillsHandCannonpg", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponKillsMachinegunpg", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponKillsMeleepg", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponKillsPulseRiflepg", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponKillsRelicpg", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponKillsRocketLauncherpg", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponKillsScoutRiflepg", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponKillsShotgunpg", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponKillsSideArmpg", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponKillsSniperpg", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponKillsSubmachinegunpg", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponKillsSuperpg", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponKillsSwordpg", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsAutoRiflepg", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsFusionRiflepg", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsGrenadepg", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsGrenadeLauncherpg", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsHandCannonpg", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsMachinegunpg", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsMeleepg", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsPulseRiflepg", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsRelicpg", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsRocketLauncherpg", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsScoutRiflepg", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsShotgunpg", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsSideArmpg", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsSniperpg", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsSubmachinegunpg", "message": ""}
            ,"": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsSuperpg", "message": ""}




















# medal_dict = { "activities": (AccountMedalStats, "activitiesEntered", "Activities Entered")
#              ,"totalmedals": (AccountMedalStats, "allMedalsEarned", "Total Number of Medals")
#              ,"totalscore": (AccountMedalStats, "allMedalsScore", "Total Medal Score")
#              ,"stormbringer": (AccountMedalStats, "medalsAbilityArcLightningKillMulti", "Storm Bringer")
#              ,"wayofthegun": (AccountMedalStats, "medalsAbilityGhostGunKillMulti", "Way of the Gun")
#              ,"cryhavoc": (AccountMedalStats, "medalsAbilityHavocKillMulti", "Cry Havoc")
#              ,"spacemagic": (AccountMedalStats, "medalsAbilityNovaBombKillMulti", "Space Magic")
#              ,"scorchedearth": (AccountMedalStats, "medalsAbilityRadianceGrenadeKillMulti", "Scorched Earth")
#              ,"gutted": (AccountMedalStats, "medalsAbilityShadowStrikeKillMulti", "Gutted")
#              ,"hammerandtongs": (AccountMedalStats, "medalsAbilityThermalHammerKillMulti", "Hammer and Tongs")
#              ,"wildhunt": (AccountMedalStats, "medalsAbilityVoidBowKillMulti", "Wild Hunt")
#              ,"blastshield": (AccountMedalStats, "medalsAbilityWardDeflect", "Blast Shield")
#              ,"objectivelycorrect":(AccountMedalStats, "medalsActivityCompleteControlMostCaptures", "Objectively Correct")
#              ,"thecycle": (AccountMedalStats, "medalsActivityCompleteCycle", "The Cycle")
#              ,"unbroken": (AccountMedalStats, "medalsActivityCompleteDeathless", "Mark of the Unbroken")
#              ,"onthebrightside": (AccountMedalStats, "medalsActivityCompleteHighestScoreLosing", "On the Bright Side...")
#              ,"thebestaround": (AccountMedalStats, "medalsActivityCompleteHighestScoreWinning", "The Best... Around")
#              ,"lonewolf": (AccountMedalStats, "medalsActivityCompleteLonewolf", "Lone Wolf")
#              ,"saboteur": (AccountMedalStats, "medalsActivityCompleteSalvageMostCancels", "Saboteur")
#              ,"shutout": (AccountMedalStats, "medalsActivityCompleteSalvageShutout", "Shutout")
#              ,"Perfectrunner": (AccountMedalStats, "medalsActivityCompleteSingularityPerfectRunner", "Perfect Runner")
#              ,"decisivevictory": (AccountMedalStats, "medalsActivityCompleteVictoryBlowout", "Decisive Victory")
#              ,"victory": (AccountMedalStats, "medalsActivityCompleteVictory", "Victory")
#              ,"trialbyfire": (AccountMedalStats, "medalsActivityCompleteVictoryElimination", "Trial by Fire")
#              ,"bulletproof": (AccountMedalStats, "medalsActivityCompleteVictoryEliminationPerfect", "Bulletproof")
#              ,"annihilation": (AccountMedalStats, "medalsActivityCompleteVictoryEliminationShutout", "Annihilation")
#              ,"clutch": (AccountMedalStats, "medalsActivityCompleteVictoryExtraLastSecond", "Clutch")
#              ,"comeback": (AccountMedalStats, "medalsActivityCompleteVictoryLastSecond", "Comeback")
#              ,"nomercy": (AccountMedalStats, "medalsActivityCompleteVictoryMercy", "No Mercy")
#              ,"sumofalltears": (AccountMedalStats, "medalsActivityCompleteVictoryRumbleBlowout", "Sum of all Tears")
#              ,"aloneatthetop": (AccountMedalStats, "medalsActivityCompleteVictoryRumble", "Alone at the Top")
#              ,"wontbebeat": (AccountMedalStats, "medalsActivityCompleteVictoryRumbleLastSecond", "Won't be Beat")
#              ,"heartbreaker": (AccountMedalStats, "medalsActivityCompleteVictoryRumbleSuddenDeath", "Heartbreaker")
#              ,"zerohour": (AccountMedalStats, "medalsActivityCompleteVictorySuddenDeath", "Zero Hour")
#              ,"avenger": (AccountMedalStats, "medalsAvenger", "Avenger")
#              ,"medic": (AccountMedalStats, "medalsBuddyResurrectionMulti", "Medic!")
#              ,"angeloflight": (AccountMedalStats, "medalsBuddyResurrectionSpree", "Angel of Light")
#              ,"narrowescape": (AccountMedalStats, "medalsCloseCallTalent", "Narrow Escape")
#              ,"backinaction": (AccountMedalStats, "medalsComebackKill", "Back in Action")
#              ,"domination": (AccountMedalStats, "medalsDominationKill", "Domination")
#              ,"hattrick": (AccountMedalStats, "medalsDominionZoneCapturedSpree", "Hat Trick")
#              ,"defender": (AccountMedalStats, "medalsDominionZoneDefenseKillSpree", "Defender")
#              ,"atanycost": (AccountMedalStats, "medalsDominionZoneOffenseKillSpree", "At any Cost")
#              ,"neversaydie": (AccountMedalStats, "medalsEliminationLastStandKill", "Never Say Die")
#              ,"fromthebrink": (AccountMedalStats, "medalsEliminationLastStandRevive", "From the Brink")
#              ,"ace": (AccountMedalStats, "medalsEliminationWipeQuick", "Ace")
#              ,"wreckingball": (AccountMedalStats, "medalsEliminationWipeSolo", "Wrecking Ball")
#              ,"firstblood": (AccountMedalStats, "medalsFirstBlood", "First Blood")
#              ,"uprising": (AccountMedalStats, "medalsFirstPlaceKillSpree", "Uprising")
#              ,"getitoff": (AccountMedalStats, "medalsGrenadeKillStick", "Get it Off!")
#              ,"hazardpay": (AccountMedalStats, "medalsHazardKill", "Hazard Pay")
#              ,"iseeyou": (AccountMedalStats, "medalsHunterKillInvisible", "I See You")
#              ,"unsunghero": (AccountMedalStats, "medalsKillAssistSpree", "Unsung Hero")
#              ,"enemyofmyenemy": (AccountMedalStats, "medalsKillAssistSpreeFfa", "Enemy of my Enemy")
#              ,"bullseye": (AccountMedalStats, "medalsKillHeadshot", "Bullseye")
#              ,"enforcer": (AccountMedalStats, "medalsKilljoy", "Enforcer")
#              ,"endoftheline": (AccountMedalStats, "medalsKilljoyMega", "End of the Line")
#              ,"doubledown": (AccountMedalStats, "medalsKillMulti2", "Double Down")
#              ,"tripledown": (AccountMedalStats, "medalsKillMulti3", "Triple Down")
#              ,"breaker": (AccountMedalStats, "medalsKillMulti4", "Breaker")
#              ,"slayer": (AccountMedalStats, "medalsKillMulti5", "Slayer")
#              ,"reaPer": (AccountMedalStats, "medalsKillMulti6", "ReaPer")
#              ,"seventhcolumn": (AccountMedalStats, "medalsKillMulti7", "Seventh Column")
#              ,"postmortem": (AccountMedalStats, "medalsKillPostmortem", "Postmortem")
#              ,"merciless": (AccountMedalStats, "medalsKillSpree1", "Merciless")
#              ,"relentless": (AccountMedalStats, "medalsKillSpree2", "Relentless")
#              ,"reignofterror": (AccountMedalStats, "medalsKillSpree3", "Reign of Terror")
#              ,"weranoutofmedals": (AccountMedalStats, "medalsKillSpreeAbsurd", "We Ran Out of Medals")
#              ,"phantom": (AccountMedalStats, "medalsKillSpreeNoDamage", "Phantom")
#              ,"stickaround": (AccountMedalStats, "medalsMeleeKillHunterThrowingKnifeHeadshot", "Stick Around")
#              ,"payback": (AccountMedalStats, "medalsPaybackKill", "Payback")
#              ,"andstaydown": (AccountMedalStats, "medalsRadianceShutdown", "...And Stay Down!")
#              ,"overwatch": (AccountMedalStats, "medalsRescue", "Overwatch")
#              ,"disruption": (AccountMedalStats, "medalsSalvageProbeCanceled", "Disruption")
#              ,"salvagecrew": (AccountMedalStats, "medalsSalvageProbeCompleteSpree", "Salvage Crew")
#              ,"improbeable": (AccountMedalStats, "medalsSalvageProbeDefenseKill", "Im-probe-able")
#              ,"cleansweep": (AccountMedalStats, "medalsSalvageProbeOffenseKillMulti", "Clean Sweep")
#              ,"relichunter": (AccountMedalStats, "medalsSalvageZoneCapturedSpree", "Relic Hunter")
#              ,"unstoppableforce": (AccountMedalStats, "medalsSingularityFlagCaptureMulti", "Unstoppable Force")
#              ,"denied": (AccountMedalStats, "medalsSingularityFlagHolderKilledClose", "Denied")
#              ,"immovableobject": (AccountMedalStats, "medalsSingularityFlagHolderKilledMulti", "Immovable Object")
#              ,"clearapath": (AccountMedalStats, "medalsSingularityRunnerDefenseMulti", "Clear a Path")
#              ,"afistfulofcrests": (AccountMedalStats, "medalsSupremacy", "A Fistful of Crests...")
#              ,"forafewcrestsmore": (AccountMedalStats, "medalsSupremacyConfirmStreakLarge", "And For a Few Crests More")
#              ,"honorguard": (AccountMedalStats, "medalsSupremacyDenyMulti", "Honor Guard")
#              ,"mineallmine": (AccountMedalStats, "medalsSupremacyMostConfirms", "Mine! All Mine!")
#              ,"handsoff": (AccountMedalStats, "medalsSupremacyMostDenies", "Hands Off")
#              ,"illdoitmyself": (AccountMedalStats, "medalsSupremacyMostSelfConfirms", "I'll Do It Myself")
#              ,"pickupthepieces": (AccountMedalStats, "medalsSupremacyMulti", "Pick Up the Pieces")
#              ,"nevergonnagetit": (AccountMedalStats, "medalsSupremacyNeverCollected", "Never Gonna Get It")
#              ,"nevermindfoundit": (AccountMedalStats, "medalsSupremacySelfDeny", "Never Mind, Found It")
#              ,"lockdown": (AccountMedalStats, "medalsTeamDominationHold1m", "Lockdown")
#              ,"strengthofthewolf": (AccountMedalStats, "medalsTeamKillSpree", "Strength of the Wolf")
#              ,"unknown": (AccountMedalStats, "medalsUnknown", "Unknown")
#              ,"gunner": (AccountMedalStats, "medalsVehicleFotcTurretKillSpree", "Gunner")
#              ,"bulldozer": (AccountMedalStats, "medalsVehicleInterceptorKillSplatter", "Bulldozer")
#              ,"chariotoffire": (AccountMedalStats, "medalsVehicleInterceptorKillSpree", "Chariot of Fire")
#              ,"skewered": (AccountMedalStats, "medalsVehiclePikeKillSplatter", "Skewered")
#              ,"fallenangel": (AccountMedalStats, "medalsVehiclePikeKillSpree", "Fallen Angel")
#              ,"neverspeakofthis": (AccountMedalStats, "medalsVehicleSparrowKillSplatter", "Never Speak of This Again")
#              ,"automatic": (AccountMedalStats, "medalsWeaponAutoRifleKillSpree", "Automatic")
#              ,"masterblaster": (AccountMedalStats, "medalsWeaponFusionRifleKillSpree", "Master Blaster")
#              ,"deadmanshand": (AccountMedalStats, "medalsWeaponHandCannonHeadshotSpree", "Dead Man's Hand")
#              ,"machinelord": (AccountMedalStats, "medalsWeaponMachineGunKillSpree", "Machine Lord")
#              ,"fingeronthepulse": (AccountMedalStats, "medalsWeaponPulseRifleKillSpree", "Finger on the Pulse")
#              ,"splashdamage": (AccountMedalStats, "medalsWeaponRocketLauncherKillSpree", "Splash Damage")
#              ,"scoutshonor": (AccountMedalStats, "medalsWeaponScoutRifleKillSpree", "Scout's Honor")
#              ,"buckshotbruiser": (AccountMedalStats, "medalsWeaponShotgunKillSpree", "Buckshot Bruiser")
#              ,"sidekick": (AccountMedalStats, "medalsWeaponSidearmKillSpree", "Sidekick")
#              ,"marksman": (AccountMedalStats, "medalsWeaponSniPerRifleHeadshotSpree", "Marksman")
#              ,"swordatagunfight": (AccountMedalStats, "medalsWeaponSwordKillSpree", "Sword at a Gun Fight")
#              ,"nailinthecoffin": (AccountMedalStats, "medalsWinningScore", "Nail in the Coffin")
#              ,"bline": (AccountMedalStats, "medalsZoneCapturedBInitial", "B-Line")
#              }
