from PyQt5 import QtWidgets,QtGui


def browse_image():
    filename, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Select Image', '', "Image Files (*.png *.jpg *.jpeg)")
    return filename
