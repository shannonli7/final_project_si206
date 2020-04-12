import json
import requests

API_KEY = "361067-SI206Pro-349C755Q"
def get_dictionary_from_tastedive(music):
    baseurl = "https://tastedive.com/api/similar"
    paramsd = {}
    paramsd["k"] = API_KEY
    paramsd["q"] = music
    paramsd["limit"] = 10
    paramsd["type"] = music

    reqs = requests.get(baseurl, paramsd)
    return reqs.json()

def get_related_artist(artist_name):
    results = get_dictionary_from_tastedive(artist_name)
    lst_of_recommendations = []
    for dictionary in list(results["Similar"]["Results"]):
        lst_of_recommendations.append(dictionary["Name"])
    return lst_of_recommendations

print(get_related_artist("The 1975"))
print(get_related_artist("The Japanese House"))
print(get_related_artist("Bleachers"))
print(get_related_artist("Lauv"))
print(get_related_artist("Two Door Cinema Club"))
print(get_related_artist("Conan Gray"))
print(get_related_artist("The Wombats"))
print(get_related_artist("The Band CAMINO"))
print(get_related_artist("flor"))
print(get_related_artist("Lorde"))

# #returned recommendations
# recommended_artists1  = ['The Neighbourhood', 'Catfish And The Bottlemen', 'Coasts', 'The Neighborhood', 'Lewis Watson', 'Swim Deep', 'Lany', 'Bad Suns', 'Kodaline', 'Saint Raymond']
# recommended_artists2 = ['Phoebe Bridgers', 'Day Wave', 'Pale Waves', 'Boy Pablo', 'Varsity', 'Lany', 'Gus Dapperton', 'Wallows', 'Dandelion Hands', 'Girl In Red']
# recommended_artists3 = ['Hunter Hunted', 'The Griswolds', 'The Colourist', 'Magic Man', "The Mowgli's", 'Ghost Beach', 'Wild Cub', 'Young Rising Sons', 'Smallpools', 'Autoheart']
# recommended_artists4 = ['Quinn Xcii', 'Lany', "Olivia O'brien", 'Yungblud', 'Astrid S', 'Gnash', 'Dean Lewis', 'Wrabel', 'Syml', 'Sasha Sloan']
# recommended_artists5 = ['Bombay Bicycle Club', 'Darwin Deez', 'The Wombats', 'The Temper Trap', 'The Naked And Famous', 'Friendly Fires', 'The Vaccines', 'The Drums', 'San Cisco', 'Miike Snow']
# recommended_artists6 = ['Mxmtoon', 'Sasha Sloan', 'Cavetown', 'Declan Mckenna', 'Girl In Red', 'Fur', 'Wallows', 'Clairo', "Why Don't We", 'Simon Vs. The Homo Sapiens Agenda']
# recommended_artists7 = ['The Pigeon Detectives', 'The Holloways', 'The Hoosiers', 'The Courteeners', 'The Vaccines', 'Milburn', 'The View', 'Jack Peñate', 'The Enemy', 'The Maccabees']
# recommended_artists8 = ['Hayley Kiyoko', 'The Wldlfe', 'Flor', 'Troye Sivan', 'Joan', 'Paramore', 'The Truman Show', 'COIN', 'Smallpools', 'Bad Suns']
# recommended_artists9 = ['Wild Party', 'The Academic', 'Coast Modern', 'Max Frost', 'Grizfolk', 'Cruisr', 'Coin', 'Rina Sawayama', 'Young Rising Sons', 'S Club 7']
# recommended_artists10 = ['Charli Xcx', 'Icona Pop', 'Foxes', 'Tove Lo', 'Haim', 'Sky Ferreira', 'Broods', 'Florence Welch', 'Echosmith', 'Ms Mr']

