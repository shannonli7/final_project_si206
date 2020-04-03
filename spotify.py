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
#audio_analysis
#result = spotify.audio_analysis("spotify:track:5hc71nKsUgtwQ3z52KEKQk")
#print(results)s
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
#def get_followers(dictionary_from_tracks):

artist1 = get_tracks(artist1_uri)
artist2 = get_tracks(artist2_uri)
artist3 = get_tracks(artist3_uri)
artist4 = get_tracks(artist4_uri)
artist5 = get_tracks(artist5_uri)
artist6 = get_tracks(artist6_uri)
artist7 = get_tracks(artist7_uri)
artist8 = get_tracks(artist8_uri)
artist9 = get_tracks(artist9_uri)
artist10 = get_tracks(artist10_uri)
# print(artist1)
# print(artist2)
# print(artist3)
# print(artist4)
# print(artist5)
# print(artist6)
# print(artist7)
# print(artist8)
# print(artist9)
# print(artist10)


