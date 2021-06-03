import Microsoft_Face_API
import Spotify_API
import Quote_API
import random
import webbrowser

if __name__ == '__main__':
	# Using API-s
	emotion = Microsoft_Face_API.Emotion_recognition()
	results = Spotify_API.Spotify_Search(emotion)
	Quote_API.random_quote(emotion)

	# Song choice list
	song_list = random.sample(results, 3)
	print('Choose which song do you want to listen to!')
	for i,song in enumerate(song_list):
		print('\t'+str(i+1)+'.', song['artists'][0]['name'],'-',song['name'],';',song['external_urls']['spotify'])
	print('Press the number of the song to play it!')
	selected = int(input())
	print('You selected:',song_list[selected-1]['name'])
	webbrowser.open(song_list[selected-1]['external_urls']['spotify']) # Open song in web browser
