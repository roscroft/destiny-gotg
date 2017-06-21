#!/usr/bin/python
#This will build both the total and per game average tables

import sqlite3 as lite
import sys
import os
import json

def initializeTable():
    con = lite.connect('guardians.db')
    with con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS PvETotal")
        cur.execute("DROP TABLE IF EXISTS PvEPGA")

        cur.execute("CREATE TABLE PvPTotal(Name TEXT, abilityKills REAL, activitiesEntered REAL, activitiesWon REAL, allParticipantsCount REAL, allParticipantsScore REAL, allParticipantsTimePlayed REAL, assists REAL, averageDeathDistance REAL, averageKillDistance REAL, averageLifespan REAL, averageScorePerKill REAL, averageScorePerLife REAL, bestSingleGameKills REAL, bestSingleGameScore REAL, closeCalls REAL, combatRating REAL, deaths REAL, defensiveKills REAL, dominationKills REAL, highestCharacterLevel REAL, highestLightLevel REAL, kills REAL, killsDeathAssists REAL, killsDeathsRatio REAL, longestKillDistance REAL, longestKillSpree REAL, longestSingleLife REAL, mostPrecisionKills REAL, objectivesCompleted REAL, offensiveKills REAL, orbsDropped REAL, orbsGathered REAL, precisionKills REAL, relicsCaptured REAL, remainingTimeAfterQuitSeconds REAL, resurrectionsPerformed REAL, resurrectionsReceived REAL, score REAL, secondsPlayed REAL, suicides REAL, teamScore REAL, totalActivityDurationSeconds REAL, totalDeathDistance REAL, totalKillDistance REAL, weaponBestType TEXT, weaponKillsAutoRifle REAL, weaponKillsFusionRifle REAL, weaponKillsGrenade REAL, weaponKillsHandCannon REAL, weaponKillsMachinegun REAL, weaponKillsMelee REAL, weaponKillsPulseRifle REAL, weaponKillsRelic REAL, weaponKillsRocketLauncher REAL, weaponKillsScoutRifle REAL, weaponKillsShotgun REAL, weaponKillsSideArm REAL, weaponKillsSniper REAL, weaponKillsSubmachinegun REAL, weaponKillsSuper REAL, weaponKillsSword REAL, winLossRatio REAL, zonesCaptured REAL, zonesNeutralized REAL)")
        
        cur.execute("CREATE TABLE PvPPGA(Name TEXT, abilityKills REAL, activitiesEntered REAL, activitiesWon REAL, allParticipantsCount REAL, allParticipantsScore REAL, allParticipantsTimePlayed REAL, assists REAL, averageDeathDistance REAL, averageKillDistance REAL, averageLifespan REAL, averageScorePerKill REAL, averageScorePerLife REAL, bestSingleGameKills REAL, bestSingleGameScore REAL, closeCalls REAL, combatRating REAL, deaths REAL, defensiveKills REAL, dominationKills REAL, highestCharacterLevel REAL, highestLightLevel REAL, kills REAL, killsDeathAssists REAL, killsDeathsRatio REAL, longestKillDistance REAL, longestKillSpree REAL, longestSingleLife REAL, mostPrecisionKills REAL, objectivesCompleted REAL, offensiveKills REAL, orbsDropped REAL, orbsGathered REAL, precisionKills REAL, relicsCaptured REAL, remainingTimeAfterQuitSeconds REAL, resurrectionsPerformed REAL, resurrectionsReceived REAL, score REAL, secondsPlayed REAL, suicides REAL, teamScore REAL, totalActivityDurationSeconds REAL, totalDeathDistance REAL, totalKillDistance REAL, weaponBestType TEXT, weaponKillsAutoRifle REAL, weaponKillsFusionRifle REAL, weaponKillsGrenade REAL, weaponKillsHandCannon REAL, weaponKillsMachinegun REAL, weaponKillsMelee REAL, weaponKillsPulseRifle REAL, weaponKillsRelic REAL, weaponKillsRocketLauncher REAL, weaponKillsScoutRifle REAL, weaponKillsShotgun REAL, weaponKillsSideArm REAL, weaponKillsSniper REAL, weaponKillsSubmachinegun REAL, weaponKillsSuper REAL, weaponKillsSword REAL, winLossRatio REAL, zonesCaptured REAL, zonesNeutralized REAL)")

def parseStatsJSON():
    for filename in os.listdir('./Stats/'):
        if filename.endswith(".json"):
            with open('./Stats/'+filename) as data_file:
                data = json.load(data_file)
                dispName = filename[:-5]
                totalStatTuple = parseData(data,'basic', dispName)
                pgaStatTuple = parseData(data, 'pga', dispName)
                addToDatabase(totalStatTuple, 'PvETotal')
                addToDatabase(pgaStatTuple, 'PvEPGA')

def parseData(data, mode, dispName):
    path = data['Response']['mergedAllCharacters']['results']['allPvE']['allTime']
    stats = []
    for stat in path:
        if mode not in path[stat]:
            stats.append((stat, None))
        else:
            stats.append((stat, path[stat][mode]['value']))
    #Sorts on first item (alphabetical list of stats)
    stats.sort(key=lambda x: x[0])
    values = [x[1] for x in stats]
    return (dispName,)+tuple(values)

def addToDatabase(stats, table):
    con = lite.connect('guardians.db')

    with con:
        cur = con.cursor()
        cur.execute("INSERT INTO "+table+" VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", stats)


def buildPvPTables():
    initializeTable()
    parseStatsJSON()

if __name__ == "__main__":
    buildPvPTables()
