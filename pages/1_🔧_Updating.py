import streamlit as st 
import cv2
import yaml 
import pickle 
from utils import submitNew, get_info_from_id, deleteOne
import numpy as np

st.set_page_config(layout="wide")
st.title("Face Recognition App")
st.write("This app is used to add new faces to the dataset")

menu = ["Adding","Deleting", "Adjusting"]
choice = st.sidebar.selectbox("Options",menu)
if choice == "Adding":
    name = st.text_input("Name",placeholder='Enter name')
    id = st.text_input("ID",placeholder='Enter id')
    #Create 2 options: Upload image or use webcam
    #If upload image is selected, show a file uploader
    #If use webcam is selected, show a button to start webcam
    upload = st.radio("Upload image or use webcam",("Upload","Webcam"))
    if upload == "Upload":
        uploaded_image = st.file_uploader("Upload",type=['jpg','png','jpeg'])
        if uploaded_image is not None:
            st.image(uploaded_image)
            submit_btn = st.button("Submit",key="submit_btn")
            if submit_btn:
                if name == "" or id == "":
                    st.error("Please enter name and ID")
                else:
                    ret = submitNew(name, id, uploaded_image)
                    if ret == 1: 
                        st.success("Student Added")
                    elif ret == 0: 
                        st.error("Student ID already exists")
                    elif ret == -1: 
                        st.error("There is no face in the picture")
    elif upload == "Webcam":
        img_file_buffer = st.camera_input("Take a picture")
        submit_btn = st.button("Submit",key="submit_btn")
        if img_file_buffer is not None:
            # To read image file buffer with OpenCV:
            bytes_data = img_file_buffer.getvalue()
            cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
            if submit_btn: 
                if name == "" or id == "":
                    st.error("Please enter name and ID")
                else:
                    ret = submitNew(name, id, cv2_img)
                    if ret == 1: 
                        st.success("Student Added")
                    elif ret == 0: 
                        st.error("Student ID already exists")
                    elif ret == -1: 
                        st.error("There is no face in the picture")
elif choice == "Deleting":
    def del_btn_callback(id):
        deleteOne(id)
        st.success("Student deleted")
        
    id = st.text_input("ID",placeholder='Enter id')
    submit_btn = st.button("Submit",key="submit_btn")
    if submit_btn:
        name, image,_ = get_info_from_id(id)
        if name == None and image == None:
            st.error("Student ID does not exist")
        else:
            st.success(f"Name of student with ID {id} is: {name}")
            st.warning("Please check the image below to make sure you are deleting the right student")
            st.image(image)
            del_btn = st.button("Delete",key="del_btn",on_click=del_btn_callback, args=(id,)) 
        
elif choice == "Adjusting":
    def form_callback(old_name, old_id, old_image, old_idx):
        new_name = st.session_state['new_name']
        new_id = st.session_state['new_id']
        new_image = st.session_state['new_image']
        
        name = old_name
        id = old_id
        image = old_image
        
        if new_image is not None:
            image = cv2.imdecode(np.frombuffer(new_image.read(), np.uint8), cv2.IMREAD_COLOR)
            
        if new_name != old_name:
            name = new_name
            
        if new_id != old_id:
            id = new_id
        
        ret = submitNew(name, id, image, old_idx=old_idx)
        if ret == 1: 
            st.success("Student Added")
        elif ret == 0: 
            st.error("Student ID already exists")
        elif ret == -1: 
            st.error("There is no face in the picture")
    id = st.text_input("ID",placeholder='Enter id')
    submit_btn = st.button("Submit",key="submit_btn")
    if submit_btn:
        old_name, old_image, old_idx = get_info_from_id(id)
        if old_name == None and old_image == None:
            st.error("Student ID does not exist")
        else:
            with st.form(key='my_form'):
                st.title("Adjusting student info")
                col1, col2 = st.columns(2)
                new_name = col1.text_input("Name",key='new_name', value=old_name, placeholder='Enter new name')
                new_id  = col1.text_input("ID",key='new_id',value=id,placeholder='Enter new id')
                new_image = col1.file_uploader("Upload new image",key='new_image',type=['jpg','png','jpeg'])
                col2.image(old_image,caption='Current image',width=400)
                st.form_submit_button(label='Submit',on_click=form_callback, args=(old_name, id, old_image, old_idx))
                