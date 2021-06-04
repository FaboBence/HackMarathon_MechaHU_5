import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def Spotify_Search(emotion):
    # Spotify API
    cid = 'f897163015af463cad929365808bf881'    # Endpoint
    with open("Spotify_API.txt","r") as f:
        KEY_SPOTIFY = f.read()                  # Key

    # Emotion -> Playlist dictionary
    playlist_dict = {'happiness': ['spotify','37i9dQZF1DX3rxVfibe1L0'],
                     'sadness': ['spotify','37i9dQZF1DX7qK8ma5wgG1'],
                     'anger': ['spotify','37i9dQZF1DX9qNs32fujYe'],
                     'neutral': ['LoudCult','50Lt6hOGx8rENluTGRwskm'],
                     'surprise': ['firegaze','6SxqdKdDe7DYf2uPeSQ0Ft'],
                     'fear': ['Meditation Station','7LI3zw8HLkjKo5YpvA26KG']}
    
    # Search
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=KEY_SPOTIFY)
    spotify = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    #results = spotify.search(q = emotion, type = 'track', limit = 20)
    results = spotify.user_playlist(user = playlist_dict[emotion][0], playlist_id = playlist_dict[emotion][1])

    return results['tracks']['items']