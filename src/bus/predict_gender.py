from tensorflow.keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
from os.path import join, dirname, realpath
import numpy as np

# Load the saved model
base_dir = dirname(realpath(__file__))  # Gets the directory where the script is located
model_path_cnn = join(base_dir, "..", "models", "cnn-gender.h5")
model_cnn = load_model(model_path_cnn)

gender_mapping = {
    0: 'Woman',
    1: 'Man'
}

def predict_cnn_gender(image_path):
    img = load_img(image_path, target_size=(100, 100))
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    pred_label = model_cnn.predict(img_array)
    pred_label = np.argmax(pred_label)
    return gender_mapping[pred_label]