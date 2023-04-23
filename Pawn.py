from Piece import Piece


class Pawn(Piece):
    isFirstMoveDone = False
    name = u"\u2659"
    nameB = u"\u265F"

    def __init__(self, color, rowPos, colPos):
        self.color = color
        self.rowPos = rowPos
        self.colPos = colPos
        pass

    def rule(self, moveToRow, moveToCol) -> bool:
        isFirstMove = not self.isFirstMoveDone
        self.isFirstMoveDone = False
        return moveToRow - self.rowPos == 1 and self.rowPos == moveToCol or isFirstMove and moveToRow - self.rowPos == 2 and self.rowPos == moveToCol

    def ruleException(self, row, col, isOppositeColorOnPos) -> bool:
        return (row - self.rowPos) == 1 and (col - self.colPos) == 1 and isOppositeColorOnPos or \
               (row - self.rowPos) == 1 and (self.colPos - col) == 1

    def wrongMoveText(self) -> str:
        return "You can Only move two forward in the beginning"
