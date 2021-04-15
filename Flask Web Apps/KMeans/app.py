# cd C:\Users\Admin\OneDrive\Desktop\Semester VI\Labs and Mini Project\ML Project\k_app
# env\Scripts\activate
# python app.py



import os
import numpy as np
from PIL import Image
from numpy import asarray
from cv2 import cv2
from os.path import join, dirname, realpath
from flask import Flask,render_template,request
import skimage
from skimage import io
from skimage.transform import resize
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans 


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config["CACHE_TYPE"] = "null"
app.static_folder = 'static'
f = ""
original_filename =""

UPLOADS_PATH = join(dirname(realpath(__file__)), 'static\\')
w, h, d = 0,0,0

def preprocess(path):
    global w,h,d
    img = Image.open(path)
    image = np.asarray(img)
    w, h, d = image.shape
    width = w*h
    image_array = image.reshape(width,d)                   #Flatten        #(28,28,1) --->(784,1)
    return image_array                                 #return numpy array

def recreate_image(kmeans):
  compressed_image_array = kmeans.cluster_centers_[kmeans.labels_] #[0,3,2,1,.........]
  #Reshape the image to original dimension
  compressed_image = compressed_image_array.reshape(w,h,d)
  #Save and display output image
  return compressed_image

@app.route('/') #Home Page
def upload_image():
    if os.path.exists("C:\\Users\\Admin\\OneDrive\\Desktop\\Semester VI\\Labs and Mini Project\\ML Project\\k_app\\static\\compressed.jpg"):
        os.remove("C:\\Users\\Admin\\OneDrive\\Desktop\\Semester VI\\Labs and Mini Project\\ML Project\\k_app\\static\\compressed.jpg")
    return render_template('index.html')


@app.route('/imageuploader',methods=['GET','POST'])
def image_upload():
    if request.method=='POST':
        f = request.files['image']
        i = (int)(request.form['clusters'])
        f.save(os.path.join(UPLOADS_PATH,f.filename))
        original_filename = f.filename
      
        path = "C:\\Users\\Admin\\OneDrive\\Desktop\\Semester VI\\Labs and Mini Project\\ML Project\\k_app\\static\\" + f.filename
        image = Image.open(os.path.join(UPLOADS_PATH,f.filename))
        image_array = preprocess(os.path.join(UPLOADS_PATH,f.filename))              #numpy array of shape (748,1)

        kmeans = KMeans(n_clusters = i,random_state=42,verbose=2,n_jobs=-1).fit(image_array)
        op_arr = recreate_image(kmeans)
        op_arr = op_arr.astype(np.uint8)
        op_img = Image.fromarray(op_arr)
        op_img.save('static\\compressed.jpg')

        return render_template('compress.html',filename = f.filename)

if __name__ == '__main__':
    app.run(debug = True)