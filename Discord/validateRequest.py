import re
import sqlite3 as lite
import sys
sys.path.append('../../')
sys.path.append('../')
import DatabaseModules.databaseStatements as db
import sys

def validateRequest(request):
    trackedStats = '../Leaderboard/TrackedStats/'
    pveStatPath = trackedStats + 'trackedPvEStats.txt'
    pvpStatPath = trackedStats + 'trackedPvPStats.txt'

    databasePath = '../Leaderboard/guardians.db'
    con = lite.connect(databasePath)
    destNames = []
    discNames = []

    req = "SELECT destName FROM Discord"
    destNames2 = db.select(req)
    #This is a list of tuples, so we want to extract the first element from each
    destNames2 = [i[0] for i in destNames2]
    print(destNames2)
    req = "SELECT discName FROM Discord"
    discNames2 = db.select(req)
    discNames2 = [i[0] for i in discNames2]
    print(discNames2)    
    nameString1 = "|".join(destNames2)
    nameString2 = "|".join(discNames2)

    def getValidStats(statPath):
        with open(statPath,'r') as f:
            return "|".join(f.read().split('\n'))[:-1]

    pvpStatString = getValidStats(pvpStatPath)
    pveStatString = getValidStats(pveStatPath)

    pvpRegex = "^pvp (total|avg) ("+pvpStatString+")$"
    pveRegex = "^pve (total|avg) ("+pveStatString+")$"
    pvpVsRegex = "^pvp (total|avg) ("+pvpStatString+") vs (("+nameString1+")|("+nameString2+"))(, (("+nameString1+")|("+nameString2+")))*$"
    pveVsRegex = "^pve (total|avg) ("+pveStatString+") vs (("+nameString1+")|("+nameString2+"))(, (("+nameString1+")|("+nameString2+")))*$"
    pvpAllRegex = "^pvp (total|avg) ("+pvpStatString+") vs all$"
    pveAllRegex = "^pve (total|avg) ("+pveStatString+") vs all$"

    pvp = re.compile(pvpRegex)
    pve = re.compile(pveRegex)
    pvpVs = re.compile(pvpVsRegex)
    pveVs = re.compile(pveVsRegex)
    pvpAll = re.compile(pvpAllRegex)
    pveAll = re.compile(pveAllRegex)

    m = pvp.match(request)
    n = pve.match(request)
    o = pvpVs.match(request)
    p = pveVs.match(request)
    q = pvpAll.match(request)
    r = pveAll.match(request)

    if m:
        return 1
    elif n:
        return 2
    elif o:
        return 3
    elif p:
        return 4
    elif q:
        return 5
    elif r:
        return 6
    else:
        return 0

if __name__ == "__main__":
    request = "!stat pvp total kills"
    out = validateRequest(request)
    print(out)
