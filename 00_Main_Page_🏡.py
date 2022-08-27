import numpy as np
import streamlit as st
import tensorflow as tf
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator
from keras.utils import array_to_img, img_to_array, load_img
from PIL import Image

IMAGE_DIM = (150, 150)

st.set_page_config(page_title="🏡 Main Page", layout="centered")
st.title("Welcome to Cat-Dog Classifier")

st.markdown("""
    ### Upload an image of cat or dog and see the prediction!
""")

uploaded_file = st.file_uploader("Upload an image...", type=["jpg", "png"])
model = load_model('model/vgg_transfer_learn_dogvscat_2.h5')

def resize_image(img):
    img = tf.image.resize(img, IMAGE_DIM)
    img_arr = img_to_array(img)
    return img_arr


def predict(img):
    img_arr = resize_image(img)
    img_arr = img_arr.reshape((1,) + img_arr.shape)
    img_arr = img_arr.astype('float32')
    img_arr /= 255.0

    pred = model.predict(img_arr)
    return pred

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    pred = predict(img)

    st.image(img, use_column_width=True)

    if pred[0][0] > 0.6:
        st.write("This is a Dog!")
    else:
        st.write("This is a Cat!")
