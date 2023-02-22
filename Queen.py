from Piece import Piece


class Queen(Piece):
    name = "Q"

    def __init__(self, color, rowPos, colPos):
        self.color = color
        self.rowPos = rowPos
        self.colPos = colPos
        pass

    def rule(self, row, col) -> bool:
        return self.__isDiogonaAllowed(row, col) or self.__isVerticalAllowed(row,col) or self.__isHoritontalAllowed(row,col)

    def __isVerticalAllowed(self, row, col) -> bool:
        return row - self.rowPos < self.colPos == col or self.rowPos - row < self.rowPos and self.colPos == col

    def __isHoritontalAllowed(self, row, col) -> bool:
        return self.rowPos == row and self.colPos - col < self.colPos or self.rowPos == row and col - self.colPos < self.colPos

    def __isDiogonaAllowed(self, row, col) -> bool:
        return self.rowPos - row == self.colPos - col or row - self.rowPos == col - self.colPos or self.rowPos - row == col - self.colPos or row - self.colPos == self.colPos - col
