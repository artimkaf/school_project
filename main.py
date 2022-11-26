import sys
import random

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.uic import *

from trash import moves

black_or_white_lives_matter = (random.choice(['white', 'black']))
print (black_or_white_lives_matter)



class WindowMain(QtWidgets.QMainWindow):
    def __init__(self):
        super(WindowMain, self).__init__()
        loadUi('window-main.ui', self)

        self.pixmap = QPixmap('4489659.png')
        self.chess_image.setPixmap(self.pixmap)
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
        if black_or_white_lives_matter == 'white':
            loadUi('window-play-white.ui', self)
        if black_or_white_lives_matter == 'black':
            loadUi('window-play-black.ui', self)

        self.pixmap = QPixmap('chess-board.png')
        self.background.setPixmap(self.pixmap)
        self.background.setScaledContents(1)

        self.chess_board()

        self.first_button_click()

        self.more_button.clicked.connect(self.press_more_button)






    def chess_board(self):

        self.a2.setText('♙')
        self.b2.setText('♙')
        self.c2.setText('♙')
        self.d2.setText('♙')
        self.e2.setText('♙')
        self.f2.setText('♙')
        self.g2.setText('♙')
        self.h2.setText('♙')
        #
        self.a1.setText('♖')
        self.b1.setText('♘')
        self.c1.setText('♗')
        self.d1.setText('♕')
        self.e1.setText('♔')
        self.f1.setText('♗')
        self.g1.setText('♘')
        self.h1.setText('♖')
        #
        self.a7.setText('♟')
        self.b7.setText('♟')
        self.c7.setText('♟')
        self.d7.setText('♟')
        self.e7.setText('♟')
        self.f7.setText('♟')
        self.g7.setText('♟')
        self.h7.setText('♟')
        #
        self.a8.setText('♜')
        self.b8.setText('♞')
        self.c8.setText('♝')
        self.d8.setText('♛')
        self.e8.setText('♚')
        self.f8.setText('♝')
        self.g8.setText('♞')
        self.h8.setText('♜')


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
widget.setFixedSize(800, 600)
widget.setWindowTitle('Free time chess')
widget.setWindowIcon(QIcon("chess_piece_king.png"))
widget.show()
app.exec()


