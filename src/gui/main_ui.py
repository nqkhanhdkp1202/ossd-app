from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui
from src.bus.browse_image import browse_image
from src.bus.predict_emotion import predict_emotion
from src.common.constants import get_array_labels, get_models_path
import time

class MainGUI(QMainWindow):
    def __init__(self):
        super(MainGUI, self).__init__()
        uic.loadUi("./gui/template/main_ui.ui", self)
        self.show()
        self.setFixedSize(self.size())
        self.filename = ""
        self.result = ""
        self.current_file = "./assets/Emotion-Detection-1.webp"
        pixmap = QtGui.QPixmap(self.current_file)
        pixmap = pixmap.scaled(self.width(), self.height())
        self.label.setPixmap(pixmap)
        self.label.setMinimumSize(1, 1)
        self.browseBtn.clicked.connect(self.get_image)
        self.predictBtn.clicked.connect(self.predict_emotion)
        self.actionQuit.triggered.connect(self.close)
        self.errorLabel.setStyleSheet("color: red")

    def get_image(self):
        try:
            self.filename = browse_image()
            file = QtGui.QPixmap(self.filename)
            file = file.scaled(self.width(), self.height())
            self.label.setPixmap(file)
        except Exception as e:
            self.errorLabel.setText(e.__str__())

    def predict_emotion(self):
        try:
            self.result = predict_emotion(self.filename, get_array_labels(), get_models_path())
            # setting for loop to set value of progress bar
            for i in range(101):
                time.sleep(0.01)
                self.pBar.setValue(i)

            self.resultLabel.setText(self.result)
        except Exception as e:
            self.errorLabel.setText(e.__str__())

