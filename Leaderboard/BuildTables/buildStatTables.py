#!/usr/bin/python
import sys
sys.path.append('../../')
sys.path.append('../')
import DatabaseModules.databaseStatements as db
import os
import json

def buildStatTables(path, databasePath):
    
    def initializeTables():
        pvpTotal = "PvPTotal"
        pvpPGA = "PvPPGA"
        pveTotal = "PvETotal"
        pvePGA = "PvEPGA"

        pvefields = "(Name TEXT, abilityKills REAL, activitiesCleared REAL, activitiesEntered REAL, allParticipantsCount REAL, allParticipantsTimePlayed REAL, assists REAL, averageDeathDistance REAL, averageKillDistance REAL, averageLifespan REAL, bestSingleGameKills REAL, courtOfOryxAttempts REAL, courtOfOryxCompletions REAL, courtOfOryxWinsTier1 REAL, courtOfOryxWinsTier2 REAL, courtOfOryxWinsTier3 REAL, deaths REAL, fastestCompletion REAL, highestCharacterLevel REAL, highestLightLevel REAL, kills REAL, killsDeathAssists REAL, killsDeathsRatio REAL, longestKillDistance REAL, longestKillSpree REAL, longestSingleLife REAL, mostPrecisionKills REAL, objectivesCompleted REAL, orbsDropped REAL, orbsGathered REAL, precisionKills REAL, publicEventsCompleted REAL, publicEventsJoined REAL, remainingTimeAfterQuitSeconds REAL, resurrectionsPerformed REAL, resurrectionsReceived REAL, secondsPlayed REAL, suicides REAL, totalActivityDurationSeconds REAL, totalDeathDistance REAL, totalKillDistance REAL, weaponBestType TEXT, weaponKillsAutoRifle REAL, weaponKillsFusionRifle REAL, weaponKillsGrenade REAL, weaponKillsHandCannon REAL, weaponKillsMachinegun REAL, weaponKillsMelee REAL, weaponKillsPulseRifle REAL, weaponKillsRelic REAL, weaponKillsRocketLauncher REAL, weaponKillsScoutRifle REAL, weaponKillsShotgun REAL, weaponKillsSideArm REAL, weaponKillsSniper REAL, weaponKillsSubmachinegun REAL, weaponKillsSuper REAL, weaponKillsSword REAL)"
        
        pvpfields = "(Name TEXT, abilityKills REAL, activitiesEntered REAL, activitiesWon REAL, allParticipantsCount REAL, allParticipantsScore REAL, allParticipantsTimePlayed REAL, assists REAL, averageDeathDistance REAL, averageKillDistance REAL, averageLifespan REAL, averageScorePerKill REAL, averageScorePerLife REAL, bestSingleGameKills REAL, bestSingleGameScore REAL, closeCalls REAL, combatRating REAL, deaths REAL, defensiveKills REAL, dominationKills REAL, highestCharacterLevel REAL, highestLightLevel REAL, kills REAL, killsDeathAssists REAL, killsDeathsRatio REAL, longestKillDistance REAL, longestKillSpree REAL, longestSingleLife REAL, mostPrecisionKills REAL, objectivesCompleted REAL, offensiveKills REAL, orbsDropped REAL, orbsGathered REAL, precisionKills REAL, relicsCaptured REAL, remainingTimeAfterQuitSeconds REAL, resurrectionsPerformed REAL, resurrectionsReceived REAL, score REAL, secondsPlayed REAL, suicides REAL, teamScore REAL, totalActivityDurationSeconds REAL, totalDeathDistance REAL, totalKillDistance REAL, weaponBestType TEXT, weaponKillsAutoRifle REAL, weaponKillsFusionRifle REAL, weaponKillsGrenade REAL, weaponKillsHandCannon REAL, weaponKillsMachinegun REAL, weaponKillsMelee REAL, weaponKillsPulseRifle REAL, weaponKillsRelic REAL, weaponKillsRocketLauncher REAL, weaponKillsScoutRifle REAL, weaponKillsShotgun REAL, weaponKillsSideArm REAL, weaponKillsSniper REAL, weaponKillsSubmachinegun REAL, weaponKillsSuper REAL, weaponKillsSword REAL, winLossRatio REAL, zonesCaptured REAL, zonesNeutralized REAL)"

        db.initializeTable(pveTotal, pvefields)
        db.initializeTable(pvePGA, pvefields)
        db.initializeTable(pvpTotal, pvpfields)
        db.initializeTable(pvpPGA, pvpfields)

    def parseStatsJSON(versus):
        totalTable = versus + "Total"
        pgaTable = versus + "PGA"
        for filename in os.listdir(path):
            if filename.endswith(".json"):
                with open(path+filename) as data_file:
                    data = json.load(data_file)
                    dispName = filename[:-5]
                    totalStatTuple = parseData(data,'basic', dispName, versus)
                    pgaStatTuple = parseData(data, 'pga', dispName, versus)
                    addToDatabase(totalStatTuple, totalTable, versus)
                    addToDatabase(pgaStatTuple, pgaTable, versus)

    def parseData(data, mode, dispName, versus):
        allVersus = "all"+versus
        path = data['Response']['mergedAllCharacters']['results'][allVersus]['allTime']
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

    def addToDatabase(stats, table, versus):
        if versus == "PvP":
            request = "INSERT INTO "+table+" VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        elif versus == "PvE":
            request = "INSERT INTO "+table+" VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        db.insert(request, stats)

    initializeTables()
    pvp = "PvP"
    pve = "PvE"
    parseStatsJSON(pvp)
    parseStatsJSON(pve)

if __name__ == "__main__":
    path = '../Stats/'
    databasePath = '../guardians.db'
    buildStatTables(path, databasePath)
