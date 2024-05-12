from tensorflow.keras.models import load_model
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np

# Path to the model
model_path = 'D:/Study/ANMMT/App/ossd-app/models/xception_299x299_rbg_fer2013_32bs_50epochs.h5'
model = load_model(model_path)

# Define emotion labels
emotions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']

def load_image():
    global img, image_path
    image_path = filedialog.askopenfilename()
    img = Image.open(image_path)
    img.thumbnail((250, 250))
    img = ImageTk.PhotoImage(img)
    panel = tk.Label(window, image=img)
    panel.image = img
    panel.grid(column=1, row=0)

def predict_emotion():
    img = Image.open(image_path).resize((299, 299))
    img_array = np.expand_dims(np.array(img) / 255.0, axis=0)
    predictions = model.predict(img_array)
    top_pred = np.argmax(predictions)
    result_label.config(text=f'Predicted Emotion: {emotions[top_pred]}')

window = tk.Tk()
window.title('Emotion Recognition')

load_btn = tk.Button(window, text='Load Image', command=load_image)
load_btn.grid(column=0, row=0)

predict_btn = tk.Button(window, text='Predict Emotion', command=predict_emotion)
predict_btn.grid(column=0, row=1)

result_label = tk.Label(window, text='Predicted Emotion: None')
result_label.grid(column=1, row=1)

window.mainloop()