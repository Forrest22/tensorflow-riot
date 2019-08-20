import json
import csv

lines = 800
filename = "matches" + str(lines) + ".json"

data = {}
data["games"] = []

# Opens each game and reorganizes
with open(filename) as file:
	matches_json = json.loads(file.read())
	for block in matches_json:
		for x in range(0,100):
			data["games"].append(block[str(x)])

# Saves new file of data
with open("matches" + str(lines) + "_clean.json", "w") as outfile:
    json.dump(data, outfile)