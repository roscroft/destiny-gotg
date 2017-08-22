#!/usr/bin/python
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from destinygotg import loadConfig

Base = declarative_base()

class Bungie(Base):
    __tablename__ = 'bungie'
    id = Column(String(50), primary_key=True)
    bungie_name = Column(String(50), nullable=False)
    membership_type = Column(Integer, nullable=False)

class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True)
    display_name = Column(String(50), nullable=False)
    membership_type = Column(Integer, nullable=False)
    bungie_id = Column(String(50), ForeignKey('bungie.id'))
    bungie = relationship(Bungie)

class Discord(Base):
    __tablename__ = 'discord'
    id = Column(Integer, primary_key=True)
    membership_id = Column(Integer, ForeignKey('account.id'), primary_key=True)
    account = relationship(Account)
    discord_name = Column(String(50))

class PvEAggregate(Base):
    __tablename__ = 'pveAggregate'
    id = Column(Integer, ForeignKey('account.id'), primary_key=True)
    account = relationship(Account)
    abilityKills = Column(Integer)
    activitiesCleared = Column(Integer)
    activitiesEntered = Column(Integer)
    allParticipantsCount = Column(Integer)
    allParticipantsTimePlayed = Column(Integer)
    assists = Column(Integer)
    averageKillDistance = Column(Float)
    averageLifespan = Column(Float)
    averageDeathDistance = Column(Float)
    bestSingleGameKills = Column(Integer)
    courtOfOryxAttempts = Column(Integer)
    courtOfOryxCompletions = Column(Integer)
    courtOfOryxWinsTier1 = Column(Integer)
    courtOfOryxWinsTier2 = Column(Integer)
    courtOfOryxWinsTier3 = Column(Integer)
    deaths = Column(Integer)
    fastestCompletion = Column(Integer)
    highestCharacterLevel = Column(Integer)
    highestLightLevel = Column(Integer)
    kills = Column(Integer)
    killsDeathsAssists = Column(Float)
    killsDeathsRatio = Column(Float)
    longestKillDistance = Column(Integer)
    longestKillSpree = Column(Integer)
    longestSingleLife = Column(Integer)
    mostPrecisionKills = Column(Integer)
    objectivesCompleted = Column(Integer)
    orbsDropped = Column(Integer)
    orbsGathered = Column(Integer)
    precisionKills = Column(Integer)
    publicEventsCompleted = Column(Integer)
    publicEventsJoined = Column(Integer)
    remainingTimeAfterQuitSeconds = Column(Integer)
    resurrectionsPerformed = Column(Integer)
    resurrectionsReceived = Column(Integer)
    secondsPlayed = Column(Integer)
    suicides = Column(Integer)
    totalActivityDurationSeconds = Column(Integer)
    totalDeathDistance = Column(Integer)
    totalKillDistance = Column(Integer)
    weaponBestType = Column(Integer)
    weaponKillsAutoRifle = Column(Integer)
    weaponKillsHandCannon = Column(Integer)
    weaponKillsFusionRifle = Column(Integer)
    weaponKillsGrenade = Column(Integer)
    weaponKillsMachinegun = Column(Integer)
    weaponKillsMelee = Column(Integer)
    weaponKillsPulseRifle = Column(Integer)
    weaponKillsRelic = Column(Integer)
    weaponKillsRocketLauncher = Column(Integer)
    weaponKillsScoutRifle = Column(Integer)
    weaponKillsShotgun = Column(Integer)
    weaponKillsSideArm = Column(Integer)
    weaponKillsSniper = Column(Integer)
    weaponKillsSubmachinegun = Column(Integer)
    weaponKillsSuper = Column(Integer)
    weaponKillsSword = Column(Integer)
    winLossRatio = Column(Float)
    zonesCaptured = Column(Integer)
    abilityKillspg = Column(Float)
    assistspg = Column(Float)
    deathspg = Column(Float)
    killspg = Column(Float)
    objectivesCompletedpg = Column(Float)
    orbsDroppedpg = Column(Float)
    orbsGatheredpg = Column(Float)
    precisionKillspg = Column(Float)
    publicEventsCompletedpg = Column(Float)
    publicEventsJoinedpg = Column(Float)
    remainingTimeAfterQuitSecondspg = Column(Float)
    resurrectionsPerformedpg = Column(Float)
    resurrectionsReceivedpg = Column(Float)
    secondsPlayedpg = Column(Float)
    suicidespg = Column(Float)
    totalActivityDurationSecondspg = Column(Float)
    weaponKillsAutoRiflepg = Column(Float)
    weaponKillsHandCannonpg = Column(Float)
    weaponKillsFusionRiflepg = Column(Float)
    weaponKillsGrenadepg = Column(Float)
    weaponKillsMachinegunpg = Column(Float)
    weaponKillsMeleepg = Column(Float)
    weaponKillsPulseRiflepg = Column(Float)
    weaponKillsRelicpg = Column(Float)
    weaponKillsRocketLauncherpg = Column(Float)
    weaponKillsScoutRiflepg = Column(Float)
    weaponKillsShotgunpg = Column(Float)
    weaponKillsSideArmpg = Column(Float)
    weaponKillsSniperpg = Column(Float)
    weaponKillsSubmachinegunpg = Column(Float)
    weaponKillsSuperpg = Column(Float)
    weaponKillsSwordpg = Column(Float)
    zonesCapturedpg = Column(Float)
    zonesNeutralizedpg = Column(Float)
    zonesNeutralized = Column(Integer)

