import csv
import json

path = "C:\\Users\\doddfm14\\Documents\\CS 391\\Riot-API\\json data\\"
lines = 800
filename = path + "matches"+str(lines)+".json"
with open(filename) as file:
    x = json.loads(file.read())

    f = csv.writer(open("matches"+str(lines)+"_adv.csv", "w", newline='\n'))

    # Write CSV Header, If you dont need that, remove this line
    # f.writerow(["match", "win", "firstBlood", "firstTower", "firstInhib"])
    # f.writerow(["firstBlood", "firstTower", "firstInhib", "firstDragon", "win"])
    f.writerow([lines,8,"Win","Fail"])
    for i, hundredMatchSet in enumerate(x):
        for ii, match in enumerate(hundredMatchSet):
            data = [
            # count,
            int(x[i][str(ii)]["teams"][0]["firstBlood"]),
            int(x[i][str(ii)]["teams"][0]["firstTower"]),
            int(x[i][str(ii)]["teams"][0]["firstInhibitor"]),
            int(x[i][str(ii)]["teams"][0]["firstDragon"]),
            int(x[i][str(ii)]["teams"][0]["towerKills"]),
            int(x[i][str(ii)]["teams"][0]["inhibitorKills"]),
            int(x[i][str(ii)]["teams"][0]["baronKills"]),
            int(x[i][str(ii)]["teams"][0]["dragonKills"]),
            ]
            for iii in range(5):
                player = [str(x[i][str(ii)]["participants"][iii]["championId"]), str(x[i][str(ii)]["participants"][iii]["stats"]["champLevel"])]
                print(player)
                data.append(player)
            count = (i+1)*(ii+1)
            data.append(int(x[i][str(ii)]["teams"][0]["win"] == "Win"))
            f.writerow(data)