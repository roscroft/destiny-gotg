#!/usr/bin/env python
import os
import sys
import model

APP_PATH = "/etc/destinygotg"

def main():
    """Run the application"""
    if not verifyPythonVersion():
        print("This app requires python 3.6 or greater!")
        return
    setAppPath()
    if not os.path.exists(f"{APP_PATH}/config"):
        generateConfig()
    loadConfig()

def setAppPath():
    if not os.path.isdir(APP_PATH):
        os.mkdir(APP_PATH)

def verifyPythonVersion():
    """Ensure the script is being run in python 3.6"""
    try:
        # use assert to throw an exception if
        # the python version is less than 3.6
        assert sys.version_info >= (3, 6)
        return True
    except AssertionError:
        return False

def generateConfig():
    """Generate and store a new config file"""
    # make sure the APP_PATH directory exists
    config = open(f"{APP_PATH}/config", "w+")
    apikey = input("Please enter your Bungie API Key: ")
    clanid = input("Please enter your Clan ID: ")
    config.write(f"BUNGIE_APIKEY:{apikey}\n")
    config.write(f"BUNGIE_CLANID:{clanid}\n")
    config.write(f"DBPATH:{APP_PATH}/guardians.db\n")
    config.close()

def loadConfig():
    """Load configs from the config file"""
    config = open(f"{APP_PATH}/config", "r").readlines()
    for value in config:
        value = value.strip().split(":")
        os.environ[value[0]] = value[1]

if __name__ == "__main__":
    main()
