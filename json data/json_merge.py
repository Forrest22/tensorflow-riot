import json, urllib.request
import jsonmerge, numpy

path = "C:\\Users\\doddfm14\\Documents\\CS 391\\Riot-API\\json data\\"

seed = "https://s3-us-west-1.amazonaws.com/riot-developer-portal/seed-data/"

# data

# for x in range(1,3):
    # url = "URL: " + seed + "matches" + str(x) + ".json"
filename = path + "matches200.json"
with open(filename) as j:
    data = json.loads(j.read())
    # print(data)
    print(data[0]["0"]["teams"][0]["firstBlood"])
    print(data[0]["0"]["teams"][0]["firstTower"])
    # for x in range(0,100):

