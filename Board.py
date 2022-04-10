import array

import numpy
from Cell import Cell

from Piece import Piece


class Board:
    rows, cols = (8, 8)
    board = []

    def __init__(self):
        for i in range(self.rows):
            col = []
            for j in range(self.cols):
                col.append(Cell(None, None))
                self.board[i][j].append(col)

    # self.board.append(col)

    def printBoard(self):
        for row in self.board:
            for col in row:
                print(col.color)


chessBoard = Board()
chessBoard.printBoard()
