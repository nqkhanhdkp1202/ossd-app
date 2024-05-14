from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model


def predict_emotion(image_path, labels_array, model_path):
    img = Image.open(image_path).resize((299, 299))
    img_array = np.expand_dims(np.array(img) / 255.0, axis=0)
    model = load_model(model_path)
    predictions = model.predict(img_array)
    top_pred = np.argmax(predictions)
    return f'Predicted Emotion: {labels_array[top_pred]}'
