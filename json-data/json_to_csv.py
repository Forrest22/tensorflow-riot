import csv
import json
from riotwatcher import RiotWatcher

watcher = RiotWatcher('RGAPI-db258b8d-2384-4c02-863e-9f0a5d66d7be')

my_region = 'na1'

me = watcher.summoner.by_name(my_region, 'Forrest the Fast')
print(json.dumps(me))

path = ""
lines = 200
filename = path + "matches"+str(lines)+".json"
with open(filename) as file:
    x = json.loads(file.read())

    f = csv.writer(open("matches"+str(lines)+"_adv.csv", "w"))

    # Write CSV Header, If you dont need that, remove this line
    # f.writerow(["match", "win", "firstBlood", "firstTower", "firstInhib"])
    # f.writerow(["firstBlood", "firstTower", "firstInhib", "firstDragon", "win"])
    f.writerow([lines*2,10,"Win","Fail"])
    for i, hundredMatchSet in enumerate(x):
        for ii, match in enumerate(hundredMatchSet):
	    platformID = x[i][str(ii)]["platformId"]
            for iii, team in enumerate(match):
	     data = []
             '''
             data = [
             # count,
             int(x[i][str(ii)]["teams"][iii]["firstBlood"]),
             int(x[i][str(ii)]["teams"][iii]["firstTower"]),
             int(x[i][str(ii)]["teams"][iii]["firstInhibitor"]),
             int(x[i][str(ii)]["teams"][iii]["firstDragon"]),
             int(x[i][str(ii)]["teams"][iii]["towerKills"]),
             int(x[i][str(ii)]["teams"][iii]["inhibitorKills"]),
             int(x[i][str(ii)]["teams"][iii]["baronKills"]),
             int(x[i][str(ii)]["teams"][iii]["dragonKills"]),
             ]
             '''
             # gets data based on player
             for playerNum in range(5):
                 # player = [str(x[i][str(ii)]["participants"][iii]["championId"]), str(x[i][str(ii)]["participants"][iii]["stats"]["champLevel"])]
                 # print(iii)
                 # print(playerNum)
                 champID = x[i][str(ii)]["participants"][(iii*5)+playerNum]["championId"]
                 summonerID = x[i][str(ii)]["participantIdentities"][(iii*5)+playerNum]["player"]["summonerId"]
		 try:
                  championMastery = watcher.champion_mastery.by_summoner_by_champion(platformID, summonerID, champID)
		 except Exception as e:
		  print(e)
                 champPoints = championMastery["championPoints"]
                 # player = [champID, champPoints]
		 # print(player)
                 data.append(champID)
                 data.append(champPoints)
             #'''
             count = (i+1)*(ii+1)
             data.append(int(x[i][str(ii)]["teams"][iii]["win"] == "Win"))
             f.writerow(data)
	     # print(data)
