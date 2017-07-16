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

class PSN(Base):
    __tablename__ = 'psn'
    id = Column(Integer, primary_key=True)
    psnName = Column(String(50), nullable=False)
    bungie_id = Column(Integer, ForeignKey('bungie.id'))
    bungie = relationship(Bungie)

class Xbox(Base):
    __tablename__ = 'xbox'
    id = Column(Integer, primary_key=True)
    xboxName = Column(String(50), nullable = False)
    bungie_id = Column(Integer, ForeignKey('bungie.id'))
    bungie = relationship(Bungie)

class Discord(Base):
    __tablename__ = 'discord'
    id = Column(Integer, primary_key=True)
    discordName = Column(String(50))
    psn_id = Column(Integer, ForeignKey('psn.id'))
    psn = relationship(PSN)
    xbox_id = Column(Integer, ForeignKey('xbox.id'))
    xbox = relationship(Xbox)

engine = create_engine('sqlite:///')

Base.metadata.create_all(engine)
