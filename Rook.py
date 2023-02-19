from Piece import Piece


class Rook(Piece):
    name = "R"

    def __init__(self, color, rowPos:int, colPos:int):
        self.color = color
        self.rowPos = rowPos
        self.colPos = colPos
        pass

    def rule(self, row, col) -> bool:
        return self.rowPos < row and self.colPos == col or self.rowPos > row and self.colPos == col or self.colPos > col and self.rowPos == row or self.colPos < col and self.rowPos == row
