#!/usr/bin/python
#Each function from BuildTables is a database function, and reads in .json files from the noted categories, then builds its named database table
#Each function from APIRequests is an API request function, and pulls the corresponding .json files from Bungie's server.
from BuildTables.buildBungieTable import buildBungieTable
from BuildTables.buildDestinyTable import buildDestinyTable
from BuildTables.buildPvPTables import buildPvPTables
from BuildTables.buildPvETables import buildPvETables
from APIRequests.getClanUserJSONs import getClanUserJSONs
from APIRequests.getIndividualUserJSONs import getIndividualUserJSONs
from APIRequests.getUserStatsJSONs import getUserStatsJSONs

#Path to Clan data
clan = './Clan/'
#Path to User data
users = './Users/'
#Path to Stats data
stats = './Stats/'

#Path to database
db = './guardians.db'

#Path to header file
headerPath = './Tokens/header.txt'
#Path to ClanId file
clanIdPath = './Tokens/clanId.txt'

def getHeader(headerPath):
    with open(headerPath,'r') as f:
        header = f.readline().strip()
    return {"X-API-KEY":header}

def getClanId(clanIdPath):
    with open(clanIdPath, 'r') as f:
        clanId = f.readline().strip()
    return clanId

#Header
header = getHeader(headerPath)
#Clan Id
clanId = getClanId(clanIdPath)

#Start of function calls. Needs to follow the proper data flow to ensure that the next step always has the appropriate database or files that it needs.
getClanUserJSONs(clan, header, clanId)     #Step 1 - Pull list of clan members
buildBungieTable(clan, db)                 #Step 2 - Build Bungie table, listing clan members
getIndividualUserJSONs(users, db, header)  #Step 3 - Pull user files, using Bungie table
buildDestinyTable(users, db)               #Step 4 - Build Destiny table, listing user Ids
getUserStatsJSONs(stats, db, header)       #Step 5 - Pull user stat files, using Destiny table
buildPvPTables(stats, db)                  #Step 6 - Build PvP tables, using user stat files
buildPvETables(stats, db)                  #Step 7 - Build PvE tables, using user stat files
