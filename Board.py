
import numpy
import numpy as np
from Cell import Cell

from Bishop import Bishop
from King import King
from Knight import Knight
from Pawn import Pawn
from Piece import Piece
from Queen import Queen
from Rook import Rook
import array


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
            self.board[row, col] = Cell("|@|", None)

    def printBoard(self):
        print()
        for row in range(self.rows):
            for col in range(self.cols):
                cell: Cell = self.board[row, col]
                if None != cell.piece:
                    print("[ " + cell.piece.name, end='] ')
                else:
                    print("" + cell.color, end='  ')
                if col == 7:
                    print()

    def setAllPiece(self):
        self.setUpperDescription()
        self.setAllPawn()
        self.setRook()
        self.setKings()
        self.setKnight()
        self.setBishop()
        self.setQueen()

    def setUpperDescription(self):
        descriptionCellA: Cell = self.board[2, 1]
        descriptionCellA.setPiece(Piece('A', None, 2, 1))
        descriptionCellB: Cell = self.board[2, 2]
        descriptionCellB.setPiece(Piece('B', None, 2, 2))
        descriptionCellC: Cell = self.board[2, 3]
        descriptionCellC.setPiece(Piece('C', None, 2, 3))

    def setAllPawn(self):
        for col in range(self.cols):
            cellWhite: Cell = self.board[2, col]
            cellBlack: Cell = self.board[7, col]
            cellWhite.setPiece(Pawn("#", 2, col))
            cellBlack.setPiece(Pawn("[ ]", 7, col))

    def setRook(self):
        cellWhiteRook: Cell = self.board[1, 0]
        cellBlackRook: Cell = self.board[6, 0]
        cellWhiteRookOne: Cell = self.board[1, 7]
        cellBlackRookOne: Cell = self.board[6, 7]
        cellWhiteRook.setPiece(Rook("#", 1, 0))
        cellBlackRook.setPiece(Rook("[ ]", 6, 0))
        cellWhiteRookOne.setPiece(Rook("#", 1, 7))
        cellBlackRookOne.setPiece(Rook("[ ]", 6, 7))

    def setKnight(self):
        cellWhiteKnight: Cell = self.board[1, 1]
        cellBlackKnight: Cell = self.board[6, 1]
        cellWhiteKnightOne: Cell = self.board[1, 6]
        cellBlackKnightOne: Cell = self.board[6, 6]
        cellWhiteKnight.setPiece(Knight("#", 1, 1))
        cellBlackKnight.setPiece(Knight("[ ]", 6, 1))
        cellWhiteKnightOne.setPiece(Knight("#", 1, 6))
        cellBlackKnightOne.setPiece(Knight("[ ]", 6, 6))

    def setBishop(self):
        cellWhiteKnight: Cell = self.board[1, 2]
        cellBlackKnight: Cell = self.board[6, 2]
        cellWhiteKnightOne: Cell = self.board[1, 5]
        cellBlackKnightOne: Cell = self.board[6, 5]
        cellWhiteKnight.setPiece(Bishop("#", 1, 2))
        cellBlackKnight.setPiece(Bishop("[ ]", 6, 2))
        cellWhiteKnightOne.setPiece(Bishop("#", 1, 5))
        cellBlackKnightOne.setPiece(Bishop("[ ]", 6, 5))

    def setQueen(self):
        cellWhiteKnight: Cell = self.board[1, 3]
        cellBlackKnight: Cell = self.board[6, 3]
        cellWhiteKnight.setPiece(Queen(" # ", 1, 3))
        cellBlackKnight.setPiece(Queen("[ ]", 6, 3))

    def setKings(self):
        cellWhiteKnight: Cell = self.board[1, 4]
        cellBlackKnight: Cell = self.board[6, 4]
        cellWhiteKnight.setPiece(King("#", 1, 4))
        cellBlackKnight.setPiece(King("[ ]", 6, 4))
