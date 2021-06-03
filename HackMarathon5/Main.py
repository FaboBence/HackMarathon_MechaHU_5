import Microsoft_Face_API
import Spotify_API
import Quote_API

if __name__ == '__main__':
	emotion = Microsoft_Face_API.Emotion_recognition()
	Spotify_API.Spotify_Search(emotion)
	print(Quote_API.random_quote(emotion))