class PvPAggregate(Base):
    __tablename__ = 'pvpAggregate'
    id = Column(Integer, ForeignKey('account.id'), primary_key=True)
    account = relationship(Account)
    abilityKills = Column(Integer)
    activitiesEntered = Column(Integer)
    activitiesWon = Column(Integer)
    allParticipantsCount = Column(Integer)
    allParticipantsScore = Column(Integer)
    allParticipantsTimePlayed = Column(Integer)
    assists = Column(Integer)
    averageKillDistance = Column(Float)
    averageLifespan = Column(Float)
    averageDeathDistance = Column(Float)
    averageScorePerKill = Column(Float)
    averageScorePerLife = Column(Float)
    bestSingleGameKills = Column(Integer)
    bestSingleGameScore = Column(Integer)
    closeCalls = Column(Integer)
    combatRating = Column(Float)
    deaths = Column(Integer)
    defensiveKills = Column(Integer)
    dominationKills = Column(Integer)
    highestCharacterLevel = Column(Integer)
    highestLightLevel = Column(Integer)
    kills = Column(Integer)
    killsDeathsAssists = Column(Float)
    killsDeathsRatio = Column(Float)
    longestKillDistance = Column(Integer)
    longestKillSpree = Column(Integer)
    longestSingleLife = Column(Integer)
    mostPrecisionKills = Column(Integer)
    objectivesCompleted = Column(Integer)
    offensiveKills = Column(Integer)
    orbsDropped = Column(Integer)
    orbsGathered = Column(Integer)
    precisionKills = Column(Integer)
    relicsCaptured = Column(Integer)
    remainingTimeAfterQuitSeconds = Column(Integer)
    resurrectionsPerformed = Column(Integer)
    resurrectionsReceived = Column(Integer)
    score = Column(Integer)
    secondsPlayed = Column(Integer)
    suicides = Column(Integer)
    teamScore = Column(Integer)
    totalActivityDurationSeconds = Column(Integer)
    totalDeathDistance = Column(Integer)
    totalKillDistance = Column(Integer)
    weaponBestType = Column(Integer)
    weaponKillsAutoRifle = Column(Integer)
    weaponKillsHandCannon = Column(Integer)
    weaponKillsFusionRifle = Column(Integer)
    weaponKillsGrenade = Column(Integer)
    weaponKillsMachinegun = Column(Integer)
    weaponKillsMelee = Column(Integer)
    weaponKillsPulseRifle = Column(Integer)
    weaponKillsRelic = Column(Integer)
    weaponKillsRocketLauncher = Column(Integer)
    weaponKillsScoutRifle = Column(Integer)
    weaponKillsShotgun = Column(Integer)
    weaponKillsSideArm = Column(Integer)
    weaponKillsSniper = Column(Integer)
    weaponKillsSubmachinegun = Column(Integer)
    weaponKillsSuper = Column(Integer)
    weaponKillsSword = Column(Integer)
    winLossRatio = Column(Float)
    zonesCaptured = Column(Integer)
    zonesNeutralized = Column(Integer)
    abilityKillspg = Column(Float)
    assistspg = Column(Float)
    closeCallspg = Column(Float)
    deathspg = Column(Float)
    dominationKillspg = Column(Float)
    killspg = Column(Float)
    objectivesCompletedpg = Column(Float)
    offensiveKillspg = Column(Float)
    orbsDroppedpg = Column(Float)
    orbsGatheredpg = Column(Float)
    precisionKillspg = Column(Float)
    relicsCapturedpg = Column(Float)
    remainingTimeAfterQuitSecondspg = Column(Float)
    resurrectionsPerformedpg = Column(Float)
    resurrectionsReceivedpg = Column(Float)
    scorepg = Column(Float)
    secondsPlayedpg = Column(Float)
    suicidespg = Column(Float)
    teamScorepg = Column(Float)
    totalActivityDurationSecondspg = Column(Float)
    weaponKillsAutoRiflepg = Column(Float)
    weaponKillsHandCannonpg = Column(Float)
    weaponKillsFusionRiflepg = Column(Float)
    weaponKillsGrenadepg = Column(Float)
    weaponKillsMachinegunpg = Column(Float)
    weaponKillsMeleepg = Column(Float)
    weaponKillsPulseRiflepg = Column(Float)
    weaponKillsRelicpg = Column(Float)
    weaponKillsRocketLauncherpg = Column(Float)
    weaponKillsScoutRiflepg = Column(Float)
    weaponKillsShotgunpg = Column(Float)
    weaponKillsSideArmpg = Column(Float)
    weaponKillsSniperpg = Column(Float)
    weaponKillsSubmachinegunpg = Column(Float)
    weaponKillsSuperpg = Column(Float)
    weaponKillsSwordpg = Column(Float)
    zonesCapturedpg = Column(Float)
    zonesNeutralizedpg = Column(Float)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    membership_id = Column(Integer, ForeignKey('account.id'))
    account = relationship(Account)
    minutes_played = Column(Integer)
    light_level = Column(Integer)
    class_hash = Column(Integer)
    grimoire = Column(Integer)

