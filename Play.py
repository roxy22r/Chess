import Board
import Cell

import Piece


class Play:
    def __init__(self, board: Board):
        self.board = board

    def play(self):
        end: bool = True
        while end:
            print("Please Enter Row Number")
            row = input()
            print("Please Enter Col Number")
            col = input()
            piece: Piece = self.board[row][col]
            self.board[row][col]: Piece = None
