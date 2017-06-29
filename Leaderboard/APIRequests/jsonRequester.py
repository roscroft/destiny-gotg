import json
import requests

def singleJsonRequest(url, header, dumpFileName):
    jsonRequest(url, header, dumpFileName)

def multiJsonRequest(url, header, dumpFileName):
    jsonRequest(url, header, dumpFileName, True)

def jsonRequest(url, header, dumpFileName, multi=False):
    print "Connecting to Bungie: " + url
    pageCounter = 1
    hasMore = True
    while hasMore:
        print "Fetching page " + str(pageCounter)
        res = requests.get(url, header)
        data = res.json()
        error_stat = data['ErrorStatus']
        if error_stat != "Success":
            prinnt "Can't fetch data for " + url
            print "Error Status: " + error_stat
        else:
            with open(dumpFileName+str(pageCounter)+'.json','w') as f:
                json.dump(userData, f)
        if multi:
            hasMore = res.json()['Response']['hasMore']
            morePages = hasMore
            pageCounter+=1
        else:
            hasMore = False
