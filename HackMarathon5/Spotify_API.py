import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def Spotify_Search(emotion):
    # Spotify API
    cid = 'f897163015af463cad929365808bf881'    # Endpoint
    with open("Spotify_API.txt","r") as f:
        KEY_SPOTIFY = f.read()                  # Key
    
    # Search
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=KEY_SPOTIFY)
    spotify = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    results = spotify.search(q = emotion, type = 'track', limit = 10)
    print('Song:',results['tracks']['items'][0]['name'],'\nLink:', results['tracks']['items'][0]['external_urls']['spotify'])