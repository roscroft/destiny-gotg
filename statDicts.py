from initdb import AccountTotalStats, AccountWeaponStats


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
            ,"akills": {"table": AccountWeaponStats, "column": "weaponKillsAbility", "message": "Total Ability Kills"}
            ,"arkills": {"table": AccountWeaponStats, "column": "weaponKillsAutoRifle", "message": "Total Auto Rifle Kills"}
            ,"frkills": {"table": AccountWeaponStats, "column": "weaponKillsFusionRifle", "message": "Total Fusion Rifle Kills"}
            ,"gkills": {"table": AccountWeaponStats, "column": "weaponKillsGrenade", "message": "Total Grenade Kills"}
            ,"glkills": {"table": AccountWeaponStats, "column": "weaponKillsGrenadeLauncher", "message": "Total Grenade Launcher Kills"}
            ,"hckills": {"table": AccountWeaponStats, "column": "weaponKillsHandCannon", "message": "Total Hand Cannon Kills"}
            ,"mgkills": {"table": AccountWeaponStats, "column": "weaponKillsMachinegun", "message": "Total Machine Gun Kills"}
            ,"mkills": {"table": AccountWeaponStats, "column": "weaponKillsMelee", "message": "Total Melee Kills"}
            ,"arpkillpct": {"table": AccountWeaponStats, "column": "weaponKillsPrecisionKillsAutoRifle", "message": "Auto Rifle Precision Kill Percentage"}
            ,"frpkillpct": {"table": AccountWeaponStats, "column": "weaponKillsPrecisionKillsFusionRifle", "message": "Fusion Rifle Precision Kill Percentage"}
            ,"gpkillpct": {"table": AccountWeaponStats, "column": "weaponKillsPrecisionKillsGrenade", "message": "Grenade Precision Kill Percentage"}
            ,"glpkillpct": {"table": AccountWeaponStats, "column": "weaponKillsPrecisionKillsGrenadeLauncher", "message": "Grenade Launcher Precision Kill Percentage"}
            ,"hcpkillpct": {"table": AccountWeaponStats, "column": "weaponKillsPrecisionKillsHandCannon", "message": "Hand Cannon Precision Kill Percentage"}
            ,"mgpkillpct": {"table": AccountWeaponStats, "column": "weaponKillsPrecisionKillsMachinegun", "message": "Machine Gun Precision Kill Percentage"}
            ,"mpkillpct": {"table": AccountWeaponStats, "column": "weaponKillsPrecisionKillsMelee", "message": "Melee Precision Kill Percentage"}
            ,"prpkillpct": {"table": AccountWeaponStats, "column": "weaponKillsPrecisionKillsPulseRifle", "message": "Pulse Rifle Precision Kill Percentage"}
            ,"rpkillpct": {"table": AccountWeaponStats, "column": "weaponKillsPrecisionKillsRelic", "message": "Relic Precision Kill Percentage"}
            ,"rlpkillpct": {"table": AccountWeaponStats, "column": "weaponKillsPrecisionKillsRocketLauncher", "message": "Rocket Launcher Precision Kill Percentage"}
            ,"srpkillpct": {"table": AccountWeaponStats, "column": "weaponKillsPrecisionKillsScoutRifle", "message": "Scout Rifle Precision Kill Percentage"}
            ,"shpkillpct": {"table": AccountWeaponStats, "column": "weaponKillsPrecisionKillsShotgun", "message": "Shotgun Precision Kill Percentage"}
            ,"sapkillpct": {"table": AccountWeaponStats, "column": "weaponKillsPrecisionKillsSideArm", "message": "Sidearm Precision Kill Percentage"}
            ,"snpkillpct": {"table": AccountWeaponStats, "column": "weaponKillsPrecisionKillsSniper", "message": "Sniper Precision Kill Percentage"}
            ,"smgpkillpct": {"table": AccountWeaponStats, "column": "weaponKillsPrecisionKillsSubmachinegun", "message": "Submachinegun Precision Kill Percentage"}
            ,"supkillpct": {"table": AccountWeaponStats, "column": "weaponKillsPrecisionKillsSuper", "message": "Super Precision Kill Percentage"}
            ,"prkills": {"table": AccountWeaponStats, "column": "weaponKillsPulseRifle", "message": "Total Pulse Rifle Kills"}
            ,"rkills": {"table": AccountWeaponStats, "column": "weaponKillsRelic", "message": "Total Relic Kills"}
            ,"rlkills": {"table": AccountWeaponStats, "column": "weaponKillsRocketLauncher", "message": "Total Rocket Launcher Kills"}
            ,"srkills": {"table": AccountWeaponStats, "column": "weaponKillsScoutRifle", "message": "Total Scout Rifle Kills"}
            ,"shkills": {"table": AccountWeaponStats, "column": "weaponKillsShotgun", "message": "Total Shotgun Kills"}
            ,"sakills": {"table": AccountWeaponStats, "column": "weaponKillsSideArm", "message": "Total Sidearm Kills"}
            ,"snkills": {"table": AccountWeaponStats, "column": "weaponKillsSniper", "message": "Total Sniper Kills"}
            ,"smgkills": {"table": AccountWeaponStats, "column": "weaponKillsSubmachinegun", "message": "Total Submachinegun Kills"}
            ,"sukills": {"table": AccountWeaponStats, "column": "weaponKillsSuper", "message": "Total Super Kills"}
            ,"swkills": {"table": AccountWeaponStats, "column": "weaponKillsSword", "message": "Total Sword Kills"}
            ,"arpkills": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsAutoRifle", "message": "Total Auto Rifle Precision Kills"}
            ,"frpkills": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsFusionRifle", "message": "Total Fusion Rifle Precision Kills"}
            ,"gpkills": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsGrenade", "message": "Total Grenade Precision Kills"}
            ,"glpkills": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsGrenadeLauncher", "message": "Total Grenade Launcher Precision Kills"}
            ,"hcpkills": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsHandCannon", "message": "Total Hand Cannon Precision Kills"}
            ,"mgpkills": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsMachinegun", "message": "Total Machine Gun Precision Kills"}
            ,"mpkills": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsMelee", "message": "Total Melee Precision Kills"}
            ,"prpkills": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsPulseRifle", "message": "Total Pulse Rifle Precision Kills"}
            ,"rpkills": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsRelic", "message": "Total Relic Precision Kills"}
            ,"rlpkills": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsRocketLauncher", "message": "Total Rocket Launcher Precision Kills"}
            ,"srpkills": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsScoutRifle", "message": "Total Scout Rifle Precision Kills"}
            ,"shpkills": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsShotgun", "message": "Total Shotgun Precision Kills"}
            ,"sapkills": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsSideArm", "message": "Total Sidearm Precision Kills"}
            ,"snpkills": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsSniper", "message": "Total Sniper Precision Kills"}
            ,"smgpkills": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsSubmachinegun", "message": "Total Submachinegun Precision Kills"}
            ,"supkills": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsSuper", "message": "Total Super Precision Kills"}
            ,"akpg": {"table": AccountWeaponStats, "column": "weaponKillsAbilitypg", "message": "Ability Kills Per Game"}
            ,"arkpg": {"table": AccountWeaponStats, "column": "weaponKillsAutoRiflepg", "message": "Auto Rifle Kills Per Game"}
            ,"frkpg": {"table": AccountWeaponStats, "column": "weaponKillsFusionRiflepg", "message": "Fusion Rifle Kills Per Game"}
            ,"gkpg": {"table": AccountWeaponStats, "column": "weaponKillsGrenadepg", "message": "Grenade Kills Per Game"}
            ,"glkpg": {"table": AccountWeaponStats, "column": "weaponKillsGrenadeLauncherpg", "message": "Grenade Launcher Kills Per Game"}
            ,"hckpg": {"table": AccountWeaponStats, "column": "weaponKillsHandCannonpg", "message": "Hand Cannon Kills Per Game"}
            ,"mgkpg": {"table": AccountWeaponStats, "column": "weaponKillsMachinegunpg", "message": "Machine Gun Kills Per Game"}
            ,"mkpg": {"table": AccountWeaponStats, "column": "weaponKillsMeleepg", "message": "Melee Kills Per Game"}
            ,"prkpg": {"table": AccountWeaponStats, "column": "weaponKillsPulseRiflepg", "message": "Pulse Rifle Kills Per Game"}
            ,"rkpg": {"table": AccountWeaponStats, "column": "weaponKillsRelicpg", "message": "Relic Kills Per Game"}
            ,"rlkpg": {"table": AccountWeaponStats, "column": "weaponKillsRocketLauncherpg", "message": "Rocket Launcher Kills Per Game"}
            ,"srkpg": {"table": AccountWeaponStats, "column": "weaponKillsScoutRiflepg", "message": "Scout Rifle Kills Per Game"}
            ,"shkpg": {"table": AccountWeaponStats, "column": "weaponKillsShotgunpg", "message": "Shotgun Kills Per Game"}
            ,"sakpg": {"table": AccountWeaponStats, "column": "weaponKillsSideArmpg", "message": "Sidearm Kills Per Game"}
            ,"snkpg": {"table": AccountWeaponStats, "column": "weaponKillsSniperpg", "message": "Sniper Kills Per Game"}
            ,"smgkpg": {"table": AccountWeaponStats, "column": "weaponKillsSubmachinegunpg", "message": "Submachinegun Kills Per Game"}
            ,"sukpg": {"table": AccountWeaponStats, "column": "weaponKillsSuperpg", "message": "Super Kills Per Game"}
            ,"swkpg": {"table": AccountWeaponStats, "column": "weaponKillsSwordpg", "message": "Sword Kills Per Game"}
            ,"arpkpg": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsAutoRiflepg", "message": "Auto Rifle Precision Kills Per Game"}
            ,"frpkpg": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsFusionRiflepg", "message": "Fusion Rifle Precision Kills Per Game"}
            ,"gpkpg": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsGrenadepg", "message": "Grenade Precision Kills Per Game"}
            ,"glpkpg": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsGrenadeLauncherpg", "message": "Grenade Launcher Precision Kills Per Game"}
            ,"hcpkpg": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsHandCannonpg", "message": "Hand Cannon Precision Kills Per Game"}
            ,"mgpkpg": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsMachinegunpg", "message": "Machine Gun Precision Kills Per Game"}
            ,"mpkpg": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsMeleepg", "message": "Melee Precision Kills Per Game"}
            ,"prpkpg": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsPulseRiflepg", "message": "Pulse Rifle Precision Kills Per Game"}
            ,"rpkpg": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsRelicpg", "message": "Relic Precision Kills Per Game"}
            ,"rlpkpg": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsRocketLauncherpg", "message": "Rocket Launcher Precision Kills Per Game"}
            ,"srpkpg": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsScoutRiflepg", "message": "Scout Rifle Precision Kills Per Game"}
            ,"shpkpg": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsShotgunpg", "message": "Shotgun Precision Kills Per Game"}
            ,"sapkpg": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsSideArmpg", "message": "Sidearm Precision Kills Per Game"}
            ,"snpkpg": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsSniperpg", "message": "Sniper Precision Kills Per Game"}
            ,"smpgkp": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsSubmachinegunpg", "message": "Submachinegun Precision Kills Per Game"}
            ,"supkpg": {"table": AccountWeaponStats, "column": "weaponPrecisionKillsSuperpg", "message": "Super Precision Kills Per Game"}
            }

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
