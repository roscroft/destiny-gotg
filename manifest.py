#!/usr/bin/python
import requests, zipfile, os
import json, sqlite3 
import shutil

APP_PATH = "/etc/destinygotg"

def loadConfig(): 
    """Load configs from the config file""" 
    config = open(f"{APP_PATH}/config", "r").readlines() 
    for value in config: 
        value = value.strip().split(":") 
        os.environ[value[0]] = value[1]

def getManifest():
    manifest_url = "http://www.bungie.net/Platform/Destiny/Manifest/"
    r = requests.get(manifest_url)
    manifest = r.json()
    mani_url = f"http://www.bungie.net/{manifest['Response']['mobileWorldContentPaths']['en']}"
    #Download the file, write it to MANZIP
    r = requests.get(mani_url)
    with open("MANZIP", "wb") as zip:
        zip.write(r.content)
    #Extract the file contents, and rename the extracted file
    with zipfile.ZipFile('MANZIP') as zip:
        name = zip.namelist()
        zip.extractall()
    shutil.move(name[0], os.environ['MANIFEST_CONTENT'])

if __name__ == "__main__":
    loadConfig()
    getManifest()
