try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

# from urllib2 import Request, urlopen
import json
from pandas.io.json import json_normalize

# path1 = '42.974049,-81.205203|42.974298,-81.195755'
# request=urllib2.Request('http://maps.googleapis.com/maps/api/elevation/json?locations='+path1+'&sensor=false')
# response = urllib2.urlopen(request)

path = "C:\\Users\\doddfm14\\Documents\\CS 391\\Riot-API\\json data\\"

filename = path + "matches200.json"
with open(filename) as j:
    data = j.read()
    data = json.loads(data)
    # print(data)
    # print(data[0]["0"]["teams"][0]["firstBlood"])
    # print(data[0]["0"]["teams"][0]["firstTower"])
    # # for x in range(0,100):
    # elevations = response.read()
    # data = json.loads(elevations)
    # jj = json_normalize(data[0]["0"], "teams", [0]["win", ])
    jj = json_normalize(data)
    jj = json_normalize()
    print(jj)