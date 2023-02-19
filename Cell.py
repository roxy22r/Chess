from Piece import Piece


class Cell:
    def __init__(self, piece: Piece, color: str):
        self.piece = piece
        self.color = color

    def setPiece(self, piece: Piece):
        self.piece = piece