class AccountWeaponUsage(Base):
    __tablename__ = 'accountWeaponUsage'
    id = Column(Integer, ForeignKey('account.id'), primary_key=True) 
    account = relationship(Account)
    weaponHash = Column(Integer, primary_key=True)
    kills = Column(Integer)
    precision_kills = Column(Integer)
    precision_kill_percentage = Column(Float)

class CharacterActivityStats(Base):
    __tablename__ = 'characterActivityStats'
    id = Column(Integer, ForeignKey('character.id'), primary_key=True)
    character = relationship(Character)
    activityHash = Column(Integer, primary_key=True)
    activityAssists = Column(Integer)
    activityCompletions = Column(Integer)
    activityDeaths = Column(Integer)
    activityGatesHit = Column(Integer)
    activityKills = Column(Integer)
    activityKillsDeathsAssists = Column(Float)
    activityKillsDeathsRatio = Column(Float)
    activityPrecisionKills = Column(Integer)
    activitySecondsPlayed = Column(Integer)
    activityWins = Column(Integer)
    fastestCompletionSecondsForActivity = Column(Integer)

class AccountMedals(Base):
    __tablename__ = 'accountMedals'
    id = Column(Integer, ForeignKey('account.id'), primary_key=True)
    account = relationship(Account)
    activitiesEntered = Column(Integer)
    allMedalsEarned = Column(Integer)
    allMedalsScore = Column(Integer)
    medalsAbilityArcLightningKillMulti = Column(Integer)
    medalsAbilityGhostGunKillMulti = Column(Integer)
    medalsAbilityHavocKillMulti = Column(Integer)
    medalsAbilityNovaBombKillMulti = Column(Integer)
    medalsAbilityRadianceGrenadeKillMulti = Column(Integer)
    medalsAbilityShadowStrikeKillMulti = Column(Integer)
    medalsAbilityThermalHammerKillMulti = Column(Integer)
    medalsAbilityVoidBowKillMulti = Column(Integer)
    medalsAbilityWardDeflect = Column(Integer)
    medalsActivityCompleteControlMostCaptures = Column(Integer)
    medalsActivityCompleteCycle = Column(Integer)
    medalsActivityCompleteDeathless = Column(Integer)
    medalsActivityCompleteHighestScoreLosing = Column(Integer)
    medalsActivityCompleteHighestScoreWinning = Column(Integer)
    medalsActivityCompleteLonewolf = Column(Integer)
    medalsActivityCompleteSalvageMostCancels = Column(Integer)
    medalsActivityCompleteSalvageShutout = Column(Integer)
    medalsActivityCompleteSingularityPerfectRunner = Column(Integer)
    medalsActivityCompleteVictoryBlowout = Column(Integer)
    medalsActivityCompleteVictory = Column(Integer)
    medalsActivityCompleteVictoryElimination = Column(Integer)
    medalsActivityCompleteVictoryEliminationPerfect = Column(Integer)
    medalsActivityCompleteVictoryEliminationShutout = Column(Integer)
    medalsActivityCompleteVictoryExtraLastSecond = Column(Integer)
    medalsActivityCompleteVictoryLastSecond = Column(Integer)
    medalsActivityCompleteVictoryMercy = Column(Integer)
    medalsActivityCompleteVictoryRumbleBlowout = Column(Integer)
    medalsActivityCompleteVictoryRumble = Column(Integer)
    medalsActivityCompleteVictoryRumbleLastSecond = Column(Integer)
    medalsActivityCompleteVictoryRumbleSuddenDeath = Column(Integer)
    medalsActivityCompleteVictorySuddenDeath = Column(Integer)
    medalsAvenger = Column(Integer)
    medalsBuddyResurrectionMulti = Column(Integer)
    medalsBuddyResurrectionSpree = Column(Integer)
    medalsCloseCallTalent = Column(Integer)
    medalsComebackKill = Column(Integer)
    medalsDominationKill = Column(Integer)
    medalsDominionZoneCapturedSpree = Column(Integer)
    medalsDominionZoneDefenseKillSpree = Column(Integer)
    medalsDominionZoneOffenseKillSpree = Column(Integer)
    medalsEliminationLastStandKill = Column(Integer)
    medalsEliminationLastStandRevive = Column(Integer)
    medalsEliminationWipeQuick = Column(Integer)
    medalsEliminationWipeSolo = Column(Integer)
    medalsFirstBlood = Column(Integer)
    medalsFirstPlaceKillSpree = Column(Integer)
    medalsGrenadeKillStick = Column(Integer)
    medalsHazardKill = Column(Integer)
    medalsHunterKillInvisible = Column(Integer)
    medalsKillAssistSpree = Column(Integer)
    medalsKillAssistSpreeFfa = Column(Integer)
    medalsKillHeadshot = Column(Integer)
    medalsKilljoy = Column(Integer)
    medalsKilljoyMega = Column(Integer)
    medalsKillMulti2 = Column(Integer)
    medalsKillMulti3 = Column(Integer)
    medalsKillMulti4 = Column(Integer)
    medalsKillMulti5 = Column(Integer)
    medalsKillMulti6 = Column(Integer)
    medalsKillMulti7 = Column(Integer)
    medalsKillPostmortem = Column(Integer)
    medalsKillSpree1 = Column(Integer)
    medalsKillSpree2 = Column(Integer)
    medalsKillSpree3 = Column(Integer)
    medalsKillSpreeAbsurd = Column(Integer)
    medalsKillSpreeNoDamage = Column(Integer)
    medalsMeleeKillHunterThrowingKnifeHeadshot = Column(Integer)
    medalsPaybackKill = Column(Integer)
    medalsRadianceShutdown = Column(Integer)
    medalsRescue = Column(Integer)
    medalsSalvageProbeCanceled = Column(Integer)
    medalsSalvageProbeCompleteSpree = Column(Integer)
    medalsSalvageProbeDefenseKill = Column(Integer)
    medalsSalvageProbeOffenseKillMulti = Column(Integer)
    medalsSalvageZoneCapturedSpree = Column(Integer)
    medalsSingularityFlagCaptureMulti = Column(Integer)
    medalsSingularityFlagHolderKilledClose = Column(Integer)
    medalsSingularityFlagHolderKilledMulti = Column(Integer)
    medalsSingularityRunnerDefenseMulti = Column(Integer)
    medalsSupremacy = Column(Integer)
    medalsSupremacyConfirmStreakLarge = Column(Integer)
    medalsSupremacyDenyMulti = Column(Integer)
    medalsSupremacyMostConfirms = Column(Integer)
    medalsSupremacyMostDenies = Column(Integer)
    medalsSupremacyMostSelfConfirms = Column(Integer)
    medalsSupremacyMulti = Column(Integer)
    medalsSupremacyNeverCollected = Column(Integer)
    medalsSupremacySelfDeny = Column(Integer)
    medalsTeamDominationHold1m = Column(Integer)
    medalsTeamKillSpree = Column(Integer)
    medalsUnknown = Column(Integer)
    medalsVehicleFotcTurretKillSpree = Column(Integer)
    medalsVehicleInterceptorKillSplatter = Column(Integer)
    medalsVehicleInterceptorKillSpree = Column(Integer)
    medalsVehiclePikeKillSplatter = Column(Integer)
    medalsVehiclePikeKillSpree = Column(Integer)
    medalsVehicleSparrowKillSplatter = Column(Integer)
    medalsWeaponAutoRifleKillSpree = Column(Integer)
    medalsWeaponFusionRifleKillSpree = Column(Integer)
    medalsWeaponHandCannonHeadshotSpree = Column(Integer)
    medalsWeaponMachineGunKillSpree = Column(Integer)
    medalsWeaponPulseRifleKillSpree = Column(Integer)
    medalsWeaponRocketLauncherKillSpree = Column(Integer)
    medalsWeaponScoutRifleKillSpree = Column(Integer)
    medalsWeaponShotgunKillSpree = Column(Integer)
    medalsWeaponSidearmKillSpree = Column(Integer)
    medalsWeaponSniperRifleHeadshotSpree = Column(Integer)
    medalsWeaponSwordKillSpree = Column(Integer)
    medalsWinningScore = Column(Integer)
    medalsZoneCapturedBInitial = Column(Integer)

