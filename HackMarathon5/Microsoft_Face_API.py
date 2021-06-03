import requests
import cv2
from PIL import Image

from azure.cognitiveservices.vision.face import FaceClient
from azure.cognitiveservices.vision.face.models import FaceAttributeType
from msrest.authentication import CognitiveServicesCredentials

def max_emotion(emotions):
    max = emotions.anger
    found = 'anger'
    if emotions.contempt > max:
        max = emotions.contempt
        found = 'contempt'
    if emotions.disgust > max:
        max = emotions.disgust
        found = 'disgust'
    if emotions.fear > max:
        max = emotions.fear
        found = 'fear'
    if emotions.happiness > max:
        max = emotions.happiness
        found = 'happiness'
    if emotions.neutral > max:
        max = emotions.neutral
        found = 'neutral'
    if emotions.sadness > max:
        max = emotions.sadness
        found = 'sadness'
    if emotions.surprise > max:
        max = emotions.surprise
        found = 'surprise'
    return found

def takephoto():
    cam = cv2.VideoCapture(0)
    while(cam.isOpened()):
        ret,frame = cam.read()
        if ret == True:
            cv2.imshow("Press 'q' to take a picture!", frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                im = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                im.save('photo.jpg')
                break
        else:
            break
    cam.release()
    cv2.destroyAllWindows()

def Emotion_recognition():
    # Microsoft Face API
    ENDPOINT = 'https://bence.cognitiveservices.azure.com/' # Endpoint
    with open("API.txt", "r") as f:
	    KEY = f.read()                                      # Key for the API

    # Create an authenticated FaceClient.
    face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))
    face_attributes = ['age', 'gender', 'smile', 'emotion']

    # Image
    takephoto()
    image = open('photo.jpg','r+b')

    # Emotion detection with Microsoft Face API
    detected_faces = face_client.face.detect_with_stream(image, return_face_attributes = face_attributes)   # With downloaded image

    for face in detected_faces:
        print()
        # ID of detected face
        print(face.face_id)
        # Show all facial attributes from the results
        print()
        print('Facial attributes detected:')
        print('Age: ', face.face_attributes.age)
        print('Gender: ', face.face_attributes.gender)
        print('Smile: ', face.face_attributes.smile)
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

        found = max_emotion(face.face_attributes.emotion)
        print('Recognised emotion:', found)
    image.close()
    return found
