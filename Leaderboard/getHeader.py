def getHeader():
    with open('./Tokens/header.txt','r') as f:
        header = f.readline().strip()
    return {"X-API-KEY":header}
