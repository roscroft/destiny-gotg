#!/usr/bin/python

import json
import requests

def getHeader():
    with open('header.txt','r') as f:
        header = f.readline().strip()
    return {"X-API-KEY":header}

def retrieveClanUserJSON():
    morePages = True
    pageCounter = 1
    while morePages:
        clan_url = "https://bungie.net/Platform/Group/1407546/Members/?lc=en&fmt=true&currentPage="+str(pageCounter)+"&platformType=2"
        print "Connecting to Bungie: " + clan_url
        print "Fetching page " + str(pageCounter) + " of users."
        res = requests.get(clan_url, headers=getHeader())
        data = res.json()
        error_stat = data['ErrorStatus']
        print "Error Stats: " + error_stat
        #Stores each page of clan user responses as a different .json
        with open('./Clan/clanUsersPage'+str(pageCounter)+'.json','w') as f:
            json.dump(data,f)
        hasMore = res.json()['Response']['hasMore']
        morePages = hasMore
        pageCounter+=1

def getClanUserJSONs():
    retrieveClanUserJSON()

if __name__ == "__main__":
    getClanUserJSONs()
