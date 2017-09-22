#!/usr/bin/python
"""Model for the app, handles the manifest and all database operations."""
import os
import zipfile
import shutil

import requests

import initdb
import builddb
import discordbot

def check_db():
    """Check to see if a database exists"""
    return os.path.isfile(os.environ['DB_NAME'])

def init_db(opts):
    """Sets up the tables for the database"""
    initdb.init_db(opts)

def check_manifest():
    """Check to see if manifest file exists"""
    return os.path.isfile(os.environ['MANIFEST_NAME'])

def get_manifest():
    """Pulls the requested definitions into the manifest database"""
    manifest_url = "http://www.bungie.net/Platform/Destiny2/Manifest/"
    res = requests.get(manifest_url)
    manifest = res.json()
    mani_url = f"http://www.bungie.net/{manifest['Response']['mobileWorldContentPaths']['en']}"
    #Download the file, write it to MANZIP
    res = requests.get(mani_url)
    with open(f"{os.environ['APP_PATH']}/MANZIP", "wb") as zip_file:
        zip_file.write(res.content)
    #Extract the file contents, and rename the extracted file
    with zipfile.ZipFile(f"{os.environ['APP_PATH']}/MANZIP") as zip_file:
        name = zip_file.namelist()
        zip_file.extractall()
    shutil.move(name[0], f"{os.environ['APP_PATH']}/{os.environ['MANIFEST_NAME']}")

def build_db(opts):
    """Main function to build the full database"""
    builddb.build_db(opts)

def run_discord():
    """Runs the Discord bot"""
    discordbot.run_bot()
