from os import listdir

def getNamesWithData():
  userStats = [f for f in listdir("./Stats/")]
  userList = []
  for user in userStats:
    userList.append(user[:-5])
  with open ("playerStatsAvailable.txt",'w') as f:
    for user in userList:
      f.write(user+"\n")
  return userList

def getAllPlayerNames():
  nameList = []
  with open("playerNameListFull.txt",'r') as names:
    nameList = names.read().split("\n")[:-1]
  return nameList

def getMissingPlayerNames():
  available = getNamesWithData()
  allnames = getAllPlayerNames()
  missing = list(set(allnames)-set(available))
  with open("playerStatsUnavailable.txt",'w') as f:
    for user in missing:
      f.write(user+"\n")
  return missing

if __name__ == "__main__":
  getMissingPlayerNames()
