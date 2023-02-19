from unittest import TestCase

from Knight import Knight


class TestKnight(TestCase):

    def test_rule_TwoRowForwardAndOneLeft_True(self):
        testee = Knight("[]", 2, 2)
        result = testee.rule(4, 1)
        self.assertTrue(result)

    def test_rule_TwoRowBackwardAndOneLeft_True(self):
        testee = Knight("[]", 3, 2)
        result = testee.rule(1, 1)
        self.assertTrue(result)

    def test_rule_TwoRowForwardAndOneRight_True(self):
        testee = Knight("[]", 2, 2)
        result = testee.rule(4, 3)
        self.assertTrue(result)

    def test_rule_TwoRowBackwardAndOneRight_True(self):
        testee = Knight("[]", 3, 2)
        result = testee.rule(1, 3)
        self.assertTrue(result)

    def test_rule_TwoRowForwardAndTwoLeft_False(self):
        testee = Knight("[]", 2, 4)
        result = testee.rule(4, 2)
        self.assertFalse(result)
