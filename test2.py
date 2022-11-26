from PyQt5.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)
        self.someFunction(self.function)
    way = []
    def someFunction(self, differ):
#       buttons = [None] * 8
        chess_board1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        chess_board2 = [1, 2, 3, 4, 5, 6, 7, 8]

            for j in range(8):
                for i in range(8):
                    button = QPushButton("Button {}{}".format(chess_board1[j], chess_board2[i]), self)
                    button.clicked.connect(lambda ch, j=j, i=i: self.differ(j, i))      # < ---
                    self.layout.addWidget(button)

    def function(self, j ,i):
        chess_board1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        chess_board2 = [1, 2, 3, 4, 5, 6, 7, 8]
        self.way.append('{}{}'.format(chess_board1[j], chess_board2[i]))

    def function2(self, j, i):
        chess_board1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        chess_board2 = [1, 2, 3, 4, 5, 6, 7, 8]
        self.way.append('{}{}'.format(chess_board1[j], chess_board2[i]))
        print(self.way[0], self.way[1])

if __name__ == '__main__':
    app = QApplication([])
    mainapp = MainWindow()
    mainapp.show()
    app.exec_()