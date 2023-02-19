from Piece import Piece


class Knight(Piece):
    name = "K"

    def __init__(self, color, rowPos, colPos):
        self.color = color
        self.rowPos = rowPos
        self.colPos = colPos
        pass

    def rule(self, row, col) -> bool:
        return self.rowPos + 2 == row and self.colPos - 1 == col or self.rowPos - 2 == row and self.colPos - 1 == col or \
        self.rowPos + 2 == row and self.colPos + 1 == col or self.rowPos - 2 == row and self.colPos + 1 == col

