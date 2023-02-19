from unittest import TestCase

from Pawn import Pawn


class TestPawn(TestCase):

    def test_pawnMovesOneRowForward_true(self):
        self.testee = Pawn("#", 1, 1)
        result = self.testee.rule(2, 1)
        self.assertTrue(result)

    def test_pawnMovesTwoRowForwardFirstMove_true(self):
        self.testee = Pawn("#", 1, 1)
        result = self.testee.rule(3, 1)
        self.assertTrue(result)

    def test_pawnMovesTwoRowForwardInSecondTurn_false(self):
        self.testee = Pawn("#", 1, 1)
        self.testee.rule(3, 1)
        result = self.testee.rule(5, 1)
        self.assertFalse(result)
