import re
import sqlite3 as lite
import sys

def validateRequest(request):
    trackedStats = '../Leaderboard/TrackedStats/'
    pveStatPath = trackedStats + 'trackedPvEStats.txt'
    pvpStatPath = trackedStats + 'trackedPvPStats.txt'

    databasePath = '../Leaderboard/guardians.db'
    con = lite.connect(databasePath)
    names = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT Name FROM Bungie")
        while True:
            row = cur.fetchone()
            if row == None:
                break
            else:
                names.append(row[0])
    nameString = "|".join(names)
    
    def getValidStats(statPath):
        with open(statPath,'r') as f:
            return "|".join(f.read().split('\n'))[:-1]

    pvpStatString = getValidStats(pvpStatPath)
    pveStatString = getValidStats(pveStatPath)

    pvpRegex = "^pvp (total|avg) ("+pvpStatString+")$"
    pveRegex = "^pve (total|avg) ("+pveStatString+")$"
    pvpVsRegex = "^pvp (total|avg) ("+pvpStatString+") vs ("+nameString+")(, ("+nameString+"))*$"
    pveVsRegex = "^pve (total|avg) ("+pveStatString+") vs ("+nameString+")(, ("+nameString+"))*$"

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
