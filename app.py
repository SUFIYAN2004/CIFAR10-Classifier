import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

st.title("CIFAR-10 Image Classifier")
model = tf.keras.models.load_model('cifar10_model.keras')

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', width=200)
    
    img = image.resize((32, 32))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    prediction = model.predict(img_array)
    result = class_names[np.argmax(prediction)]
    
    st.subheader(f"Result: This looks like a {result}!")