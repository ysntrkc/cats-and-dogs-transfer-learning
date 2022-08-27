import streamlit as st
import tensorflow as tf
from keras.models import load_model
from keras.utils import img_to_array
from PIL import Image

IMAGE_DIM = (150, 150)

st.set_page_config(page_title="🏡 Main Page", layout="centered")
st.title("Welcome to Cat-Dog Classifier")

st.markdown("---")
st.subheader("Upload an image of cat or dog and see the prediction!")

uploaded_file = st.file_uploader(label="", type=["jpg", "png"])
st.markdown("---")

model = load_model('model/vgg_transfer_learn_dogvscat.h5')

def resize_image(img):
    img = tf.image.resize(img, IMAGE_DIM)
    img_arr = img_to_array(img)
    return img_arr


def predict(img):
    img_arr = resize_image(img)
    img_arr = img_arr.reshape((1,) + img_arr.shape)
    img_arr = img_arr.astype('float16')
    img_arr /= 255.0

    pred = model.predict(img_arr)
    return pred

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    pred = predict(img)

    if pred[0][0] > 0.55:
        st.subheader("Predicted: Dog!")
    else:
        st.subheader("Predicted: Cat!")

    st.image(img, use_column_width=True)