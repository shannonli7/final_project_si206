import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import json
import os

#visualization for the artist followers ordered increasingly and average track price

#get artist follower count
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

artist_follower_count = []
for d in lst_of_dictionary:
    followers = d["followers"]
    artist = d["name"]
    artist_follower_count.append((artist, followers))

#sort follower count increasingly
followers_sorted = sorted(artist_follower_count, key= lambda x: x[1])
#obtain just artist names in that order for the graph
artist_sorted = []
for t in followers_sorted:
    artist_sorted.append(str(t[0]))



#get artist average track price
try:
    dir = os.path.dirname(__file__)
    full_path = os.path.join(dir,"average_track_price_per_artist.txt")
    in_file = open(full_path, 'r')
    data = in_file.read()
except:
    print("Problem reading the input file")

#get the text file into a usaable formation
track_price = []
split_data = data.strip().split("\n")
for line in split_data:
    info = line.strip().split(",")
    track_price.append((info[0], info[1]))

#sort the track prices the same as the artists were sorted - the values of track price and follower count will line up for each artist
track_sorted = []
for artist in artist_sorted:
    for track in track_price:
        if track[0] in artist:
            track_sorted.append(float("%.3f" % float(track[1])))


#setting up line graph
fig, ax = plt.subplots()
ax.plot(artist_sorted, track_sorted, color = "#952748", linewidth = 3)
ax.set_facecolor("#ffe7ee")
plt.xticks(rotation=20, family='monospace', weight="semibold", size="small")
ax.set_xlabel("Artists (increasing in order of follower count)")
ax.set_ylabel("Average Track Price", fontname="monospace")
ax.set_title("Average Track Price vs. Artist Follwer Count", fontname="monospace", weight="heavy", size=20)
ax.grid()

#save the figure
fig.savefig("trackprice_vis.png")

plt.show()