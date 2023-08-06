import unittest
from bears import *

# Starter test cases - write more!

class TestAssign1(unittest.TestCase):
    def test_bear_01(self):
        self.assertTrue(bears(250))

    def test_bear_02(self):
        self.assertTrue(bears(42))

    def test_bear_03(self):
        self.assertFalse(bears(53))

    def test_bear_04(self):
        self.assertFalse(bears(41))

    def test_bear_05(self):
        # this test case runs the function if the input value is an even number and returns False
        self.assertFalse(bears(60))

    def test_bear_06(self):
        # this test case runs the function if the input value is an even number and returns True
        self.assertTrue(bears(84))

    def test_bear_07(self):
        # this test case runs the function if the input value is divisible by 3 and returns False
        self.assertFalse(bears(51))

    def test_bear_08(self):
        # this test case runs the function if the input value is divisible by 3 and returns True
        self.assertTrue(bears(210))

    def test_bear_09(self):
        # this test case runs the function if the input value is divisible by 4 and returns False
        self.assertFalse(bears(40))

    def test_bear_10(self):
        # this test case runs the function if the input value is divisible by 4 and returns True
        self.assertTrue(bears(168))



if __name__ == "__main__":
    unittest.main()
