# Face recognition app using Streamlit

This is a face recognition application built using Python and Streamlit framework. The app allows users to upload an image containing faces and performs face recognition using the face recognition library.

## Features

- Face detection and recognition
- Multi-face recognition
- Option to display recognized faces
- User-friendly interface

## Requirements 
- Python 3.9
- Streamlit 1.22.0

## Repository structure
```bash
├───dataset
│   │───ID_Name.jpg
│   │───...
├───pages
│   ├───1_🔧_Updating.py
│   └───2_💾_Database
├───👁️_Tracking.py
│───utils.py
├───config.yaml 
├───requirements.txt
├───packages.txt
└───README.md
```

## Description
- **dataset**: contains images of people to be recognized. The file name format is ID_Name.jpg. `For example, 1_Elon_Musk.jpg, 2_Jenna_Ortega.jpg, 3_Bill_Gates.jpg, etc.` It is freely to use jpg, jpeg or png format.
- **pages**: contains the code for each page of the app. If you want to add more pages, you can create a new file which format is `Order_Icon_Pagename` in this folder, or just no-icon page with format `Order_Pagename`.
- **Tracking.py**: home page of the app, using for tracking real-time using webcam and picture.
- **utils.py**: contains the functions utilized by the app.
- **config.yaml**: contains the configuration for the app such as path of dataset dir and prompt messages.
- **requirements.txt**: contains the dependencies for the app.
- **packages.txt**: contains the packages for the app used to deploy on Streamlit Cloud.



## Installation
1. Clone the repository
```bash
git clone https://github.com/chungtiendat8102000/Face-recognition-app-using-Streamlit.git
cd Face-recognition-app-using-Streamlit
```

2. Install the dependencies
```bash
pip install -r requirements.txt
```

3. Run the app
```bash
streamlit run Tracking.py
```

## Usage
1. Tracking real-time using webcam 
2. Tracking using a image file 
3. Updating database (adding, deleting and updating)
4. Viewing the database


## Demo
[Click here](https://chungtiendat8102000-face-recognition-app-using--tracking-9380y2.streamlit.app/) to watch a demo of the app.

## Contributing
Contributions are always welcome! If you would like to contribute to this project, please open an issue to discuss your ideas or submit a pull request.

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).