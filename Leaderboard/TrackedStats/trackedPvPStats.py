import json

with open('./Stats/Roscroft.json','r') as f:
    with open('trackedPvPStats.txt','w') as g:
        data = json.load(f)
        path = data['Response']['mergedAllCharacters']['results']['allPvP']['allTime']
        sortedStats = []
        for value in path:
            sortedStats.append(value)
        sortedStats = sorted(sortedStats)
        for stat in sortedStats:
            g.write(stat+"\n")
