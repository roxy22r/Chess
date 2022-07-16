import array

import numpy
import numpy as np
from Cell import Cell

from Knight import Knight
from Pawn import Pawn
from Piece import Piece
from Rook import Rook


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
                    print("[ " + cell.piece.name, end='] ')
                else:
                    print("  " + cell.color, end=' ')
                if col == 7:
                    print()

    def setAllPiece(self):
        self.setAllPawn()
        self.setKings()
        self.setKnight()

    def setAllPawn(self):
        for col in range(self.cols):
            cellWhite: Cell = self.board[1, col]
            cellBlack: Cell = self.board[6, col]
            cellWhite.setPiece(Pawn("#", 1, col))
            cellBlack.setPiece(Pawn("[ ]", 6, col))

    def setKings(self):
        cellWhiteRook: Cell = self.board[0, 0]
        cellBlackRook: Cell = self.board[7, 0]
        cellWhiteRookOne: Cell = self.board[0, 7]
        cellBlackRookOne: Cell = self.board[7, 7]
        cellWhiteRook.setPiece(Rook("#", 0, 0))
        cellBlackRook.setPiece(Rook("[ ]", 7, 0))
        cellWhiteRookOne.setPiece(Rook("#", 0, 7))
        cellBlackRookOne.setPiece(Rook("[ ]", 7, 7))

    def setKnight(self):
        cellWhiteKnight: Cell = self.board[0, 1]
        cellBlackKnight: Cell = self.board[7, 1]
        cellWhiteKnightOne: Cell = self.board[0, 6]
        cellBlackKnightOne: Cell = self.board[7, 6]
        cellWhiteKnight.setPiece(Knight("#", 0, 1))
        cellBlackKnight.setPiece(Knight("[ ]", 7, 1))
        cellWhiteKnightOne.setPiece(Knight("#", 0, 6 ))
        cellBlackKnightOne.setPiece(Knight("[ ]", 7, 6))

board = Board()
board.printBoard()
board.setAllPiece()
board.printBoard()
