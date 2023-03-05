from unittest import TestCase

from Pawn import Pawn


class TestPawn(TestCase):

    def test_pawnMovesOneRowForward_true(self):
        testee = Pawn("#", 1, 1)
        result = testee.rule(2, 1)
        self.assertTrue(result)

    def test_pawnMovesTwoRowForwardFirstMove_true(self):
        testee = Pawn("#", 1, 1)
        result = testee.rule(3, 1)
        self.assertTrue(result)

    def test_pawnMovesTwoRowForwardInSecondTurn_false(self):
        testee = Pawn("#", 1, 1)
        testee.rule(3, 1)
        result = testee.rule(5, 1)
        self.assertFalse(result)

    def test_ruleExceptionWhenOppositeFigurColorIsInFirstDiogonalFrontRight_true(self):
        testee = Pawn("#", 1, 1)
        result = testee.ruleException(2, 2, True)
        self.assertTrue(result)

    def test_ruleExceptionWhenOppositeFigurColorIsInFirstDiogonalLeft_true(self):
        testee = Pawn("#", 1, 6)
        result = testee.ruleException(2, 5, True)
        self.assertTrue(result)

    def test_ruleExceptionWhenOppositeFigurColorIsInBackDiogonaRight_false(self):
        testee = Pawn("[]", 4, 4)
        result = testee.ruleException(3, 5, False)
        self.assertFalse(result)

    def test_ruleExceptionWhenOppositeFigurColorIsInBackDiogonaLeft_false(self):
        testee = Pawn("[]", 3, 3)
        result = testee.ruleException(2, 2, False)
        self.assertFalse(result)

    def test_ruleExceptionWhenOppositeFigurColorIsInBackTwoDiogonaLeft_false(self):
        testee = Pawn("[]", 5, 5)
        result = testee.ruleException(3, 3, False)
        self.assertFalse(result)

    def test_ruleExceptionWhenOppositeFigurColorIsInFrontTwoDiogonaRight_false(self):
        testee = Pawn("[]", 6, 6)
        result = testee.ruleException(4, 4, False)
        self.assertFalse(result)

