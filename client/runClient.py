import cv2
import numpy as np
from nwhacks2018.client.ernn.emotion_recognition import EmotionRecognition
from nwhacks2018.client.ernn.constants import *
from nwhacks2018.client.ernn.poc import format_image
from nwhacks2018.client.client_manager import ClientHelper

def run():
#Vars
    cascade_classifier = cv2.CascadeClassifier(CASC_PATH)

    config = ClientHelper()
    config.load_config()

    network = EmotionRecognition()
    network.build_network()#Neural Net
    video_capture = cv2.VideoCapture(0)


    while True:
        ret, frame = video_capture.read()

        formatted_image = format_image(frame)

        #analyze image for separate faces

        result = network.predict(formatted_image)

        for feeling in result:
            if feeling >= config.trigger_threshold:
                config.emergency_update()
                break
        if config.time_since_update == config.update_frequency:
            config.update()
        else:
            config.increment_time()

run()