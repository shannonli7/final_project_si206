import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import json
import os

#visualization for the number of followers

try:
    dir = os.path.dirname(__file__)
    full_path = os.path.join(dir,"data.json")
    in_file = open(full_path, 'r')
    data = in_file.read()
    lst_of_dictionary = json.loads(data)
    in_file.close()
except:
    print("Problem reading the input file")
    lst_of_dictionary = {}

artistList = []
followersList = []
for dictionary in lst_of_dictionary:
    artist_name = dictionary["name"]
    followers = dictionary["followers"]
    followersList.append(followers)
    artistList.append(artist_name)

#print(artistList)
artists = ('The 1975', 'The Japanese House', 'Bleachers', 'Lauv', 'Two Door Cinema', 'Conan Gray', 'The Wombats', 'The Band CAMINO', 'Flor', 'Lorde')
fig, ax = plt.subplots(figsize=(5, 3))

ax.bar(artists, followersList, color="#6EE37E", edgecolor="#01FCA8")
xlocs, xlabs = plt.xticks()
ax.set_xticks(artists)
ax.set_xticklabels(artists)
plt.xticks(rotation=20, family='monospace', weight="semibold", size="small")
plt.yticks(family='monospace', weight="semibold", size="small")


ax.set_title("Follower Count of Each Artist Recorded from Spotify", fontname="monospace", weight="heavy", size=20)
ax.set_xlabel("Artists", fontname="monospace", weight="bold", color="white", bbox={'facecolor': '#343434', 'alpha': 0.9})
ax.set_ylabel("Number of Followers (Spotify API)", fontname="monospace", weight="bold", color="white", bbox={'facecolor': '#343434', 'alpha': 0.9})
ax = plt.gca()

for i, v in enumerate(followersList):
    plt.text(xlocs[i] - 0.32, v + 0.60, str(v), color="white", weight="black")

ax.set_facecolor('#535353')

# save the figure
fig.savefig("followers_vis.png")
plt.show()




