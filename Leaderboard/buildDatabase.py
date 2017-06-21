#!/usr/bin/python
from getClanUserJSONs import getClanUserJSONs
from BuildTables.buildBungieTable import buildBungieTable
from getIndividualUserJSONs import getIndividualUserJSONs
from BuildTables.buildDestinyTable import buildDestinyTable
from getUserStatsJSONs import getUserStatsJSONs
from BuildTables.buildPvPTables import buildPvPTables
from BuildTables.buildPvETables import buildPvETables

#Path to Clan data
clan = './Clan/'
#Path to User data
users = './Users/'
#Path to Stats data
stats = './Stats/'

#Path to database
db = './guardians.db'

#getClanUserJSONs()
buildBungieTable(clan, db)
#getIndividualUserJSONs()
buildDestinyTable(users, db)
#getUserStatsJSONs()
buildPvPTables(stats, db)
buildPvETables(stats, db)
