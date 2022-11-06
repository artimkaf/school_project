import sys
import random

from PyQt6 import QtWidgets
# from PyQt6 import uic
# from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.uic import *

title_names = ['Free time chess', 'Бесплатное время шахматы']


class WindowMain(QtWidgets.QMainWindow):
    def __init__(self):
        super(WindowMain, self).__init__()
        self.settings_button = WindowSettings()
        loadUi('window-main.ui', self)

        self.settings_button.clicked.connect(self.gotosetbtn)

    def press_settings_button(self):
        settings_button = WindowSettings()
        widget.addWidget(self.settings_button)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        #print ('clicked')
        #self.Window = setwin()


class WindowSettings(QtWidgets.QMainWindow):
    def __init__(self):
        super(WindowSettings, self).__init__()
        loadUi('window-settings.ui', self)
        #то что ниже работать не хочет
        '''
        self.exitmenubtn.clicked.connect(self.gotosetbtn)
        
    def gotoexitmenubtn(self):
        exitmenubtn = mainwin()
        widget.addWidget(exitmenubtn)
        widget.setCurrentIndex(widget.currentIndex() + 1)
'''


app = QApplication(sys.argv)
windowMain = WindowMain()
widget = QtWidgets.QStackedWidget()
widget.addWidget(windowMain)
widget.setFixedSize(800, 600)
widget.setWindowTitle(random.choice(title_names))
widget.setWindowIcon(QIcon("chess_piece_king.png"))
widget.show()
app.exec()


