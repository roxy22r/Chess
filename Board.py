import array

import numpy
import numpy as np
from Cell import Cell

from Pawn import Pawn
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
            self.board[row, col] = Cell("[ ]", None)
        elif (row % 2) == 1 & (col % 2) == 1:
            self.board[row, col] = Cell("[ ]", None)
        elif (row % 2) == 0 & (col % 2) == 1:
            self.board[row, col] = Cell("[ ]", None)
        else:
            self.board[row, col] = Cell("#", None)

    def printBoard(self):
        print()
        for row in range(self.rows):
            for col in range(self.cols):
                cell: Cell = self.board[row, col]
                if None != cell.piece:
                    print(" " + cell.piece.name, end=' ')
                else:
                    print("  " + cell.color, end=' ')
                if col == 7:
                    print()

    def setAllPiece(self):
        self.setAllPawn()

    def setAllPawn(self):
        for col in range(self.cols):
            cellWhite: Cell = self.board[1, col]
            cellBlack: Cell = self.board[6, col]
            cellWhite.setPiece(Pawn("{P}", "#", 1, col))
            cellBlack.setPiece(Pawn("[P]", "#", 6, col))


board = Board()
board.printBoard()
board.setAllPiece()
board.printBoard()
