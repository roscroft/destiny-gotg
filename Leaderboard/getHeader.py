def getHeader():
    with open('header.txt','r') as f:
        header = f.readline().strip()
    return {"X-API-KEY":header}
