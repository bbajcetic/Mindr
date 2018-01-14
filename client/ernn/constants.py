#                               __                    __             
#                              /\ \__                /\ \__          
#   ___    ___     ___     ____\ \ ,_\    __      ___\ \ ,_\   ____  
#  /'___\ / __`\ /' _ `\  /',__\\ \ \/  /'__`\  /' _ `\ \ \/  /',__\ 
# /\ \__//\ \L\ \/\ \/\ \/\__, `\\ \ \_/\ \L\.\_/\ \/\ \ \ \_/\__, `\
# \ \____\ \____/\ \_\ \_\/\____/ \ \__\ \__/.\_\ \_\ \_\ \__\/\____/
#  \/____/\/___/  \/_/\/_/\/___/   \/__/\/__/\/_/\/_/\/_/\/__/\/___/  .txt
#
#
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
CASC_PATH = dir_path + "/haarcascade_files/haarcascade_frontalface_default.xml"
SIZE_FACE = 48
EMOTIONS = ['angry', 'disgusted', 'fearful', 'happy', 'sad', 'surprised', 'neutral']
SAVE_DIRECTORY = dir_path+"/data"
SAVE_MODEL_FILENAME = 'Gudi_model_100_epochs_20000_faces'
SAVE_DATASET_IMAGES_FILENAME = 'data_kike.npy'
SAVE_DATASET_LABELS_FILENAME = 'labels_kike.npy'
SAVE_DATASET_IMAGES_TEST_FILENAME = 'data_kike.npy'
SAVE_DATASET_LABELS_TEST_FILENAME = 'labels_kike.npy'