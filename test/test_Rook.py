from unittest import TestCase

from Rook import Rook


class TestRook(TestCase):
    def test_rule_rookMoves4Forward_True(self):
        testee = Rook("#", 7, 7)
        result = testee.rule(3, 7)
        self.assertTrue(result)

    def test_rule_rookMoves4backward_True(self):
        testee = Rook("#", 3, 7)
        result = testee.rule(7, 7)
        self.assertTrue(result)

    def test_rule_rookMovesHorinzontalRight_True(self):
        testee = Rook("#", 3, 3)
        result = testee.rule(3, 7)
        self.assertTrue(result)

    def test_rule_rookMovesHorinzontalLeft_True(self):
        testee = Rook("#", 3, 7)
        result = testee.rule(3, 3)
        self.assertTrue(result)

    def test_rule_rookMovesHorinzontalLeftAnd2Forward_True(self):
        testee = Rook("#", 3, 7)
        result = testee.rule(5, 3)
        self.assertFalse(result)

    def test_rule_rookMovesHorinzontalRighAnd2Backwards_True(self):
        testee = Rook("#", 5, 2)
        result = testee.rule(3, 6)
        self.assertFalse(result)
