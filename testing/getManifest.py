import requests, zipfile, os
import json, sqlite3 
#import pickle #Optional

#Reading the Destiny API Manifest in Python. [How I Did It, Anyway]

weapon_types = ['Rocket Launcher', 'Scout Rifle', 'Fusion Rifle', 'Sniper Rifle', 
        'Shotgun', 'Machine Gun', 'Pulse Rifle', 'Auto Rifle', 'Hand Cannon', 'Sidearm']

#dictionary that tells where to get the hashes for each table
#FULL DICTIONARY
hash_dict = {'DestinyActivityDefinition': 'activityHash',
             'DestinyActivityTypeDefinition': 'activityTypeHash',
             #'DestinyClassDefinition': 'classHash',
             #'DestinyGenderDefinition': 'genderHash',
             #'DestinyInventoryBucketDefinition': 'bucketHash',
             #'DestinyInventoryItemDefinition': 'itemHash',
             #'DestinyProgressionDefinition': 'progressionHash',
             #'DestinyRaceDefinition': 'raceHash',
             #'DestinyTalentGridDefinition': 'gridHash',
             #'DestinyUnlockFlagDefinition': 'flagHash',
             'DestinyHistoricalStatsDefinition': 'statId',
             #'DestinyDirectorBookDefinition': 'bookHash',
             'DestinyStatDefinition': 'statHash',
             #'DestinySandboxPerkDefinition': 'perkHash',
             #'DestinyDestinationDefinition': 'destinationHash',
             #'DestinyPlaceDefinition': 'placeHash',
             'DestinyActivityBundleDefinition': 'bundleHash'#,
             #'DestinyStatGroupDefinition': 'statGroupHash',
             #'DestinySpecialEventDefinition': 'eventHash',
             #'DestinyFactionDefinition': 'factionHash',
             #'DestinyVendorCategoryDefinition': 'categoryHash',
             #'DestinyEnemyRaceDefinition': 'raceHash',
             #'DestinyScriptedSkullDefinition': 'skullHash',
             #'DestinyGrimoireCardDefinition': 'cardId'}
            }
def get_manifest():
    manifest_url = 'http://www.bungie.net/Platform/Destiny/Manifest/'
    #get the manifest location from the json
    r = requests.get(manifest_url)
    manifest = r.json()
    mani_url = 'http://www.bungie.net'+manifest['Response']['mobileWorldContentPaths']['en']
    #Download the file, write it to MANZIP
    r = requests.get(mani_url)
    with open("MANZIP", "wb") as zip:
        zip.write(r.content)
    #print("Download Complete!")

    #Extract the file contents, and rename the extracted file
    # to 'Manifest.content'
    with zipfile.ZipFile('MANZIP') as zip:
        name = zip.namelist()
        zip.extractall()
    os.rename(name[0], 'Manifest.content')
    #print('Unzipped!')
               
def build_dict(hash_dict):
    #connect to the manifest
    con = sqlite3.connect('Manifest.content')
    #print('Connected')
    #create a cursor object
    cur = con.cursor()

    all_data = {}
    #for every table name in the dictionary
    for table_name in hash_dict.keys():
        #get a list of all the jsons from the table
        cur.execute('SELECT json from '+table_name)
        #print('Generating '+table_name+' dictionary....')

        #this returns a list of tuples: the first item in each tuple is our json
        items = cur.fetchall()

        #create a list of jsons
        item_jsons = [json.loads(item[0]) for item in items]

        #create a dictionary with the hashes as keys
        #and the jsons as values
        item_dict = {}
        hash = hash_dict[table_name]
        for item in item_jsons:   
            item_dict[item[hash]] = item

        #add that dictionary to our all_data using the name of the table
        #as a key. 
        all_data[table_name] = item_dict 
    #print('Dictionary Generated!')
    return all_data

all_data = build_dict(hash_dict)

for table_name, fields in all_data.items():
    #if table_name == "DestinyActivityDefinition":
    dataList = list(fields.values())
    headerList = [(key,value) for (key,value) in dataList[0].items()]
    print (f"class {table_name}(Base):")
    print (f"    __tablename__ = {table_name}")
    print ("    id = Column(Integer, primary_key=True")
    for header in headerList:
        print (f"    {header} = Column(String(50))")
    print ()
