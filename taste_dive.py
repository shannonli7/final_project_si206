import json
import requests

API_KEY = "361067-SI206Pro-349C755Q"
def get_songs_from_tastedive(music):
    baseurl = "https://tastedive.com/api/similar"
    paramsd = {}
    paramsd["k"] = API_KEY
    paramsd["q"] = music
    paramsd["limit"] = 10
    paramsd["type"] = music
    paramsd["info"] = 1

    reqs = requests.get(baseurl, paramsd)

    return reqs.json()
#testing
#nested dictionary of related artists printed!
print(get_songs_from_tastedive("The 1975"))