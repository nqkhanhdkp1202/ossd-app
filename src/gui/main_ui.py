from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui
from src.bus.browse_image import browse_image

class MainGUI(QMainWindow):
    def __init__(self):
        super(MainGUI, self).__init__()
        uic.loadUi("./gui/template/main_ui.ui", self)
        self.show()
        self.current_file = "./assets/Emotion-Detection-1.webp"
        pixmap = QtGui.QPixmap(self.current_file)
        pixmap = pixmap.scaled(self.width(), self.height())
        self.label.setPixmap(pixmap)
        self.label.setMinimumSize(1, 1)
        self.browseBtn.clicked.connect(browse_image)
