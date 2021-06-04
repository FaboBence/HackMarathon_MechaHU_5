import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def Spotify_Search(emotion):
    # Spotify API
    cid = 'f897163015af463cad929365808bf881'    # Endpoint
    with open("Spotify_API.txt","r") as f:
        KEY_SPOTIFY = f.read()                  # Key

    # Emotion -> Playlist dictionary
    playlist_dict = {'happiness': ['Bence','4BiXda1TWLMG301vICPvAG'],
                     'sadness': ['Bence','0FF7u1u9wdeHFOd4Lns2oL'],
                     'anger': ['Bence','3gbGsBHj1o3Gx7Pr8JuLsa'],
                     'neutral': ['Bence','5UtB4Fk6XQyUvlboAZkgfu'],
                     'surprise': ['firegaze','6SxqdKdDe7DYf2uPeSQ0Ft'],
                     'fear': ['Bence','4hGSBWGpk6ASYTqa0GCfLy']}
    
    # Search
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=KEY_SPOTIFY)
    spotify = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    #results = spotify.search(q = emotion, type = 'track', limit = 20)
    results = spotify.user_playlist(user = playlist_dict[emotion][0], playlist_id = playlist_dict[emotion][1])

    return results['tracks']['items']