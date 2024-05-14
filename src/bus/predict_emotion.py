from PIL import Image, ImageTk
import numpy as np

def predict_emotion(image_path, labels_array, model, result_label):
    img = Image.open(image_path).resize((299, 299))
    img_array = np.expand_dims(np.array(img) / 255.0, axis=0)
    predictions = model.predict(img_array)
    top_pred = np.argmax(predictions)
    result_label.config(text=f'Predicted Emotion: {labels_array[top_pred]}')