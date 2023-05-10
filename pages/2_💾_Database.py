import streamlit as st 
import pickle 
import yaml 
import cv2
cfg = yaml.load(open("config.yaml", "r"), Loader=yaml.FullLoader)
PKL_PATH = cfg['PATH']["PKL_PATH"]
st.set_page_config(layout="wide")

#Load databse 
with open(PKL_PATH, 'rb') as file:
    database = pickle.load(file)

Index, Id, Image, Name = st.columns(4)

for idx, person in database.items():
    with Index:
        st.write(idx)
    with Id: 
        st.write(person['id'])
    with Image:     
        st.image(person['image'])
    with Name:     
        st.write(person['name'])
        