#class CharacterStatStory(Base):
#    __tablename__ = "characterStatStory"
#
#class CharacterStatStrike(Base):
#    __tablename__ = "characterStatStrike"
#
#class CharacterStatRaid(Base):
#    __tablename__ = "characterStatRaid"
#
#class CharacterStatAllPvP(Base):
#    __tablename__ = "characterStatAllPvP"
#
#class CharacterStatPatrol(Base):
#    __tablename__ = "characterStatPatrol"
#
#class CharacterStatAllPvE(Base):
#    __tablename__ = "characterStatPvE"
#
#class CharacterStatPvPIntroduction(Base):
#    __tablename__ = "characterStatPvPIntroduction"
#
#class CharacterStatThreeVsThree(Base):
#    __tablename__ = "characterStatThreeVsThree"
#
#class CharacterStatControl(Base):
#    __tablename__ = "characterStatControl"
#
#class CharacterStatLockdown(Base):
#    __tablename__ = "characterStatLockdown"
#
#class CharacterStatTeam(Base):
#    __tablename__ = "characterStatTeam"
#
#class CharacterStatFreeForAll(Base):
#    __tablename__ = "characterStatFreeForAll"
#
#class CharacterStatTrialsOfOsiris(Base):
#    __tablename__ = "characterStatTrialsOfOsiris"
#
#class CharacterStatDoubles(Base):
#    __tablename__ = "characterStatDoubles"
#
#class CharacterStatNightfall(Base):
#    __tablename__ = "characterStatNightfall"
#
#class CharacterStatHeroic(Base):
#    __tablename__ = "characterStatHeroic"
#
#class CharacterStatAllStrikes(Base):
#    __tablename__ = "characterStatAllStrikes"
#
#class CharacterStatIronBanner(Base):
#    __tablename__ = "characterStatIronBanner"
#
#class CharacterStatAllArena(Base):
#    __tablename__ = "characterStatAllArena"
#
#class CharacterStatArena(Base):
#    __tablename__ = "characterStatArena"
#
#class CharacterStatAreneChallenge(Base):
#    __tablename__ = "characterStatArenaChallenge"
#
#class CharacterStatElimination(Base):
#    __tablename__ = "characterStatElimination"
#
#class CharacterStatRift(Base):
#    __tablename__ = "characterStatRift"
#
#class CharacterStatAllMayhem(Base):
#    __tablename__ = "characterStatAllMayhem"

