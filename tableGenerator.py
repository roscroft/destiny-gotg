# Generates standard activity table initialization code from a JSON.

# Parse the JSON for a list of attributes - these will be the database fields

initialSet = {"abilityKills", "activitiesCleared", "activitiesEntered", "activitiesWon", "activityDuration", "allParticipantsCount", "allParticipantsScore", "allParticipantsTimePlayed", "assists", "averageDeathDistance", "averageKillDistance", "averageLifespan", "averageScorePerKill", "averageScorePerLife", "bestSingleGameKills", "bestSingleGameScore", "capturedYourOwnKill", "carrierKills", "closeCalls", "combatRating", "completionReason", "courtOfOryxAttempts", "courtOfOryxCompletions", "courtOfOryxWinsTier1", "courtOfOryxWinsTier2", "courtOfOryxWinsTier3", "dailyMedalsEarned", "deaths", "defensiveKills", "dominationKills", "dunkKills", "fastestCompletion", "fireTeamId", "gatesHit", "highestCharacterLevel", "highestLightLevel", "highestSandboxLevel", "kills", "killsDeathsAssists", "killsDeathsRatio", "longestKillDistance", "longestKillSpree", "longestSingleLife", "lostTagToOpponent", "mostPrecisionKills", "objectivesCompleted", "offensiveKills", "orbsDropped", "orbsGathered", "playerCount", "precisionKills", "publicEventsCompleted", "publicEventsJoined", "raceCompletionMilliseconds", "raceCompletionSeconds", "recoveredOwnDeadTag", "recoveredTeammateTags", "relicsCaptured", "remainingTimeAfterQuitSeconds", "resurrectionsPerformed", "resurrectionsReceived", "score", "secondsPlayed", "slamDunks", "sparksCaptured", "standing", "styleDunks", "suicides", "tagCaptures", "tagsCapturedPerTagLost", "team", "teamScore", "totalActivityDurationSeconds", "totalDeathDistance", "totalKillDistance", "weaponBestType", "weaponKillsAutoRifle", "weaponKillsHandCannon", "weaponKillsFusionRifle", "weaponKillsGrenade", "weaponKillsMachinegun", "weaponKillsMelee", "weaponKillsPulseRifle", "weaponKillsRelic", "weaponKillsRocketLauncher", "weaponKillsScoutRifle", "weaponKillsShotgun", "weaponKillsSideArm", "weaponKillsSniper", "weaponKillsSubmachinegun", "weaponKillsSuper", "weaponKillsSword", "winLossRatio", "zonesCaptured", "zonesNeutralized"}

def table_generator(iterator, dct):
    mode = iterator[1] 
    statList = set()
    for key in dct.keys():
        statList.add(key)
    initialSet = initialSet.intersection(statList)

    with open(f"commonStats.txt", "w+") as f:
        lst = sorted(list(initialSet))

        for item in lst:
            f.write(f"    {stat} = Column(Float)")

    # with open(f"./generatedTables/addTable_{mode}", "w+") as f:
    #     modeTitle = mode.title()
    #     f.write(f"Class Account{modeTitle}Stats\n")
    #     f.write(f"    __tablename__ = 'account{modeTitle}Stats'\n")
    #     f.write("    id = Column(Integer, ForeignKey('account.id'), primary_key=True)\n")
    #     f.write("    account = relationship(Account)\n")
    #     for stat in statList:
    #         f.write(f"    {stat},\n")
