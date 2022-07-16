from Piece import Piece


class Pawn(Piece):
    name = "P"
    def __init__(self, color, rowPos, colPos):
        self.color = color
        self.rowPos = rowPos
        self.colPos = colPos
        pass