class AccountActivityModeStats(Base):
    __tablename__ = "accountActivityModeStats"
    id = Column(Integer, ForeignKey('account.id'), primary_key=True)
    account = relationship(Account)
    mode = Column(String, primary_key=True)
    abilityKills = Column(Integer)
    activitiesEntered = Column(Integer)
    activitiesWon = Column(Integer)
    allParticipantsCount = Column(Integer)
    allParticipantsScore = Column(Integer)
    allParticipantsTimePlayed = Column(Integer)
    assists = Column(Integer)
    averageKillDistance = Column(Float)
    averageLifespan = Column(Float)
    averageDeathDistance = Column(Float)
    averageScorePerKill = Column(Float)
    averageScorePerLife = Column(Float)
    bestSingleGameKills = Column(Integer)
    bestSingleGameScore = Column(Integer)
    closeCalls = Column(Integer)
    combatRating = Column(Float)
    deaths = Column(Integer)
    defensiveKills = Column(Integer)
    dominationKills = Column(Integer)
    highestCharacterLevel = Column(Integer)
    highestLightLevel = Column(Integer)
    kills = Column(Integer)
    killsDeathsAssists = Column(Float)
    killsDeathsRatio = Column(Float)
    longestKillDistance = Column(Integer)
    longestKillSpree = Column(Integer)
    longestSingleLife = Column(Integer)
    mostPrecisionKills = Column(Integer)
    objectivesCompleted = Column(Integer)
    offensiveKills = Column(Integer)
    orbsDropped = Column(Integer)
    orbsGathered = Column(Integer)
    precisionKills = Column(Integer)
    relicsCaptured = Column(Integer)
    remainingTimeAfterQuitSeconds = Column(Integer)
    resurrectionsPerformed = Column(Integer)
    resurrectionsReceived = Column(Integer)
    score = Column(Integer)
    secondsPlayed = Column(Integer)
    suicides = Column(Integer)
    teamScore = Column(Integer)
    totalActivityDurationSeconds = Column(Integer)
    totalDeathDistance = Column(Integer)
    totalKillDistance = Column(Integer)
    weaponBestType = Column(Integer)
    weaponKillsAutoRifle = Column(Integer)
    weaponKillsHandCannon = Column(Integer)
    weaponKillsFusionRifle = Column(Integer)
    weaponKillsGrenade = Column(Integer)
    weaponKillsMachinegun = Column(Integer)
    weaponKillsMelee = Column(Integer)
    weaponKillsPulseRifle = Column(Integer)
    weaponKillsRelic = Column(Integer)
    weaponKillsRocketLauncher = Column(Integer)
    weaponKillsScoutRifle = Column(Integer)
    weaponKillsShotgun = Column(Integer)
    weaponKillsSideArm = Column(Integer)
    weaponKillsSniper = Column(Integer)
    weaponKillsSubmachinegun = Column(Integer)
    weaponKillsSuper = Column(Integer)
    weaponKillsSword = Column(Integer)
    winLossRatio = Column(Float)
    zonesCaptured = Column(Integer)
    zonesNeutralized = Column(Integer)

