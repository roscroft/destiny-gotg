#!/usr/bin/python
import json
import requests
import sys
import os

APP_PATH = "/etc/destinygotg"
URL_START = "https://bungie.net/Platform"

def loadConfig(): 
    """Load configs from the config file""" 
    config = open(f"{APP_PATH}/config", "r").readlines() 
    for value in config: 
        value = value.strip().split(":")
        os.environ[value[0]] = value[1]

def makeHeader():
    return {'X-API-KEY':os.environ['BUNGIE_APIKEY']}

def jSONRequest(url, outFile, message=""):
    print(f"Connecting to Bungie: {url}")
    print(message)
    res = requests.get(url, headers=makeHeader())
    data = res.json()
    error_stat = data['ErrorStatus']
    print("Error Status: " + error_stat)
    if error_stat == "Success":
        with open(outFile,"w+") as f:
            json.dump(data, f)
        return data
    else:
        return None

def getJSON(bungieId, displayName):
    #url = "https://www.bungie.net/Platform/User/GetMembershipsById/"+str(bungieID)+"/2/"
    #url = "https://www.bungie.net/Platform/Destiny/2/Account/"+str(bungieID)+"/Summary/"
    #url = "https://www.bungie.net/Platform/User/GetBungieAccount/"+str(bungieID)+"/2/"
    #url = "https://www.bungie.net/Platform/Destiny/2/Account/"+str(bungieID)+"/Character/2305843009379090568/"
    #url = "https://www.bungie.net/Platform/Destiny/Stats/AggregateActivityStats/2/"+str(bungieID)+"/2305843009379090568/"
    #url = "https://www.bungie.net/Platform/Destiny/Stats/AggregateActivityStats/2/"+str(bungieID)+"/2305843009265556749/"
    #url = "https://www.bungie.net/Platform/Destiny/Stats/ActivityHistory/2/"+str(bungieID)+"/2305843009379090568/?mode=MayhemClash"
    #url = "https://www.bungie.net/Platform/Destiny/Stats/ActivityHistory/2/"+str(bungieID)+"/2305843009265556749/?mode=MayhemClash"
    pageCount = 1
    #url = f"{URL_START}/Group/{os.environ['BUNGIE_CLANID']}/Membersv3/?lc=en&fmt=true&currentPage={pageCount}&platformType=2"
    
    #url = f"{URL_START}/User/GetMembershipsById/{bungieId}/254/"
    #url = f"{URL_START}/Destiny/Manifest"
    url = f"{URL_START}/Destiny/2/Account/4611686018456448671/Summary/?definitions=True"
    outFile = 'accountSummary.json'
    jSONRequest(url, outFile)

if __name__ == "__main__":
    loadConfig()
    bungieID = 10349404
    displayName = ""
    getJSON(bungieID, displayName)
