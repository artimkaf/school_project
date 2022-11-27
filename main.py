import sys
import random
import functools

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.uic import *

from trash import moves

black_or_white_lives_matter = (random.choice(['white', 'black']))
user_color_white = (random.getrandbits(1))
print (user_color_white)

class WindowMain(QtWidgets.QMainWindow):
    def __init__(self):
        super(WindowMain, self).__init__()
        loadUi('window-main.ui', self)
        # show the main image
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
        if user_color_white == 1:
            loadUi('window-play-white.ui', self)
        else:
            loadUi('window-play-black.ui', self)

        self.pixmap = QPixmap('chess-board.png')
        self.background.setPixmap(self.pixmap)
        self.background.setScaledContents(1)

        self.dirlist = ''  # !!!

        self.chess_board()



        # self.first_button_click()

        self.more_button.clicked.connect(self.press_more_button)

    def chess_board(self):
        '''
        self.chess_board_list = [
        [self.a8, self.b8, self.c8, self.d8, self.e8, self.f8, self.g8, self.h8],
        [self.a7, self.b7, self.c7, self.d7, self.e7, self.f7, self.g7, self.h7],
        [self.a6, self.b6, self.c6, self.d6, self.e6, self.f6, self.g6, self.h6],
        [self.a5, self.b5, self.c5, self.d5, self.e5, self.f5, self.g5, self.h5],
        [self.a4, self.b4, self.c4, self.d4, self.e4, self.f4, self.g4, self.h4],
        [self.a3, self.b3, self.c3, self.d3, self.e3, self.f3, self.g3, self.h3],
        [self.a2, self.b2, self.c2, self.d2, self.e2, self.f2, self.g2, self.h2],
        [self.a1, self.b1, self.c1, self.d1, self.e1, self.f1, self.g1, self.h1]]
        '''
        self.chess_board_list = [
            [self.a1, self.b1, self.c1, self.d1, self.e1, self.f1, self.g1, self.h1],
            [self.a2, self.b2, self.c2, self.d2, self.e2, self.f2, self.g2, self.h2],
            [self.a3, self.b3, self.c3, self.d3, self.e3, self.f3, self.g3, self.h3],
            [self.a4, self.b4, self.c4, self.d4, self.e4, self.f4, self.g4, self.h4],
            [self.a5, self.b5, self.c5, self.d5, self.e5, self.f5, self.g5, self.h5],
            [self.a6, self.b6, self.c6, self.d6, self.e6, self.f6, self.g6, self.h6],
            [self.a7, self.b7, self.c7, self.d7, self.e7, self.f7, self.g7, self.h7],
            [self.a8, self.b8, self.c8, self.d8, self.e8, self.f8, self.g8, self.h8]
        ]

        chess_piese_list = []
        self.move_save = []

        for name in self.chess_board_list[6]:
            name.setText('♟')

        for name1 in self.chess_board_list[1]:
            name1.setText('♙')

        for row in range(8):
            for column in range(8):
                self.chess_board_list[row][column].clicked.connect(
                    functools.partial(self.press_field, row=row, column=column)
                )

        '''
        for self.dick_index in range (8):
            for self.dick in chess_board_list[self.dick_index]:
                self.dick.clicked.connect(functools.partial(self.press_field, first_press = self.dick, first_press_index = self.dick_index))
        '''
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
        self.a8.setText('♜')
        self.b8.setText('♞')
        self.c8.setText('♝')
        self.d8.setText('♛')
        self.e8.setText('♚')
        self.f8.setText('♝')
        self.g8.setText('♞')
        self.h8.setText('♜')

    def press_field(self, row, column):
        print(row, column)
        self.move_save.append({'row': row, 'column': column})
        print(self.move_save)
        self.check()

    def check(self):
        if len(self.move_save) == 2:
            rowFrom = self.move_save[0]['row']
            columnFrom = self.move_save[0]['column']
            fromText = self.chess_board_list[rowFrom][columnFrom].text()
            self.chess_board_list[rowFrom][columnFrom].setText('')
            rowTo = self.move_save[1]['row']
            columnTo = self.move_save[1]['column']
            self.chess_board_list[rowTo][columnTo].setText(fromText)
            self.move_save.clear()


        '''
        self.dirlist = self # !!!
        if self.dirlist:
            self.chess_move.setText(self.dirlist)
        else:
            self.lineEdit.clear()
        '''
    def from_to_other(self):
        self.label.setText(self.dirlist)  # !!!

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


