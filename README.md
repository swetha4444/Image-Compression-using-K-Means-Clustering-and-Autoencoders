# Image Compression using K-Means Clustering and Convolutional Autoencoders

A project which performs compression and decompression of images from the MNIST dataset using autoencoder and K-Means clustering and deployment of the model using Flask.


# Environment
 - Coded in python 3.8
 - Interactive python notebook editor - Google collab

# Folders
- Notebooks - contains the google collab notebooks
- Flask App - contains the code required for the flask application 
- Models - contains the pretrained models in h5 format
- Results - contains screenshots of the project outcome 

# Installation
To run the flask app in a  windows environment

 1. Install python 3.8
 2. Run ```pip install virtualenv```
 3. Run ```mkdir project``` to create project directory
 4. Run ```cd project``` to move to the project directory
 5. Run ```virtualenv venv``` to create a virtual environment
 6. Run ```.\Scripts\activate```  to activate the virtual environement
 7. Run ```pip install tensorflow numpy Flask keras matplotlib pillow opencv-python scikit-image cv2 sklearn``` to install the dependencies
 8. Copy the contents of the Flask app folder to your virtual environment and use command ```python app.py``` to run the app. 

The python notebooks can be executed in Google collab by signing up for a Google account. 
Upload the pre-trained models into the collab runtime and load them to execute the code faster. 
