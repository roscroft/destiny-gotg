
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
