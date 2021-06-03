# HackMarathon_MechaHU_5
### Team
MechaHU
### Team members

- Bence Fabó, Budapest University of Technology and Economics
- Mihály Makovsky, Budapest University of Technology and Economics
- Gellért Csapodi, Budapest University of Technology and Economics

# Our project
The aim of our project was to combine some APIs in a cretive and fun way. After some research, we've choosen three APIs to work with: the Microsoft Azure Face Detection API, the Spotify API and the Quote API. 

Our small fun program recognizes the current emotions and mood of the user via a picture taken with a webcam, and according to that, it gives the user a fitting quote from a famous person and recommends some music which matcehs the mood of the user. This way, you can focus on your feelings and think about them with fitting background music and a nice matching quote, or you can simply have fun.

# Detailed description
When the program is launched, the webcam of the user's computer is switched on and a photo is taken of the user.
Next, the Microsoft Azure Face Detection API guesses the current mood and the emotions of the user, and returns the most fitting one, like happiness, sadness, fear, surprise, anger, etc. 
This emotion is passed to the Quote API which comes up with a quote from a famous person about the feeling of the user. This is displayed in the console.
In the next stage, the Spotify API recommends the user some music which fits his/her current mood the best: some elated, nice music for happiness, dark and sourful  songs for sadness, or a powerful heavy metal hit for anger, etc. The user can choose a song from the recommendation list, which is then started via Spotify.

# Further ideas
The program could be boosted by applying further APIs which deal with the emotions of the user, like recommending activites, food or a beer matching his/her mood.
Furthermore, other things could also be guessed from the picture taken of the user: for isntance, if his/her hair seems to be too long, the program could recommend a hairdresser, or required sleeping hours could be advised if the user seems to be tired. 
