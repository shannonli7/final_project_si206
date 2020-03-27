import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

lz_uri = 'spotify:artist:3mIj9lX2MWuHmhNCA7LSCW'

#set SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials("17f86f3cbfd64d5e8d650c809760fee0", "315a2c5b3f924ef6bf86af634ff4dce1"))
results = spotify.artist_top_tracks(lz_uri)

for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    #print('audio    : ' + track['preview_url'])
    #print('cover art: ' + track['album']['images'][0]['url'])
    #print()