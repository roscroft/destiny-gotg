#This file will read all players' crucible stats and output the aggregated stats corresponding to leaderboard categories
import json
from os import listdir

playerDict = {}

tracked_stats = ["weaponKillsMachinegun","weaponKillsRocketLauncher","weaponKillsSword","weaponKillsSniper","weaponKillsFusionRifle","weaponKillsShotgun","weaponKillsSideArm","weaponKillsScoutRifle","weaponKillsPulseRifle","weaponKillsHandCannon","weaponKillsAutoRifle","weaponKillsMelee","weaponKillsGrenade","weaponKillsSuper","assists","deaths","suicides","averageLifespan","resurrectionsPerformed","resurrectionsReceived","kills","precisionKills","abilityKills","averageKillDistance","longestKillDistance","averageScorePerKill","closeCalls","orbsGathered","orbsDropped","objectivesCompleted","secondsPlayed","winLossRatio","remainingTimeAfterQuitSeconds","score","combatRating","teamScore","allParticipantsScore"]

def addPlayerToStatDict(playerName):
  if playerName != "LutherArkwright":
    with open("./Stats/"+playerName+".json") as data_file:
      agg_data = json.load(data_file)
    pvp_stats = agg_data['Response']['mergedAllCharacters']['results']['allPvP']['allTime']
    statDict = {}
    for stat in tracked_stats:
      if stat in ["assists","closeCalls","orbsGathered"]:
        statDict.update({stat:pvp_stats[stat]['pga']['value']})
      else:
        statDict.update({stat:pvp_stats[stat]['basic']['value']})
    playerDict.update({playerName:statDict})

def buildLeaderboard():
  #Making a dictionary of all leaderboard categories, key is category name, value is tuple of (playername, value)
  leaderboard = {}

  def upd(categoryName, statNameList, func=idt, startVal=0): 
   leaderboard.update({categoryName:maxStats(statNameList, func, startVal)})

  upd("Machine Lord",["weaponKillsMachinegun"])
  upd("Splash Damage",["weaponKillsRocketLauncher"])
  upd("Sword at a Gun Fight",["weaponKillsSword"])
  upd("Marksman",["weaponKillsSniper"])
  upd("Master Blaster",["weaponKillsFusionRifle"])
  upd("Buckshot Bruiser",["weaponKillsShotgun"])
  upd("Sidekick",["weaponKillsSideArm"])
  upd("Scout's Honor",["weaponKillsScoutRifle"])
  upd("Finger on the Pulse",["weaponKillsPulseRifle"])
  upd("Dead Man's Hand",["weaponKillsHandCannon"])
  upd("Automatic",["weaponKillsAutoRifle"])
  upd("Stick Around",["weaponKillsMelee"])
  upd("Get it Off",["weaponKillsGrenade"])
  upd("Superhero",["weaponKillsSuper"])
  
  upd("Two (or more) to the Morgue",["deaths"])
  upd("No Old and Bold Guardians",["averageLifespan"])
  upd("One Shot, One Kill",["precisionKills","kills","abilityKills"],precKillRatio)
  upd("Close Killer",["averageKillDistance"],invdt,-2000000000)
  upd("Close Caller",["closeCalls"])
  upd("Supercharged",["orbsGathered"])
  upd("Objectively Correct",["objectivesCompleted"])
  upd("Outside? What's that?",["secondsPlayed"])
  upd("This One's for Solid",["suicides"])#I'll do it Myself
  upd("Can't Stop Winning",["winLossRatio"])
  upd("Quitter",["remainingTimeAfterQuitSeconds"])
  upd("Top of the Leaderboard",["score"])
  upd("Up Close and Personal",["weaponKillsMelee","kills"],divOverTotal)
  upd("Numbers Speak for Themselves",["combatRating"])
  upd("Eagle Eye",["longestKillDistance"])
  upd("Efficiency is Key",["averageScorePerKill"])
  upd("Team Player",["score","teamScore"],divOverTotal)
  upd("The Best Around",["score","allParticipantsScore"],divOverTotal)
  upd("Who Needs Guns?",["abilityKills","kills"],divOverTotal)
  upd("I am Become Death",["kills"])
  upd("I Helped!",["assists"])
  upd("Last Guardian Standing",["resurrectionsPerformed","resurrectionsReceived"],divOverTotal)
  upd("Mayhem",["weaponKillsSuper","kills"],divOverTotal)
  upd("Support Role",["orbsDropped"])
  upd("Pull the Pin (nerf lightnings plz)",["weaponKillsGrenade","kills"],divOverTotal)
  
  return leaderboard

def maxStats(statNameList, func, startVal):
  maxInfo = (startVal, "")
  for playerName, statDict in playerDict.items():
    playerStats = []
    for statName in statNameList:
      playerStats.append(statDict[statName])
    playerStatVal = func(playerStats)
    #print playerName + ": " + str(playerStatVal)
    if playerStatVal > maxInfo[0]:
      maxInfo = (playerStatVal, playerName)
  if startVal == 0:
    return maxInfo
  else:
    return (maxInfo[0]*-1,maxInfo[1])
# For minimum values - go negative!!

def idt(playerStats):
  return playerStats[0]

def invdt(playerStats):
  return -1*playerStats[0]

#Needs precision kills, kills, ability kills in that order
def precKillRatio(playerStats):
  return playerStats[0]/(playerStats[1]-playerStats[2])

#Needs stat of interest, total stat in that order
def divOverTotal(playerStats):
  if playerStats[1] == 0:
    return playerStats[0]
  else:
    return playerStats[0]/playerStats[1]

def getAvailablePlayers():
  nameList = []
  with open("playerStatsAvailable.txt",'r') as names:
    nameList = names.read().split("\n")[:-1]
  return nameList

if __name__ == "__main__":
  nameList = getAvailablePlayers()
  for name in nameList:
    addPlayerToStatDict(name)
  leaderboard = buildLeaderboard()
  for (cat, playerInfo) in leaderboard.items():
    print cat + ": " + playerInfo[1] + ", " + str(playerInfo[0])
  with open("../Discord/leaderboard.txt",'w') as f:
    for (cat, playerInfo) in leaderboard.items():                   
      f.write(cat + ": " + playerInfo[1] + ", " + str(playerInfo[0])+"\n")

