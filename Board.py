import array

import numpy
import numpy as np
from Cell import Cell

from Piece import Piece


class Board:
    rows, cols = (8, 8)
    board = np.full([rows, cols], Cell(None, None))

    def __init__(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.setCellColor(row, col)

    def setCellColor(self, row, col):

        if (row % 2) == 1 & (col % 2) == 0:
            self.board[row, col] = Cell("[]", None)
        elif (row % 2) == 1 & (col % 2) == 1:
            self.board[row, col] = Cell("[]", None)
        elif (row % 2) == 0 & (col % 2) == 1:
            self.board[row, col] = Cell("[]", None)
        else:
            self.board[row, col] = Cell("#", None)

    def printBoard(self):
        print()
        for row in range(self.rows):
            for col in range(self.cols):
                cell: Cell = self.board[row, col]
                print(" " + cell.color, end='')
                if col == 7:
                    print()


tet = Board()
tet.printBoard()
