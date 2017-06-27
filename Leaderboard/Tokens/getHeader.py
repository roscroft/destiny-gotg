def getHeader(headerPath):
    with open(headerPath,'r') as f:
        header = f.readline().strip()
    return {"X-API-KEY":header}
