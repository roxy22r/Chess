from Piece import Piece


class King(Piece):
    name = "?"

    def __init__(self, color, rowPos, colPos):
        self.color = color
        self.rowPos = rowPos
        self.colPos = colPos
        pass

    def rule(self, row, col) -> bool:
        return self.__isHoritontalAllowed(row, col) or self.__isVerticalAllowed(row,col) or \
               self.__isDiogonalLeftAllowed(row, col) or self.__isDiogonalRightAllowed(row, col)

    def __isVerticalAllowed(self, row, col) -> bool:
        return row - self.rowPos == 1 and self.colPos == col or self.rowPos - row == 1 and self.colPos == col

    def __isHoritontalAllowed(self, row, col) -> bool:
        return self.rowPos == row and self.colPos - col == 1 or self.rowPos == row and col - self.colPos == 1

    def __isDiogonalLeftAllowed(self, row, col) -> bool:
        return self.rowPos - 1 == row and self.colPos - 1 == col or self.rowPos + 1 == row and self.colPos - 1 == col

    def __isDiogonalRightAllowed(self, row, col) -> bool:
        return self.rowPos - 1 == row and self.colPos +1 == col or self.rowPos + 1 == row and self.colPos + 1 == col