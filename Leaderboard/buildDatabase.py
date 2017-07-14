#!/usr/bin/python
#Each function from BuildTables is a database function, and reads in .json files from the noted categories, then builds its named database table
#Each function from APIRequests is an API request function, and pulls the corresponding .json files from Bungie's server.
from BuildTables.buildBungieTable import buildBungieTable
from BuildTables.buildDestinyTable import buildDestinyTable
from BuildTables.buildStatTables import buildStatTables
from APIRequests.apiRequests import getClanUserJSONs
from APIRequests.apiRequests import getIndividualUserJSONs
from APIRequests.apiRequests import getUserStatsJSONs
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
    getClanUserJSONs(clan, header, clanId)     #Step 1 - Pull list of clan members
    buildBungieTable(clan, db)                 #Step 2 - Build Bungie table, listing clan members
    getIndividualUserJSONs(users, db, header)  #Step 3 - Pull user files, using Bungie table
    buildDestinyTable(users, db)               #Step 4 - Build Destiny table, listing user Ids
    getUserStatsJSONs(stats, db, header)       #Step 5 - Pull user stat files, using Destiny table
    buildStatTables(stats, db)                 #Step 6 - Build stat tables, using user stat files

def tablesOnly():
    buildBungieTable(clan, db)                 #Step 2 - Build Bungie table, listing clan members
    buildDestinyTable(users, db)               #Step 4 - Build Destiny table, listing user Ids
    buildStatTables(stats, db)                 #Step 6 - Build stat tables, using user stat files

if __name__ == "__main__":
    args = sys.argv
    if len(args) == 1:
        fullSetup()
    elif args[1] == '1':
        tablesOnly()
    else:
        fullSetup()