#class CharacterStatMayhemRumble(Base):
#    __tablename__ = "characterStatMayhemRumble"
#
#class CharacterStatZoneControl(Base):
#    __tablename__ = "characterStatZoneControl"
#
#class CharacterStatRacing(Base):
#    __tablename__ = "characterStatRacing"
#
#class CharacterStatArenaElderChallenge(Base):
#    __tablename__ = "characterStatArenaElderChallenge"
#
#class CharacterStatSupremacy(Base):
#    __tablename__ = "characterStatSupremacy"
#
#class CharacterStatPrivateMatchesAll(Base):
#    __tablename__ = "characterStatPrivateMatchesAll"
#
#class CharacterStatSupremacyRumble(Base):
#    __tablename__ = "characterStatSupremacyRumble"
#
#class CharacterStatSupremacyClash(Base):
#    __tablename__ = "characterStatSupremacyClash"
#
#class CharacterStatSupremacyInferno(Base):
#    __tablename__ = "characterStatSupremacyInferno"
#
#class CharacterStatSupremacyMayhem(Base):
#    __tablename__ = "characterStatSupremacyMayhem"

class ActivityReference(Base):
    __tablename__ = 'activityReference'
    id = Column(Integer, primary_key=True)
    activity_name = Column(String(50))
    activity_type_hash = Column(String(50))

