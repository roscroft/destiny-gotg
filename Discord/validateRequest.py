import re

def validateRequest(request):
    trackedStats = '../Leaderboard/TrackedStats/'
    pveStatPath = trackedStats + 'trackedPvEStats.txt'
    pvpStatPath = trackedStats + 'trackedPvPStats.txt'
    def getValidStats(statPath):
        with open(statPath,'r') as f:
            return "|".join(f.read().split('\n'))[:-1]

    pvpStatString = getValidStats(pvpStatPath)
    pveStatString = getValidStats(pveStatPath)

    pvpRegex = "pvp (total|avg) ("+pvpStatString+")"
    pveRegex = "pve (total|avg) ("+pveStatString+")"

    pvp = re.compile(pvpRegex)
    pve = re.compile(pveRegex)

    m = pvp.match(request)
    n = pve.match(request)
    if not m and not n:
        return False
    return True
