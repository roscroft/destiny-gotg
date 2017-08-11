#!/usr/bin/python
import os
import json, sqlite3
import initdb
import builddb
import requests, zipfile
import shutil
import discordController

APP_PATH = "/etc/destinygotg"
DBPATH = f"{APP_PATH}/guardians.db"

def checkDB():
    """Check to see if a database exists"""
    return os.path.isfile(os.environ['DBPATH'])

def initDB(engine):
    """Sets up the tables for the database"""
    initdb.initDB(engine)

def checkManifest():
    """Check to see if manifest file exists"""
    return os.path.isfile(os.environ['MANIFEST_CONTENT'])

def getManifest():
    """Pulls the requested definitions into the manifest database"""
    manifest_url = "http://www.bungie.net/Platform/Destiny/Manifest/"
    r = requests.get(manifest_url)
    manifest = r.json()
    mani_url = f"http://www.bungie.net/{manifest['Response']['mobileWorldContentPaths']['en']}"
    #Download the file, write it to MANZIP
    r = requests.get(mani_url)
    with open(f"{APP_PATH}/MANZIP", "wb") as zip:
        zip.write(r.content)
    #Extract the file contents, and rename the extracted file
    with zipfile.ZipFile(f"{APP_PATH}/MANZIP") as zip:
        name = zip.namelist()
        zip.extractall()
    shutil.move(name[0], os.environ['MANIFEST_CONTENT'])

def buildDB():
    """Main function to build the full database"""
    builddb.buildDB()

def runDiscord(engine):
    discordController.runBot(engine)
