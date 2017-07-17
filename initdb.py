#!/usr/bin/python
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
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

class PvEAccountStats(Base):
    __tablename__ = 'pveAccountStats'
    membership_id = Column(Integer, ForeignKey('account.id'), primary_key=True)
    account = relationship(Account)

class PvPAccountStats(Base):
    __tablename__ = 'pvpAccountStats'
    membership_id = Column(Integer, ForeignKey('account.id'), primary_key=True)
    account = relationship(Account)
    #literally over a hundred other fields fuck

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    #class = Column(Integer) I don't really care about this one yet
    membership_id = Column(Integer, ForeignKey('account.id'))
    account = relationship(Account)

class ActivityReference(Base):
    __tablename__ = 'activityReference'
    activity_id = Column(Integer, primary_key=True)
    activity_name = Column(String(50))

class Activity(Base):
    __tablename__ = 'activity'
    instance_id = Column(Integer, primary_key=True)
    activity_id = Column(Integer, ForeignKey('activityReference.activity_id'))
    activityReference = relationship(ActivityReference)
    reference_id = Column(Integer)
    #Other activity-specific fields

class CharacterPlaysActivity(Base):
    __tablename__ = 'characterPlaysActivity'
    character_id = Column(Integer, ForeignKey('character.id'), primary_key=True)
    character = relationship(Character)
    instance_id = Column(Integer, ForeignKey('activity.instance_id'), primary_key=True)
    activity = relationship(Activity)
    #Other character-specific activity related fields

#print(f"sqlite:///{os.environ['DBPATH']}")
engine = create_engine(f"sqlite:///{os.environ['DBPATH']}")
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
