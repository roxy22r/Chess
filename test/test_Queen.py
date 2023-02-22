from unittest import TestCase

from Queen import Queen


class TestQueen(TestCase):

    def test_rule_3Forward_true(self):
        testee = Queen("#", 1, 1)
        result = testee.rule(4, 1)
        self.assertTrue(result)

    def test_rule_2Backward_true(self):
        testee = Queen("#", 3, 1)
        result = testee.rule(1, 1)
        self.assertTrue(result)

    def test_rule_4HorinzontalLeft_true(self):
        testee = Queen("#", 3, 6)
        result = testee.rule(3, 2)
        self.assertTrue(result)


    def test_rule_3HorinzontalRight_true(self):
        testee = Queen("#", 2, 3)
        result = testee.rule(2, 6)
        self.assertTrue(result)

    def test_rule_2DiagonalLeftUp_true(self):
        testee = Queen("#", 3, 3)
        result = testee.rule(5, 1)
        self.assertTrue(result)

    def test_rule_4DiagonalRightDown_true(self):
        testee = Queen("#", 3, 3)
        result = testee.rule(5, 1)
        self.assertTrue(result)

    def test_rule_3DiagonalRightDownAndOneLeft_false(self):
        testee = Queen("#", 5, 5)
        result = testee.rule(2, 1)
        self.assertFalse(result)

    def test_rule_3DiagonalLeftUpAndOneRight_false(self):
        testee = Queen("#", 7, 7)
        result = testee.rule(4, 5)
        self.assertFalse(result)
