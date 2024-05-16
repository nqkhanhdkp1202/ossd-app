from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui
from bus.browse_image import browse_image
from bus.predict_emotion import predict_cnn_emotion, predict_xception_emotion
from bus.predict_gender import predict_cnn_gender
from bus.predict_animals import predict_cnn_animal
from bus.predict_handwriting_digit import predict_cnn_handwriting
from common.constants import get_array_labels, get_models_path
import time

class MainGUI(QMainWindow):
    def __init__(self):
        super(MainGUI, self).__init__()
        uic.loadUi("src/gui/template/main_ui.ui", self) 
        self.show()
        self.setFixedSize(self.size())
        self.emotion_image_filename = ""
        self.emotion_result = ""
        self.emotion_current_file = "src/assets/faces-675-675x394.jpeg"
        emotion_pixmap = QtGui.QPixmap(self.emotion_current_file)
        emotion_pixmap = emotion_pixmap.scaled(self.width(), self.height())
        self.emotionImage.setPixmap(emotion_pixmap)
        self.emotionImage.setMinimumSize(1, 1)
        self.emotionBrowseBtn.clicked.connect(self.get_image_emotion)
        self.emotionPredictBtn.clicked.connect(self.predict_emotion_gender)
        self.animal_image_filename = ""
        self.animal_result = ""
        self.animal_current_file = "src/assets/animal-classification-stickers-2.jpg"
        animal_pixmap = QtGui.QPixmap(self.animal_current_file)
        animal_pixmap = animal_pixmap.scaled(self.width(), self.height())
        self.animalImage.setPixmap(animal_pixmap)
        self.animalImage.setMinimumSize(1, 1)
        self.animalBrowseBtn.clicked.connect(self.get_image_animal)
        self.animalPredictBtn.clicked.connect(self.predict_animal)
        self.number_image_filename = ""
        self.number_result = ""
        self.number_current_file = "src/assets/MnistExamplesModified.png"
        number_pixmap = QtGui.QPixmap(self.number_current_file)
        number_pixmap = number_pixmap.scaled(self.width(), self.height())
        self.numberImage.setPixmap(number_pixmap)
        self.numberImage.setMinimumSize(1, 1)
        self.numberBrowseBtn.clicked.connect(self.get_image_number)
        self.numberPredictBtn.clicked.connect(self.predict_number)
        self.actionQuit.triggered.connect(self.close)
        self.emotionErrorLabel.setStyleSheet("color: red")
        self.emoitonQAction.triggered.connect(self.switch_to_emotion_screen)
        self.animalQAction.triggered.connect(self.switch_to_animal_screen)
        self.numericalQAction.triggered.connect(self.switch_to_number_screen)
        self.animalGroupBox.hide()
        self.numberGroupBox.hide()
        self.emotionGroupBox.show()
        self.cnnRadio.toggled.connect(self.cnnselected)
        self.xceptionRadio.toggled.connect(self.xceptionselected)
        self.isSelectedCnn = True
        self.isSelectedXception = False

    def switch_to_emotion_screen(self):
        self.numberGroupBox.hide()
        self.animalGroupBox.hide()
        self.emotionGroupBox.show()
        self.numberErrorLabel.setText("")
        self.emotionErrorLabel.setText("")
        self.animalErrorLabel.setText("")

    def switch_to_animal_screen(self):
        self.numberGroupBox.hide()
        self.animalGroupBox.show()
        self.emotionGroupBox.hide()
        self.numberErrorLabel.setText("")
        self.emotionErrorLabel.setText("")
        self.animalErrorLabel.setText("")

    def switch_to_number_screen(self):
        self.numberGroupBox.show()
        self.animalGroupBox.hide()
        self.emotionGroupBox.hide()
        self.numberErrorLabel.setText("")
        self.emotionErrorLabel.setText("")
        self.animalErrorLabel.setText("")

    def cnnselected(self, selected):
        if selected:
            self.isSelectedCnn = True
            self.isSelectedXception = False

    def xceptionselected(self, selected):
        if selected:
            self.isSelectedCnn = False
            self.isSelectedXception = True

    def get_image_emotion(self):
        try:
            self.emotion_image_filename = browse_image()
            file = QtGui.QPixmap(self.emotion_image_filename)
            file = file.scaled(self.width(), self.height())
            self.emotionImage.setPixmap(file)
        except Exception as e:
            print(e)
            self.emotionErrorLabel.setText(e.__str__())

    def predict_emotion_gender(self):
        try:
            if self.isSelectedCnn:
                self.emotion_result = predict_cnn_emotion(self.emotion_image_filename)
                # setting for loop to set value of progress bar
                for i in range(101):
                    time.sleep(0.01)
                    self.emotionPBar.setValue(i)
            if self.isSelectedXception:
                self.emotion_result = predict_xception_emotion(self.emotion_image_filename)
                # setting for loop to set value of progress bar
                for i in range(101):
                    time.sleep(0.01)
                    self.emotionPBar.setValue(i)

            genderResult = predict_cnn_gender(self.emotion_image_filename)
            self.emotionResultLabel.setText(self.emotion_result + genderResult)

        except Exception as e:
            print(e)
            self.emotionErrorLabel.setText(e.__str__())

    def get_image_animal(self):
        try:
            self.animal_image_filename = browse_image()
            file = QtGui.QPixmap(self.animal_image_filename)
            file = file.scaled(self.width(), self.height())
            self.animalImage.setPixmap(file)
        except Exception as e:
            print(e)
            self.animalErrorLabel.setText(e.__str__())

    def predict_animal(self):
        try:
            self.animal_result = predict_cnn_animal(self.animal_image_filename)
            # setting for loop to set value of progress bar
            for i in range(101):
                time.sleep(0.01)
                self.animalPBar.setValue(i)

            self.animalResultLabel.setText(self.animal_result)
        except Exception as e:
            print(e)
            self.animalErrorLabel.setText(e.__str__())

    def get_image_number(self):
        try:
            self.number_image_filename = browse_image()
            file = QtGui.QPixmap(self.number_image_filename)
            file = file.scaled(self.width(), self.height())
            self.numberImage.setPixmap(file)
        except Exception as e:
            print(e)
            self.numberErrorLabel.setText(e.__str__())

    def predict_number(self):
        try:
            self.number_result = predict_cnn_handwriting(self.number_image_filename)
            # setting for loop to set value of progress bar
            for i in range(101):
                time.sleep(0.01)
                self.numberPBar.setValue(i)

            self.numberResultLabel.setText(self.number_result)
        except Exception as e:
            print(e)
            self.numberErrorLabel.setText(e.__str__())
