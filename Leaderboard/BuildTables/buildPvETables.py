#!/usr/bin/python
#This will build both the total and per game average tables

import sqlite3 as lite
import sys
import os
import json

def buildPvETables(path, databasePath):
    
    def initializeTable():
        con = lite.connect(databasePath)
        with con:
            cur = con.cursor()
            cur.execute("DROP TABLE IF EXISTS PvETotal")
            cur.execute("DROP TABLE IF EXISTS PvEPGA")

            cur.execute("CREATE TABLE PvETotal(Name TEXT, abilityKills REAL, activitiesCleared REAL, activitiesEntered REAL, allParticipantsCount REAL, allParticipantsTimePlayed REAL, assists REAL, averageDeathDistance REAL, averageKillDistance REAL, averageLifespan REAL, bestSingleGameKills REAL, courtOfOryxAttempts REAL, courtOfOryxCompletions REAL, courtOfOryxWinsTier1 REAL, courtOfOryxWinsTier2 REAL, courtOfOryxWinsTier3 REAL, deaths REAL, fastestCompletion REAL, highestCharacterLevel REAL, highestLightLevel REAL, kills REAL, killsDeathAssists REAL, killsDeathsRatio REAL, longestKillDistance REAL, longestKillSpree REAL, longestSingleLife REAL, mostPrecisionKills REAL, objectivesCompleted REAL, orbsDropped REAL, orbsGathered REAL, precisionKills REAL, publicEventsCompleted REAL, publicEventsJoined REAL, remainingTimeAfterQuitSeconds REAL, resurrectionsPerformed REAL, resurrectionsReceived REAL, secondsPlayed REAL, suicides REAL, totalActivityDurationSeconds REAL, totalDeathDistance REAL, totalKillDistance REAL, weaponBestType TEXT, weaponKillsAutoRifle REAL, weaponKillsFusionRifle REAL, weaponKillsGrenade REAL, weaponKillsHandCannon REAL, weaponKillsMachinegun REAL, weaponKillsMelee REAL, weaponKillsPulseRifle REAL, weaponKillsRelic REAL, weaponKillsRocketLauncher REAL, weaponKillsScoutRifle REAL, weaponKillsShotgun REAL, weaponKillsSideArm REAL, weaponKillsSniper REAL, weaponKillsSubmachinegun REAL, weaponKillsSuper REAL, weaponKillsSword REAL)")

            
            cur.execute("CREATE TABLE PvEPGA(Name TEXT, abilityKills REAL, activitiesCleared REAL, activitiesEntered REAL, allParticipantsCount REAL, allParticipantsTimePlayed REAL, assists REAL, averageDeathDistance REAL, averageKillDistance REAL, averageLifespan REAL, bestSingleGameKills REAL, courtOfOryxAttempts REAL, courtOfOryxCompletions REAL, courtOfOryxWinsTier1 REAL, courtOfOryxWinsTier2 REAL, courtOfOryxWinsTier3 REAL, deaths REAL, fastestCompletion REAL, highestCharacterLevel REAL, highestLightLevel REAL, kills REAL, killsDeathAssists REAL, killsDeathsRatio REAL, longestKillDistance REAL, longestKillSpree REAL, longestSingleLife REAL, mostPrecisionKills REAL, objectivesCompleted REAL, orbsDropped REAL, orbsGathered REAL, precisionKills REAL, publicEventsCompleted REAL, publicEventsJoined REAL, remainingTimeAfterQuitSeconds REAL, resurrectionsPerformed REAL, resurrectionsReceived REAL, secondsPlayed REAL, suicides REAL, totalActivityDurationSeconds REAL, totalDeathDistance REAL, totalKillDistance REAL, weaponBestType TEXT, weaponKillsAutoRifle REAL, weaponKillsFusionRifle REAL, weaponKillsGrenade REAL, weaponKillsHandCannon REAL, weaponKillsMachinegun REAL, weaponKillsMelee REAL, weaponKillsPulseRifle REAL, weaponKillsRelic REAL, weaponKillsRocketLauncher REAL, weaponKillsScoutRifle REAL, weaponKillsShotgun REAL, weaponKillsSideArm REAL, weaponKillsSniper REAL, weaponKillsSubmachinegun REAL, weaponKillsSuper REAL, weaponKillsSword REAL)")

    def parseStatsJSON():
        for filename in os.listdir(path):
            if filename.endswith(".json"):
                with open(path+filename) as data_file:
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
        con = lite.connect(databasePath)

        with con:
            cur = con.cursor()
            cur.execute("INSERT INTO "+table+" VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", stats)

    initializeTable()
    parseStatsJSON()

if __name__ == "__main__":
    path = '../Stats/'
    databasePath = '../guardians.db'
    
    buildPvETables(path, databasePath)
