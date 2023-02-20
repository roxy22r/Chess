from unittest import TestCase

from Bishop import Bishop


class TestBishop(TestCase):
    def test_rule_3DiagonalUpLeft_true(self):
        testee = Bishop("[]", 4, 7)
        result = testee.rule(7, 4)
        self.assertTrue(result)

    def test_rule_2DiagonalDownLeft_true(self):
        testee = Bishop("[]", 3, 6)
        result = testee.rule(1, 4)
        self.assertTrue(result)

    def test_rule_5DiagonalUpRight_true(self):
        testee = Bishop("[]", 1, 2)
        result = testee.rule(6, 7)
        self.assertTrue(result)

    def test_rule_4DiagonalDownRight_true(self):
        testee = Bishop("[]", 6, 7)
        result = testee.rule(2, 3)
        self.assertTrue(result)

    def test_rule_4DiagonalUpRightAndOneForward_false(self):
        testee = Bishop("[]", 1, 1)
        result = testee.rule(5, 6)
        self.assertFalse(result)

    def test_rule_4DiagonalDownLefttAndOneDown_false(self):
        testee = Bishop("[]", 5, 6)
        result = testee.rule(1, 1)
        self.assertFalse(result)