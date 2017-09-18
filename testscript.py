import os
import sys
import json
import requests

write_files = True
URL_START = "https://bungie.net/Platform"
APP_PATH = "/etc/destinygotg"

def testscript():
    # Specify a URL
    destinyMembershipId = 4611686018456448671
    characterId = 2305843009266030136
    membershipType = 2
    bungieId = 13340015
    url_start = f"{URL_START}"
    # url_end = f"/Destiny2/{membershipType}/Profile/{destinyMembershipId}/?components=200"
    # url_end = "/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/?groups=3"
    # url_end = "/Destiny2/Stats/AggregateClanStats/1407546/"
    # url_end = f"/Destiny2/{membershipType}/Account/{destinyMembershipId}/Stats/"
    url_end = f"/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/?groups=2"
    # url_end = f"/Destiny2/{membershipType}/Account/{destinyMembershipId}/Stats/?groups=2"
    # url_end = f"/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/Activities/?mode=None"
    # url_end = f"/Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/AggregateActivityStats/"
    # url = f"{URL_START}/GroupV2/{os.environ['BUNGIE_CLANID']}/Members/?currentPage=1"
    # Specify an outfile
    url = url_start + url_end
    out_file = "testJSON.json"
    # Request a JSON
    request_session = requests.Session()
    data = json_request(request_session, url, out_file)
    # Write the JSON

def make_header():
    return {'X-API-KEY':os.environ['BUNGIE_APIKEY']}

def json_request(request_session, url, out_file):
    print(url)
    headers = make_header()
    res = request_session.get(url, headers=headers)
    try:
        data = res.json()
        print(res.text)
    except json.decoder.JSONDecodeError:
        print(res.text)
        return None
    error_stat = data['ErrorStatus']
    if error_stat == "Success":
        if write_files:
            with open(f"JSON/{out_file}","w+") as f:
                json.dump(data, f)
        print("Writing file...")
        return data
    else:
        print("Error Status: " + error_stat)
        return None 

if __name__ == "__main__":
    config = open(f"{APP_PATH}/config", "r").readlines()
    for value in config:
        value = value.strip().split(":")
        os.environ[value[0]] = value[1]
    testscript()
