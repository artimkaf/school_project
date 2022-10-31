import sys
import random

from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.uic import *

title_names=['Free time chess', 'Бесплатное время шахматы']

class mainwin(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainwin, self).__init__()
        loadUi('menuwin.ui', self)

        self.setbtn.clicked.connect(self.gotosetbtn)

    def gotosetbtn(self):
        setbtn = setwin()
        widget.addWidget(setbtn)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        #print ('clicked')
        #self.Window = setwin()



class setwin(QtWidgets.QMainWindow):
    def __init__(self):
        super(setwin, self).__init__()
        loadUi('settingswin.ui', self)
        #то что ниже работать не хочет
        '''
        self.exitmenubtn.clicked.connect(self.gotosetbtn)
        
    def gotoexitmenubtn(self):
        exitmenubtn = mainwin()
        widget.addWidget(exitmenubtn)
        widget.setCurrentIndex(widget.currentIndex() + 1)
'''

app = QApplication(sys.argv)
mainwindow = mainwin()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedSize(800,600)
widget.setWindowTitle(random.choice(title_names))
widget.setWindowIcon(QIcon("chess_piece_king.png"))
widget.show()
app.exec()


