# HackMarathon_MechaHU_5
### Team
MechaHU
### Team members

- Bence Fabó, Budapest University of Technology and Economics
- Mihály Makovsky, Budapest University of Technology and Economics
- Gellért Csapodi, Budapest University of Technology and Economics

# Our project
The aim of our project was to combine some APIs in a creative and fun way. After some research, we've choosen three APIs to work with: the Microsoft Azure Face Detection API, the Spotify API and the Quote API.

Our program recognizes the current mood of the user via a picture taken with a webcam, and based on that it gives the user a fitting quote from a famous person and recommends some music.

We made a video about it, check it out!
https://youtu.be/ZioqrRkyJDY

# Detailed description
When the program is launched, the webcam of the user's computer is switched on and a photo is taken of the user.
We feed the photo to the Microsoft Azure Face Detection API, which recognises the current emotion of the user. We only take happiness, sadness, fear, anger and neutral emotion into account.

Happiness: (Bence Fabó)

<p align='center'>
<img height="300" src="https://user-images.githubusercontent.com/65888378/120859746-f0214800-c584-11eb-8437-525178ced50e.png" />
</p>

Anger: (Mihály Makovsky)

<p align='center'>
<img height="300" src="https://user-images.githubusercontent.com/65888378/120842732-61550100-c56d-11eb-8c0a-7e1eb79d61f5.png" />
</p>

Neutral: (Gellért Csapodi)

<p align='center'>
<img height=300 src="https://user-images.githubusercontent.com/65888378/120842813-83e71a00-c56d-11eb-8fe5-211ed286b4fa.png" />
</p>

This emotion is passed on to the Quote API which finds a quote about it from a famous person. This is displayed in the console.

In the next stage, with the help of the Spotify API we find some music which fits the users current mood the best: some fast-paced music for happiness, comforting songs for sadness, or a powerful heavy metal hit for anger, etc. Currently we use hard coded Spotify playlists from which our program can choose three songs randomly. the  The user can choose a song from the recommendation list, which is then automatically opened in the browser on Spotify.

![image](https://user-images.githubusercontent.com/65888378/120860155-83f31400-c585-11eb-85b4-fc41a2a06fe0.png)


# Further ideas
The program could be boosted by applying further APIs which recommend other activites, such as food or a beer matching the current mood of the user.
