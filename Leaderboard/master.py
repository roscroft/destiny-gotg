#!/usr/bin/python
#Each function from BuildTables is a database function, and reads in .json files from the noted categories, then builds its named database table
#Each function from APIRequests is an API request function, and pulls the corresponding .json files from Bungie's server.
import buildTables as bt
import apiRequests as ar
from Tokens.getHeader import getHeader
from Tokens.getClanId import getClanId
import sys

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

#Header
header = getHeader(headerPath)
#Clan Id
clanId = getClanId(clanIdPath)

#Start of function calls. Needs to follow the proper data flow to ensure that the next step always has the appropriate database or files that it needs.
def fullSetup():
    ar.getClanUserJSONs(clan, header, clanId)     #Step 1 - Pull list of clan members
    bt.buildBungieTable(clan, db)                 #Step 2 - Build Bungie table, listing clan members
    ar.getIndividualUserJSONs(users, db, header)  #Step 3 - Pull user files, using Bungie table
    bt.buildDestinyTable(users, db)               #Step 4 - Build Destiny table, listing user Ids
    ar.getUserStatsJSONs(stats, db, header)       #Step 5 - Pull user stat files, using Destiny table
    bt.buildStatTables(stats, db)                 #Step 6 - Build stat tables, using user stat files

def tablesOnly():
    bt.buildBungieTable(clan, db)                 #Step 2 - Build Bungie table, listing clan members
    bt.buildDestinyTable(users, db)               #Step 4 - Build Destiny table, listing user Ids
    bt.buildStatTables(stats, db)                 #Step 6 - Build stat tables, using user stat files

if __name__ == "__main__":
    args = sys.argv
    if len(args) == 1:
        fullSetup()
    elif args[1] == '1':
        tablesOnly()
    else:
        fullSetup()
