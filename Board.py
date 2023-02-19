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
            self.board[row, col] = Cell(None, "[ ]")
        elif (row % 2) == 1 & (col % 2) == 1:
            self.board[row, col] = Cell(None, "[ ]")
        elif (row % 2) == 0 & (col % 2) == 1:
            self.board[row, col] = Cell(None, "[ ]")
        else:
            self.board[row, col] = Cell(None, "|@|")

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
        self.setAllPawn()
        self.setRook()
        self.setKings()
        self.setKnight()
        self.setBishop()
        self.setQueen()

    def setAllPawn(self):
        for col in range(self.cols):
            cellWhite: Cell = self.board[1, col]
            cellBlack: Cell = self.board[6, col]
            cellWhite.setPiece(Pawn("#", 1, col))
            cellBlack.setPiece(Pawn("[ ]", 6, col))

    def setRook(self):
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
        cellWhiteKnightOne.setPiece(Knight("#", 0, 6))
        cellBlackKnightOne.setPiece(Knight("[ ]", 7, 6))

    def setBishop(self):
        cellWhiteKnight: Cell = self.board[0, 2]
        cellBlackKnight: Cell = self.board[7, 2]
        cellWhiteKnightOne: Cell = self.board[0, 5]
        cellBlackKnightOne: Cell = self.board[7, 5]
        cellWhiteKnight.setPiece(Bishop("#", 0, 2))
        cellBlackKnight.setPiece(Bishop("[ ]", 7, 2))
        cellWhiteKnightOne.setPiece(Bishop("#", 0, 5))
        cellBlackKnightOne.setPiece(Bishop("[ ]", 7, 5))

    def setQueen(self):
        cellWhiteKnight: Cell = self.board[0, 3]
        cellBlackKnight: Cell = self.board[7, 3]
        cellWhiteKnight.setPiece(Queen(" # ", 0, 3))
        cellBlackKnight.setPiece(Queen("[ ]", 7, 3))

    def setKings(self):
        cellWhiteKnight: Cell = self.board[0, 4]
        cellBlackKnight: Cell = self.board[7, 4]
        cellWhiteKnight.setPiece(King("#", 0, 4))
        cellBlackKnight.setPiece(King("[ ]", 7, 4))
    def getCell(self,row:int,coll:int)->Cell:
        return self.board[row][coll]