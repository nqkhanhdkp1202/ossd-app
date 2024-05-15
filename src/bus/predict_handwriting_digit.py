# predict.py
from keras.models import load_model
from PIL import Image
import numpy as np
from os.path import join, dirname, realpath

# Load the saved model
base_dir = dirname(realpath(__file__))  # Gets the directory where the script is located
model_path = 'models/cnn-handwritten-digits.h5'
model = load_model(model_path)

# Define class labels
results = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}


def predict_cnn_handwriting(image_path):
    # Load and preprocess the image
    im = Image.open(image_path)
    im = im.resize((28, 28))  # Ensure the size matches the model's expected input
    im = im.convert('L')  # Convert the image to grayscale
    im = np.array(im) / 255.0  # Normalize pixel values
    im = np.expand_dims(im, axis=-1)  # Add the channel dimension
    im = np.expand_dims(im, axis=0)  # Add the batch dimension

    # Make prediction
    pred = model.predict(im)
    predicted_class = np.argmax(pred, axis=1)[0]
    return results[predicted_class]
