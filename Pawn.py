from Piece import Piece


class Pawn(Piece):
    def __init__(self, name, color, rowPos, colPos):
        self.name = name
        self.color = color
        self.rowPos = rowPos
        self.colPos = colPos
        pass
