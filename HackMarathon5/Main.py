import Microsoft_Face_API
import Spotify_API

if __name__ == '__main__':
	emotion = Microsoft_Face_API.Emotion_recognition()
	Spotify_API.Spotify_Search(emotion)
