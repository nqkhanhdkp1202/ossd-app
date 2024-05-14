# from tensorflow.keras.models import load_model
# import tkinter as tk
# from tkinter import filedialog

# import numpy as np
#
# # Path to the model
# model_path = '../models/xception_299x299_rbg_fer2013_32bs_50epochs.h5'
# model = load_model(model_path)
#
# emotions = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']
#
#
# def load_image():
#     global img, image_path
#     photo = tk.PhotoImage("/Users/nqkhanh2003/Downloads/355198101_1175351713158657_3732404125354556913_n.jpg")
#
#     label = tk.Label(image=photo)
#     label.image = photo  # keep a reference!
#     label.pack()
#
#
# def predict_emotion():
#     img = Image.open(image_path).resize((299, 299))
#     img_array = np.expand_dims(np.array(img) / 255.0, axis=0)
#     predictions = model.predict(img_array)
#     top_pred = np.argmax(predictions)
#     result_label.config(text=f'Predicted Emotion: {emotions[top_pred]}')
#
#
# window = tk.Tk()
# window.title('Emotion Recognition')
# window.geometry()
#
# load_btn = tk.Button(window, text='Load Image', command=load_image)
# load_btn.grid(column=0, row=0)
#
# predict_btn = tk.Button(window, text='Predict Emotion', command=predict_emotion)
# predict_btn.grid(column=0, row=1)
#
# result_label = tk.Label(window, text='Predicted Emotion: None')
# result_label.grid(column=1, row=1)
#
# window.mainloop()
import sys
from PyQt5.QtWidgets import QApplication
from gui.main_ui import MainGUI


def main():
    app = QApplication(sys.argv)
    window = MainGUI()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()