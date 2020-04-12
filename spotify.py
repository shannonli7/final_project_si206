import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#each of the artist's unique uri from Spotify app
#the 1975
artist1_uri = 'spotify:artist:3mIj9lX2MWuHmhNCA7LSCW'
#the japanese house
artist2_uri = 'spotify:artist:3IunaFjvNKj98JW89JYv9u'
#bleachers
artist3_uri = 'spotify:artist:2eam0iDomRHGBypaDQLwWI'
#lauv
artist4_uri = 'spotify:artist:5JZ7CnR6gTvEMKX4g70Amv'
#two door cinema club
artist5_uri = 'spotify:artist:536BYVgOnRky0xjsPT96zl'
#conan gray
artist6_uri = 'spotify:artist:4Uc8Dsxct0oMqx0P6i60ea'
#the wombats
artist7_uri = 'spotify:artist:0Ya43ZKWHTKkAbkoJJkwIB'
#the band CAMINO
artist8_uri = 'spotify:artist:6d4jrmreCmsenscuieJERc'
#flor
artist9_uri = 'spotify:artist:0szWPxzzE8DVEfXFRCLBUb'
#Lorde
artist10_uri = 'spotify:artist:163tK9Wjr9P9DmM0AVK7lm'

#set SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials("17f86f3cbfd64d5e8d650c809760fee0", "315a2c5b3f924ef6bf86af634ff4dce1"))
#predefined functions of spotify's api

def get_tracks(artist_uri):
    dictionary = {}
    lst_of_tracks = []
    results = spotify.artist_top_tracks(artist_uri)
    for track in results['tracks'][:10]:
        lst_of_tracks.append(track["name"])
    artist_name = results["tracks"][0]["album"]["artists"][0]["name"]
    dictionary[artist_name] = lst_of_tracks
    return dictionary

#total number of followers given
#result = spotify.search(q="The 1975", limit = 2, offset=0, type="artist")
#print(result["artists"]["items"][0]["followers"]["total"])
def get_followers(dictionary_from_tracks):
    name = list(dictionary_from_tracks.keys())[0]
    result = spotify.search(q=name, limit = 2, offset=0, type="artist")
    return result["artists"]["items"][0]["followers"]["total"]

#from the iTunes API
track_prices1 = [1.29, 1.29, 1.29, 1.29, 1.29, 1.29, 1.99, 1.29, 1.99, 1.29]
track_prices2 = [1.29, 1.29, 1.29, 1.29, 1.99, 1.29, 1.29, 1.99, 1.29, 1.29]
track_prices3 = [1.29, 1.29, 1.99, 1.29, 1.00, 1.29, 1.29, 1.99, 1.29, 1.29]
track_prices4 = [1.00, 1.29, 1.99, 1.29, 0.99, 0.99, 1.29, 1.99, 1.29, 1.29]
track_prices5 = [1.29, 1.29, 1.29, 1.99, 1.29, 1.29, 1.00, 1.29, 1.29, 1.29]
track_prices6 = [1.29, 1.99, 1.00, 1.29, 1.29, 1.99, 1.29, 1.29, 0.69, 1.29]
track_prices7 = [1.29, 1.29, 1.29, 1.29, 1.29, 1.29, 1.29, 1.29, 1.29, 1.29]
track_prices8 = [1.29, 1.29, 1.29, 0.99, 1.29, 1.29, 1.29, 1.29, 1.29, 1.29]
track_prices9 = [0.99, 1.29, 0.69, 1.29, 0.99, 0.99, 0.99, 0.99, 0.99, 0.99]
track_prices10 = [1.29, 1.29, 1.00, 1.29, 1.29, 1.29, 1.29, 1.29, 1.29, 1.29]

#gather data into a dictionary 
lst_of_dictionary = []
artist1 = get_tracks(artist1_uri)
artist1["followers"] = get_followers(artist1) #3922606
artist1["track_prices"] = track_prices1
lst_of_dictionary.append(artist1)


artist2 = get_tracks(artist2_uri)
artist2["followers"] = get_followers(artist2) #354715
artist2["track_prices"] = track_prices2
lst_of_dictionary.append(artist2)

artist3 = get_tracks(artist3_uri)
artist3["followers"] = get_followers(artist3) #364344
artist3["track_prices"] = track_prices3
lst_of_dictionary.append(artist3)

artist4 = get_tracks(artist4_uri)
artist4["followers"] = get_followers(artist4) #2589051
artist4["track_prices"] = track_prices4
lst_of_dictionary.append(artist4)

artist5 = get_tracks(artist5_uri)
artist5["followers"] = get_followers(artist5) #1833816
artist5["track_prices"] = track_prices5
lst_of_dictionary.append(artist5)

artist6 = get_tracks(artist6_uri)
artist6["followers"] = get_followers(artist6) #951347
artist6["track_prices"] = track_prices6
lst_of_dictionary.append(artist6)

artist7 = get_tracks(artist7_uri)
artist7["followers"] = get_followers(artist7) #761801
artist7["track_prices"] = track_prices7
lst_of_dictionary.append(artist7)

artist8 = get_tracks(artist8_uri)
artist8["followers"] = get_followers(artist8) #151465
artist8["track_prices"] = track_prices8
lst_of_dictionary.append(artist8)

artist9 = get_tracks(artist9_uri)
artist9["followers"] = get_followers(artist9) #3648080
artist9["track_prices"] = track_prices9
lst_of_dictionary.append(artist9)

artist10 = get_tracks(artist10_uri)
artist10["followers"]= get_followers(artist10) #5626478
artist10["track_prices"] = track_prices10
lst_of_dictionary.append(artist10)

print(lst_of_dictionary)

track_uri = "spotify:track:035QPHPAcqApSGMMcogT45"
#Audio Analysis of A Change of Heart by The 1975 or Visualization
audio_result = spotify.audio_analysis(track_uri)
#loudness or confidence of the track overtime
#print(audio_result["segments"])
temp_confidence = []
confidence = []
for level in audio_result["segments"]:
    temp_confidence.append(level["confidence"])
count = 10
for c in range(len(temp_confidence)):
    if count > len(temp_confidence) - 1:
        break
    confidence.append(temp_confidence[count])
    count += 10

temp_duration = []
duration = []
for level in audio_result["segments"]:
    temp_duration.append(level["duration"])
count = 10
for d in range(len(temp_duration)):
    if count > len(temp_duration) - 1:
        break
    duration.append(temp_duration[count])
    count += 10