class ActivityTypeReference(Base):
    __tablename__ = 'activityTypeReference'
    id = Column(Integer, primary_key=True)
    activity_type_name = Column(String(50))
    
class ClassReference(Base):
    __tablename__ = 'classReference'
    id = Column(Integer, primary_key=True)
    class_name = Column(String(50))

class WeaponReference(Base):
    __tablename__ = 'weaponReference'
    id = Column(Integer, primary_key=True)
    weapon_name = Column(String(50))
    weapon_type = Column(String(50))
    weapon_rarity = Column(String(50))

class BucketReference(Base):
    __tablename__ = 'bucketReference'
    id = Column(Integer, primary_key=True)
    bucket_name = Column(String(50))

# I will not be including single game tracking for a while, probably. Maybe when D2 gets started I'll ramp it up, but we're going to need some more storage space.
#class Activity(Base):
#    __tablename__ = 'activity'
#    instance_id = Column(Integer, primary_key=True)
#    activity_id = Column(Integer, ForeignKey('activityReference.activity_id'))
#    activityReference = relationship(ActivityReference)
#    reference_id = Column(Integer)
#    #Other activity-specific fields

#class CharacterPlaysActivity(Base):
#    __tablename__ = 'characterPlaysActivity'
#    character_id = Column(Integer, ForeignKey('character.id'), primary_key=True)
#    character = relationship(Character)
#    instance_id = Column(Integer, ForeignKey('activity.instance_id'), primary_key=True)
#    activity = relationship(Activity)
#    #Other character-specific activity related fields

class LastUpdated(Base):
    __tablename__ = 'lastUpdated'
    id = Column(Integer, primary_key=True)
    table_name = Column(String(50))
    last_updated = Column(DateTime)

def initDB(engine):
    Base.metadata.bind = engine
    #Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    # loadConfig for testing purposes
    APP_PATH = "/etc/destinygotg"

    loadConfig()
    initDB(engine)
