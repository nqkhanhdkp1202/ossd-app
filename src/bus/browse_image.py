from PIL import Image, ImageTk
from PyQt5 import QtWidgets,QtGui


def browse_image():
    filename, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Select Image', '', "Image Files (*.png *.jpg *.jpeg)")

    if filename:
    else:
            return filename


    return None  # Or any other default value