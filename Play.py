import Board
import Cell

import Piece


class Play:

    def __init__(self, board: Board):
        self.board = board

    def play(self):
        end: bool = True
        while end:
            self.board.printBoard()
            row = int(input("Please enter row number of piece"))
            col = int(input("Please enter col number of piece"))
            cell: Cell = self.board.getCell(row, col)
            piece: Piece = cell.piece
            cell.setPiece(None)
            print("You choose", piece.name, "to move")
            row = int(input("Please enter row number to move"))
            col = int(input("Please enter col number to move"))
            if piece.rule(row, col):
                cell: Cell = self.board.getCell(row, col)
                cell.setPiece(piece)
            else:
                print("You can't move Player that way")