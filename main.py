import sys

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.uic import *


class WindowMain(QtWidgets.QMainWindow):
    def __init__(self):
        super(WindowMain, self).__init__()
        loadUi('window-main.ui', self)

        self.chess_image = QLabel(self)
        self.pixmap = QPixmap('4489659.png')
        self.chess_image.setPixmap(self.pixmap)
        self.chess_image.setGeometry(360,190,371,361)
        self.chess_image.setScaledContents(1)

        self.play_button.clicked.connect(self.press_play_button)
        self.settings_button.clicked.connect(self.press_settings_button)

    def press_settings_button(self):
        windowSettings = WindowSettings()
        widget.addWidget(windowSettings)
        widget.removeWidget(windowMain)
        widget.removeWidget(windowPlay)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def press_play_button(self):
        windowPlay = WindowPlay()
        widget.addWidget(windowPlay)
        widget.removeWidget(windowMain)
        widget.removeWidget(windowSettings)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class WindowSettings(QtWidgets.QMainWindow):
    def __init__(self):
        super(WindowSettings, self).__init__()
        loadUi('window-settings.ui', self)
        self.setFixedSize(800, 600)

        self.menu_button.clicked.connect(self.press_menu_button)

    def press_menu_button(self):
        windowMain = WindowMain()
        widget.addWidget(windowMain)
        widget.removeWidget(windowSettings)
        widget.removeWidget(windowPlay)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class WindowPlay(QtWidgets.QMainWindow):
    def __init__(self):
        super(WindowPlay, self).__init__()
        self.setFixedSize(800, 600)

        loadUi('window-play.ui', self)

        self.pixmap = QPixmap('daskjdhaskj.png')
        self.background.setPixmap(self.pixmap)
        self.background.setScaledContents(1)

        self.more_button.clicked.connect(self.press_more_button)

    def press_more_button(self):
        windowMain = WindowMain()
        widget.addWidget(windowMain)
        widget.removeWidget(windowPlay)
        widget.removeWidget(windowSettings)
        widget.setCurrentIndex(widget.currentIndex() + 1)



'''
app = QApplication(sys.argv)

window = WindowMain()
window.show()

app.exec()

'''
app = QApplication(sys.argv)
windowMain = WindowMain()
windowSettings = WindowSettings()
windowPlay = WindowPlay()
widget = QtWidgets.QStackedWidget()
widget.addWidget(windowMain)
widget.addWidget(windowSettings)
widget.addWidget(windowPlay)
widget.setWindowTitle('Free time chess')
widget.setWindowIcon(QIcon("chess_piece_king.png"))
widget.show()
app.exec()


