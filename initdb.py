#!/usr/bin/python
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

#load env vars for testing purposes
APP_PATH = "/etc/destinygotg"
def loadConfig(): 
    """Load configs from the config file""" 
    config = open(f"{APP_PATH}/config", "r").readlines() 
    for value in config: 
        value = value.strip().split(":") 
        os.environ[value[0]] = value[1]

loadConfig()

Base = declarative_base()

class Bungie(Base):
    __tablename__ = 'bungie'
    id = Column(String(50), primary_key=True)
    bungie_name = Column(String(50), nullable=False)
    membership_type = Column(Integer, nullable=False)

class Discord(Base):
    __tablename__ = 'discord'
    id = Column(Integer, primary_key=True)
    discord_name = Column(String(50))

class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True)
    display_name = Column(String(50), nullable=False)
    membership_type = Column(Integer, nullable=False)
    bungie_id = Column(String(50), ForeignKey('bungie.id'))
    bungie = relationship(Bungie)
    discord_id = Column(Integer, ForeignKey('discord.id'))
    discord = relationship(Discord)

class PvETotal(Base):
    __tablename__ = 'pveTotal'
    membership_id = Column(Integer, ForeignKey('account.id'), primary_key=True)
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
    zonesNeutralized = Column(Integer)

class PvEAverage(Base):
    __tablename__ = 'pveAverage'
    membership_id = Column(Integer, ForeignKey('account.id'), primary_key=True)
    account = relationship(Account)
    abilityKills = Column(Float)
    assists = Column(Float)
    deaths = Column(Float)
    kills = Column(Float)
    objectivesCompleted = Column(Float)
    orbsDropped = Column(Float)
    orbsGathered = Column(Float)
    precisionKills = Column(Float)
    publicEventsCompleted = Column(Float)
    publicEventsJoined = Column(Float)
    remainingTimeAfterQuitSeconds = Column(Float)
    resurrectionsPerformed = Column(Float)
    resurrectionsReceived = Column(Float)
    secondsPlayed = Column(Float)
    suicides = Column(Float)
    totalActivityDurationSeconds = Column(Float)
    weaponKillsAutoRifle = Column(Float)
    weaponKillsHandCannon = Column(Float)
    weaponKillsFusionRifle = Column(Float)
    weaponKillsGrenade = Column(Float)
    weaponKillsMachinegun = Column(Float)
    weaponKillsMelee = Column(Float)
    weaponKillsPulseRifle = Column(Float)
    weaponKillsRelic = Column(Float)
    weaponKillsRocketLauncher = Column(Float)
    weaponKillsScoutRifle = Column(Float)
    weaponKillsShotgun = Column(Float)
    weaponKillsSideArm = Column(Float)
    weaponKillsSniper = Column(Float)
    weaponKillsSubmachinegun = Column(Float)
    weaponKillsSuper = Column(Float)
    weaponKillsSword = Column(Float)
    zonesCaptured = Column(Float)
    zonesNeutralized = Column(Float)

class PvPTotal(Base):
    __tablename__ = 'pvpTotal'
    membership_id = Column(Integer, ForeignKey('account.id'), primary_key=True)
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

class PvPAverage(Base):
    __tablename__ = 'pvpAverage'
    membership_id = Column(Integer, ForeignKey('account.id'), primary_key=True)
    account = relationship(Account)
    abilityKills = Column(Float)
    assists = Column(Float)
    closeCalls = Column(Float)
    deaths = Column(Float)
    dominationKills = Column(Float)
    kills = Column(Float)
    objectivesCompleted = Column(Float)
    offensiveKills = Column(Float)
    orbsDropped = Column(Float)
    orbsGathered = Column(Float)
    precisionKills = Column(Float)
    relicsCaptured = Column(Float)
    remainingTimeAfterQuitSeconds = Column(Float)
    resurrectionsPerformed = Column(Float)
    resurrectionsReceived = Column(Float)
    score = Column(Float)
    secondsPlayed = Column(Float)
    suicides = Column(Float)
    teamScore = Column(Float)
    totalActivityDurationSeconds = Column(Float)
    weaponKillsAutoRifle = Column(Float)
    weaponKillsHandCannon = Column(Float)
    weaponKillsFusionRifle = Column(Float)
    weaponKillsGrenade = Column(Float)
    weaponKillsMachinegun = Column(Float)
    weaponKillsMelee = Column(Float)
    weaponKillsPulseRifle = Column(Float)
    weaponKillsRelic = Column(Float)
    weaponKillsRocketLauncher = Column(Float)
    weaponKillsScoutRifle = Column(Float)
    weaponKillsShotgun = Column(Float)
    weaponKillsSideArm = Column(Float)
    weaponKillsSniper = Column(Float)
    weaponKillsSubmachinegun = Column(Float)
    weaponKillsSuper = Column(Float)
    weaponKillsSword = Column(Float)
    zonesCaptured = Column(Float)
    zonesNeutralized = Column(Float)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    minutes_played = Column(Integer)
    light_level = Column(Integer)    
    membership_id = Column(Integer, ForeignKey('account.id'))
    class_hash = Column(Integer)
    account = relationship(Account)

class CharacterUsesWeapon(Base):
    __tablename__ = 'characterUsesWeapon'
    character_id = Column(Integer, ForeignKey('character.id'), primary_key=True)
    character = relationship(Character)
    weapon_hash = Column(Integer)
    kills = Column(Integer)
    precision_kills = Column(Integer)
    precision_kill_percentage = Column(Float)

class AggregateStatsCharacter(Base):
    __tablename__ = 'aggregateStatsCharacter'
    character_id = Column(Integer, ForeignKey('character.id'), primary_key=True)
    character = relationship(Character)
    activity_hash = Column(Integer)
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

class ActivityReference(Base):
    __tablename__ = 'activityReference'
    activity_hash = Column(Integer, primary_key=True)
    activity_name = Column(String(50))

class ClassReference(Base):
    __tablename__ = 'characterReference'
    class_hash = Column(Integer, primary_key=True)
    class_name = Column(String(50))

class WeaponReference(Base):
    __tablename__ = 'weaponReference'
    weapon_hash = Column(Integer, primary_key=True)
    weapon_name = Column(String(50))

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

#print(f"sqlite:///{os.environ['DBPATH']}")
engine = create_engine(f"sqlite:///{os.environ['DBPATH']}")
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
