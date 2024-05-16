from keras.models import load_model
from PIL import Image
import numpy as np
from os.path import join, dirname, realpath


# Load the saved model
base_dir = dirname(__file__)  # Gets the directory where the script is located

model_path_cnn = join(base_dir, "..", "models", "cnn-animals.h5")
model_cnn = load_model(model_path_cnn)



results = {
    0: 'bird',
    1: 'cat',
    2: 'deer',
    3: 'dog',
    4: 'frog',
    5: 'horse',
}


def predict_cnn_animal(image_path):
    im = Image.open(image_path)
    im = im.resize((32, 32))
    im = np.expand_dims(im, axis=0)
    im = np.array(im) / 255.0
    pred = model_cnn.predict(im)
    predicted_class = np.argmax(pred, axis=1)[0]
    return get_result(predicted_class)


def get_result(index):
    if index == 0 or index == 1 or index == 8 or index == 9:
        return "None"
    return results[index - 2]
