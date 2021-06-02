import requests

from azure.cognitiveservices.vision.face import FaceClient
from azure.cognitiveservices.vision.face.models import FaceAttributeType
from msrest.authentication import CognitiveServicesCredentials

# Key for the API
with open("API.txt", "r") as f:
	KEY = f.read()

# Microsoft Face API endpoint
ENDPOINT = 'https://bence.cognitiveservices.azure.com/'

# Create an authenticated FaceClient.
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

#img_url = 'https://upload.wikimedia.org/wikipedia/commons/c/c3/John_F._Kennedy%2C_White_House_color_photo_portrait.jpg' # Kennedy
img_url = 'https://hungarytoday.hu/wp-content/uploads/2020/06/Hide-the-Pain-Harold-prof..jpg' # Hide the pain Harold
face_attributes = ['age', 'gender', 'headPose', 'smile', 'facialHair', 'glasses', 'emotion']

# Emotion detection with Microsoft Face API
detected_faces = face_client.face.detect_with_url(url = img_url, return_face_attributes = face_attributes)

for face in detected_faces:
        print()
        # ID of detected face
        print(face.face_id)
        # Show all facial attributes from the results
        print()
        print('Facial attributes detected:')
        print('Age: ', face.face_attributes.age)
        print('Gender: ', face.face_attributes.gender)
        print('Head pose: ', face.face_attributes.head_pose)
        print('Smile: ', face.face_attributes.smile)
        print('Facial hair: ', face.face_attributes.facial_hair)
        print('Glasses: ', face.face_attributes.glasses)
        print('Emotion: ')
        print('\tAnger: ', face.face_attributes.emotion.anger)
        print('\tContempt: ', face.face_attributes.emotion.contempt)
        print('\tDisgust: ', face.face_attributes.emotion.disgust)
        print('\tFear: ', face.face_attributes.emotion.fear)
        print('\tHappiness: ', face.face_attributes.emotion.happiness)
        print('\tNeutral: ', face.face_attributes.emotion.neutral)
        print('\tSadness: ', face.face_attributes.emotion.sadness)
        print('\tSurprise: ', face.face_attributes.emotion.surprise)
        print()