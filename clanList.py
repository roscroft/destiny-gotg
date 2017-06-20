import requests
import json
import sqlite3 as lite
import sys


def getHeader():
    with open('header.txt','r') as f:
        header = f.readline().strip()
    return {"X-API-KEY":header}
HEADERS = getHeader()
def getUsersInClan():
    userDict = {}
    morePages = True
    pageCounter = 1 
    while morePages:
        clan_url = "https://bungie.net/Platform/Group/1407546/Members/?lc=en&fmt=true&currentPage="+str(pageCounter)+"&platformType=2"
        print "Connecting to Bungie: " + clan_url
        print "Fetching page " + str(pageCounter) + " of users."
        res = requests.get(clan_url, headers=HEADERS)
        data = res.json()
  
        error_stat = data['ErrorStatus']
        print "Error Stats: " + error_stat
        # Bungie Id and character name

        for result in data['Response']['results']:
            currentUser = str(result['user']['displayName'])
            userDict.update({result['membershipId']:currentUser}) 
    
        hasMore = res.json()['Response']['hasMore']
        morePages = hasMore
        pageCounter+=1
  
    #with open('./Misc/data.json','w') as f:
    #  json.dump(data,f)
    return userDict

def getUserData(userDict):
    userInfoDict={}
    for (bungieID,displayName) in userDict.items():
        user_url = "https://bungie.net/platform/User/GetBungieAccount/"+bungieID+"/254/"
        print "Connecting to Bungie: " + user_url
        print "Fetching user data for " + displayName
        userres = requests.get(user_url, headers=HEADERS)
        userdata = userres.json()
    
    # Membership Id, membership type, all character Ids. Indexed by membership Id, membership type, and display name
    #with open('user.json','w') as f:
    #  json.dump(userdata, f)
    
    #if debugStats:
    #  error_stat = userdata['ErrorStatus']
    #  print "Error Stats: " + error_stat + "\n"
    
        error_stat = userdata['ErrorStatus']
    #print "Error Status: " + error_stat
        
        if error_stat != "Success":
            print "Can't fetch user data for " + displayName
            print "Error Status: " + error_stat
        else:
            characters = userdata['Response']['destinyAccounts'][0]
            characterIds = []
            membershipId = str(characters['userInfo']['membershipId'])
            membershipType = str(characters['userInfo']['membershipType'])
    
            for character in characters:
                characterIds.append(['characterId'])
    
            userKey = (membershipId, membershipType, displayName)
            userInfoDict.update({userKey:characterIds})
    
    return userInfoDict
    #for (indexes, characterIds) in userInfoDict.items():
    #  print displayName + "'s character IDs:"
    #  for characterId in characterIds:
    #    print characterId

def getGeneralStats(userInfoDict):
    for (key, charIds) in userInfoDict.items():
        (memId, memType, disName) = key
        stats_url = "https://bungie.net/platform/Destiny/Stats/Account/"+memType+"/"+memId
        print "Connecting to Bungie: " + stats_url
        print "Fetching aggregate historical stats for " + disName
        statsres = requests.get(stats_url, headers=HEADERS)
        statsdata = statsres.json()
        filename = "./Stats/"+disName+".json" 
        with open(filename,'w') as f:
            json.dump(statsdata, f)



userDict = getUsersInClan()
with open("playerNameListFull.txt",'w') as f:
  for key, value in userDict.items():
    f.write(value+"\n")
userInfoDict = getUserData(userDict)
getGeneralStats(userInfoDict)



#for (bungieID, name) in userDict.items():
#  print name
