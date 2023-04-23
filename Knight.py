from Piece import Piece


class Knight(Piece):



    name = 	u"\u2658"

    def __init__(self, color, rowPos, colPos):
        self.color = color
        self.rowPos = rowPos
        self.colPos = colPos
        pass

    def rule(self, row, col) -> bool:
        return self.rowPos + 2 == row and self.colPos - 1 == col or self.rowPos - 2 == row and self.colPos - 1 == col or \
        self.rowPos + 2 == row and self.colPos + 1 == col or self.rowPos - 2 == row and self.colPos + 1 == col

    def ruleException(self, row, col, isOppositeColorOnPos) -> bool:
        pass

    def wrongMoveText(self) -> str:
        return  "The knight can only walk in an L shape 2 for/back/side wards and one left or right"