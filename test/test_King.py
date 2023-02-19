from unittest import TestCase

from King import King


class TestKing(TestCase):
    def test_rule_moveOneForward_true(self):
        testee = King("[]", 1, 1)
        result = testee.rule(2, 1)
        self.assertTrue(result)

    def test_rule_moveOneBackwards_true(self):
        testee = King("[]", 3, 1)
        result = testee.rule(2, 1)
        self.assertTrue(result)

    def test_rule_moveOneHorinzontalLeft_true(self):
        testee = King("[]", 4, 5)
        result = testee.rule(4, 4)
        self.assertTrue(result)

    def test_rule_moveOneHorinzontalRight_true(self):
        testee = King("[]", 3, 2)
        result = testee.rule(3, 3)
        self.assertTrue(result)

    def test_rule_moveOneForwardDiogonalLeft_true(self):
        testee = King("[]", 3, 3)
        result = testee.rule(4, 2)
        self.assertTrue(result)

    def test_rule_moveOneForwardDiogonalRight_true(self):
        testee = King("[]", 3, 3)
        result = testee.rule(4, 4)
        self.assertTrue(result)

    def test_rule_moveOneBackwarsDiogonalLeft_true(self):
        testee = King("[]", 3, 3)
        result = testee.rule(2, 2)
        self.assertTrue(result)

    def test_rule_moveOneBackwarsDiogonalRight_true(self):
        testee = King("[]", 3, 3)
        result = testee.rule(2, 4)
        self.assertTrue(result)
        #

    def test_rule_moveTwoForward_false(self):
        testee = King("[]", 1, 1)
        result = testee.rule(3, 1)
        self.assertFalse(result)

    def test_rule_moveTwoBackwards_false(self):
        testee = King("[]", 4, 1)
        result = testee.rule(2, 1)
        self.assertFalse(result)

    def test_rule_moveTwoHorinzontalLeft_false(self):
        testee = King("[]", 4, 5)
        result = testee.rule(4, 3)
        self.assertFalse(result)


    def test_rule_moveTwoHorinzontalRight_false(self):
        testee = King("[]", 4, 5)
        result = testee.rule(4,7)
        self.assertFalse(result)


    def test_rule_moveTwoForwardDiogonalLeft_false(self):
        testee = King("[]", 2, 2)
        result = testee.rule(4, 1)
        self.assertFalse(result)

    def test_rule_moveTwoBackwarsDiogonalLeft_false(self):
        testee = King("[]", 4, 4)
        result = testee.rule(2, 3)
        self.assertFalse(result)

    def test_rule_moveTwoForwardDiogonalRight_True(self):
        testee = King("[]", 4, 2)
        result = testee.rule(6, 3)
        self.assertFalse(result)

    def test_rule_moveTwoBackwarsDiogonalRight_True(self):
        testee = King("[]", 4, 2)
        result = testee.rule(2, 3)
        self.assertFalse(result)
