#!/usr/bin/python
from BuildTables.updateDestinyTable import updateDestinyTable
from Tokens.getHeader import getHeader
from APIRequests.getMissingUserJSONs import getMissingUserJSONs
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

#Header
header = getHeader(headerPath)

def getMissing():
    #Specifically, users who are on clan list and thus in table Bungie but not in table Destiny
    missingUsers = True
    while missingUsers:
        #Are any users missing? Function returns true if yes and attempts to get their JSONs
        missingUsers, updatedUsers = getMissingUserJSONs(users, header)
        #If this successfully updates a user, update the database
        
        if updatedUsers != []:
            for username in updatedUsers:
                updateDestinyTable(users, username, db)
        #Otherwise, we loop and keep trying

    #Now, we want to know who is in Destiny but does not have attached stats.
    #TODO

if __name__ == "__main__":
    getMissing()
