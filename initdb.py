import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()
#Bungie, PSN, Xbox, and Discord all have an implicit "user" after the noun, but I omitted it to save space

class Bungie(Base):
    __tablename__ = 'bungie'
    id = Column(Integer, primary_key=True)
    bungieName = Column(String(50), nullable=False)

class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True)
    displayName = Column(String(50), nullable=False)
    bungie_id = Column(Integer, ForeignKey('bungie.id'))
    bungie = relationship(Bungie)
    discord_id = Column(Integer, ForeignKey('discord.id'))
    discord = relationship(Discord)

class Discord(Base):
    __tablename__ = 'discord'
    id = Column(Integer, primary_key=True)
    discordName = Column(String(50))

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    #class = Column(Integer) I don't really care about this one yet
    membership_id = Column(Integer, ForeignKey('account.id'))
    account = relationship(Account)

class PvEAccountStats(Base):
    __tablename__ = 'pveAccountStats'
    membership_id = Column(Integer, primary_key=True, ForeignKey('account.id'))
    account = relationship(Account)
    #add in the shit ton of other stat fields fml

class PvPAccountStats(Base):
    __tablename__ = 'pvpAccountStats'
    membership_id = Column(Integer, primary_key=True, ForeignKey('account.id'))
    account = relationship(Account)
    #literally over a hundred other fields fuck

class Ch

engine = create_engine('sqlite:///')

Base.metadata.create_all(engine)
