def getClanId(clanIdPath):
    with open(clanIdPath, 'r') as f:
        clanId = f.readline().strip()
    return clanId
