from Piece import Piece


class Queen(Piece):
    name = "Q"
    def __init__(self, color, rowPos, colPos):
        self.color = color
        self.rowPos = rowPos
        self.colPos = colPos
        pass
