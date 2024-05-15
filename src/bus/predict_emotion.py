from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model
from os.path import join, dirname, realpath
import numpy as np
import os.path

# Load the saved model
base_dir = dirname(realpath(__file__))
model_path_cnn = 'models/cnn-animals.h5'
model_path_exception = 'models/xception_299x299_rbg_fer2013_32bs_50epochs.h5'

model_cnn = load_model(model_path_cnn)
model_exception = load_model(model_path_exception)

emotion_mapping = {
    0: 'Surprise',
    1: 'Fear',
    2: 'Disgust',
    3: 'Happy',
    4: 'Sad',
    5: 'Angry',
    6: 'Neutral'
}


def predict_cnn_emotion(image_path):
    img = load_img(image_path, target_size=(100, 100))
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    pred_label = model_cnn.predict(img_array)
    pred_label = np.argmax(pred_label)
    return emotion_mapping[pred_label]


def predict_xception_emotion(image_path):
    img = load_img(image_path, target_size=(100, 100))
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    pred_label = model_exception.predict(img_array)
    pred_label = np.argmax(pred_label)
    return emotion_mapping[pred_label]
