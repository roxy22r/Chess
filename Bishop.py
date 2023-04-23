from Piece import Piece
from math import factorial


class Bishop(Piece):


    name = u"\u2657"

    def __init__(self, color, rowPos, colPos):
        self.color = color
        self.rowPos = rowPos
        self.colPos = colPos
        pass

    def rule(self, row, col) -> bool:
        return self.rowPos - row == self.colPos - col or row - self.rowPos == col - self.colPos or self.rowPos - row == col - self.colPos or row - self.colPos == self.colPos - col

    def wrongMoveText(self) -> str:
        return "Bishop can only walk diagonal"

    def ruleException(self, row, col, isOppositeColorOnPos) -> bool:
        return False