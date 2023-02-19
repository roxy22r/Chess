from abc import ABC, abstractmethod


class Piece(ABC):

    def __init__(self, name, color, rowPos, colPos):
        self.name = name
        self.color = color
        self.rowPos = rowPos
        self.colPos = colPos

    @abstractmethod
    def rule(self, row, col) -> bool:
        ''' To override '''
        pass
