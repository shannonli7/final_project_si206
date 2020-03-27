import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

artist1_uri = 'spotify:artist:3mIj9lX2MWuHmhNCA7LSCW'

#set SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials("17f86f3cbfd64d5e8d650c809760fee0", "315a2c5b3f924ef6bf86af634ff4dce1"))
#predefined functions of spotify's api
results = spotify.artist_top_tracks(artist1_uri)
#result = spotify.audio_analysis("spotify:track:5hc71nKsUgtwQ3z52KEKQk")
#print(result)
#total number of followers given
#result = spotify.search(q="The 1975", limit = 2, offset=0, type="artist")
#print(result)
def get_tracks():
    for track in results['tracks'][:10]:
        print('track    : ' + track['name'])
        #print('audio    : ' + track['preview_url'])
        #print('cover art: ' + track['album']['images'][0]['url'])
