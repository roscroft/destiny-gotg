import re
import sqlite3 as lite
import sys

def validateRequest(request):
    trackedStats = '../Leaderboard/TrackedStats/'
    pveStatPath = trackedStats + 'trackedPvEStats.txt'
    pvpStatPath = trackedStats + 'trackedPvPStats.txt'

    databasePath = '../Leaderboard/guardians.db'
    con = lite.connect(databasePath)
    destNames = []
    discNames = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT destName FROM Discord")
        while True:
            row = cur.fetchone()
            if row == None:
                break
            else:
                destNames.append(row[0])
        
        cur.execute("SELECT discName FROM Discord")
        while True:
            row = cur.fetchone()
            if row == None:
                break
            else:
                discNames.append(row[0])
    
    discNames = [i for i in discNames if i != None]
    nameString1 = "|".join(destNames)
    nameString2 = "|".join(discNames)
    
    def getValidStats(statPath):
        with open(statPath,'r') as f:
            return "|".join(f.read().split('\n'))[:-1]

    pvpStatString = getValidStats(pvpStatPath)
    pveStatString = getValidStats(pveStatPath)

    pvpRegex = "^pvp (total|avg) ("+pvpStatString+")$"
    pveRegex = "^pve (total|avg) ("+pveStatString+")$"
    pvpVsRegex = "^pvp (total|avg) ("+pvpStatString+") vs (("+nameString1+")|("+nameString2+"))(, (("+nameString1+")|("+nameString2+")))*$"
    pveVsRegex = "^pve (total|avg) ("+pveStatString+") vs (("+nameString1+")|("+nameString2+"))(, (("+nameString1+")|("+nameString2+")))*$"

    pvp = re.compile(pvpRegex)
    pve = re.compile(pveRegex)
    pvpVs = re.compile(pvpVsRegex)
    pveVs = re.compile(pveVsRegex)

    m = pvp.match(request)
    n = pve.match(request)
    o = pvpVs.match(request)
    p = pveVs.match(request)

    if m:
        return 1
    elif n:
        return 2
    elif o:
        return 3
    elif p:
        return 4
    else:
        return 0

if __name__ == "__main__":
    request = "!stat pvp total kills"
    out = validateRequest(request)
    print(out)
