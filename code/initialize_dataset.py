import face_recognition as frg 
import os 
import cv2 
import pickle as pkl
import yaml
import pandas as pd
from collections import defaultdict


information = defaultdict(dict)
cfg = yaml.load(open('config.yaml','r'),Loader=yaml.FullLoader)
DATASET_DIR = cfg['PATH']['DATASET_DIR']


def build_dataset():
    counter = 0
    for image in os.listdir(DATASET_DIR):
        image_path = os.path.join(DATASET_DIR,image)
        image_name = image.split('.')[0]
        parsed_name = image_name.split('_')
        person_id = parsed_name[0]
        person_name = ' '.join(parsed_name[1:])
        if not image_path.endswith('.jpg'):
            continue
        image = frg.load_image_file(image_path)
        information[counter]['image'] = image 
        information[counter]['id'] = person_id
        information[counter]['name'] = person_name
        information[counter]['encoding'] = frg.face_encodings(image)[0]
        counter += 1

    with open(os.path.join(DATASET_DIR,'database.pkl'),'wb') as f:
        pkl.dump(information,f)
    
if __name__ == "__main__":
    build_dataset()
