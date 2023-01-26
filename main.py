import sys
import random
import functools

from PyQt6 import QtWidgets
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.uic import *


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
        piece_board = [
            ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖'],
            ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟'],
            ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜']
        ]
        self.board_buttons_info = [
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            []
        ]

        self.move_save = []

        for row in range(8):
            for column in range(8):
                self.chess_board_list[row][column].clicked.connect(
                    functools.partial(self.press_field, row=row, column=column)
                )

        for row in range(8):
            for column in range(8):
                button = self.chess_board_list[row][column]
                txt = piece_board[row][column]
                figure = '' #пустая клетка
                if txt == '♙' or txt == '♟': #пешка / pawn
                    figure = 'pawn'
                if txt == '♗' or txt == '♝': #слон / bishop
                    figure = 'bishop'
                if txt == '♘' or txt == '♞': #конина / knight
                    figure = 'knight'
                if txt == '♖' or txt == '♜': #ладья / rook
                    figure = 'rook'
                if txt == '♔' or txt == '♚': #король / king
                    figure = 'king'
                if txt == '♕' or txt == '♛': #королева / queen
                    figure = 'queen'

                color = 'none'
                if txt == '♙' or txt == '♗' or txt == '♘' or txt == '♖' or txt == '♔' or txt == '♕': #white
                    color = 'white'
                if txt == '♟' or txt == '♝' or txt == '♞' or txt == '♜' or txt == '♚' or txt == '♛': #black
                    color = 'black'

                a_to_h = 'abcdefgh'
                self.board_buttons_info[row].append({'coord': (a_to_h[column] + str(row + 1)), 'button': button, 'unicode': str(txt), 'type': figure, 'color': color, 'row': row, 'column': column})

        self.board_fill()

    def board_fill(self):
        for row in range(8):
            for column in range(8):
                board_button = self.board_buttons_info[row][column]['button']
                board_button.setText(self.board_buttons_info[row][column]['unicode'])

    def press_field(self, row, column):
        if len(self.move_save) == 0 and self.board_buttons_info[row][column]['unicode'] == '':
            return False
        print(row, column)
        self.move_save.append({'row': row, 'column': column})
        print(self.move_save)
        #print(self.board_buttons_info)

        self.check()


    def check(self):
        if len(self.move_save) != 2:
            return False

        row_from = self.move_save[0]['row']
        column_from = self.move_save[0]['column']
        row_to = self.move_save[1]['row']
        column_to = self.move_save[1]['column']
        from_text = self.board_buttons_info[row_from][column_from]['unicode']
        from_type = self.board_buttons_info[row_from][column_from]['type']
        from_color = self.board_buttons_info[row_from][column_from]['color']

        if from_text == '':
            self.move_save.clear()
            return False

        if self.board_buttons_info[row_from][column_from]['color'] == self.board_buttons_info[row_to][column_to]['color']:
            self.move_save.clear()
            return False

        self.board_buttons_info[row_from][column_from]['unicode'] = ''
        self.board_buttons_info[row_from][column_from]['type'] = ''
        self.board_buttons_info[row_from][column_from]['color'] = 'none'

        self.board_buttons_info[row_to][column_to]['unicode'] = from_text
        self.board_buttons_info[row_to][column_to]['type'] = from_type
        self.board_buttons_info[row_to][column_to]['color'] = from_color

        self.move_save.clear()

        self.board_fill()

        # лейбл с откуда и куда пошла фигура
        '''
        self.dirlist = self # !!!
        if self.dirlist:
            self.chess_move.setText(self.dirlist)
        else:
            self.lineEdit.clear()

    def from_to_other(self):
        self.label.setText(self.dirlist)  # !!!
                '''

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


