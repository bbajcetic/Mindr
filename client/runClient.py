import cv2
import numpy as np
import time

from ernn.emotion_recognition import EmotionRecognition
from ernn.constants import *
from ernn.poc import format_image
from client_manager import ClientHelper

def runtime():
#Vars
    #load = DatasetLoader()
    #load.load_from_save()

    config = ClientHelper()

    network = EmotionRecognition()
    network.build_network()
    network.load_model()

    video_capture = cv2.VideoCapture(0)

    #print("reading Image")
    #img = cv2.imread('test2.jpeg', 0)


    #print("my butthole is ready")
    #print("my butthole is really ready")
    #print("my butthole is really really ready")

    while True:
        time.sleep(.9)
        ret, frame = video_capture.read()
        #analyze image for separate faces
        if ret == True:
            temp_image = format_image(frame)
            result = network.predict(temp_image)
            cv2.imshow('feed', temp_image)

            print("checkin 1")
                #if not result:
                   # print("result faileds")
            if result is not None:
                for feeling in result:
                #print(feeling)
                    for emotion in feeling:
                        if emotion >= config.trigger_threshold:
                            config.emergency_update(result, img)
                print(feeling)
                if config.time_since_update == config.update_frequency:
                    config.update(result)
                else:
                    config.increment_time()
    print("finished execution")

runtime()
