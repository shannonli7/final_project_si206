import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#each of the artist's unique uri from Spotify app
artist1_uri = 'spotify:artist:3mIj9lX2MWuHmhNCA7LSCW'

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
#def get_followers():

print(get_tracks(artist1_uri))