import json
import requests

def singleJSONRequest(url, header, dumpFileName, message=""):
    return jSONRequest(url, header, dumpFileName, message)

def multiJSONRequest(url, header, dumpFileName, message=""):
    return jSONRequest(url, header, dumpFileName, message, True)

def jSONRequest(url, header, dumpFileName, message, multi=False):
    print "Connecting to Bungie: " + url
    print message
    pageCounter = 1
    hasMore = True
    exitCodes = []
    while hasMore:
        #print "Fetching page " + str(pageCounter)
        res = requests.get(url, headers=header)
        data = res.json()
        error_stat = data['ErrorStatus']
        print "Error Status: " + error_stat
        if error_stat != "Success":
            print "Error fetching data"
            with open("errorExample.json",'w') as f:
                json.dump(data,f)
            exitCodes.append(0)
        else:
            with open(dumpFileName,'w') as f:
                json.dump(data, f)
            exitCodes.append(1)
        if multi:
            hasMore = res.json()['Response']['hasMore']
            morePages = hasMore
            pageCounter+=1
        else:
            hasMore = False
    if len(exitCodes) == 1:
        return exitCodes[0]
    return exitCodes
