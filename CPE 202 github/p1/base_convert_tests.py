import unittest
from base_convert import *


class TestBaseConvert(unittest.TestCase):

    def test_base2(self):
        self.assertEqual(convert(45, 2), "101101")

    def test_base4(self):
        self.assertEqual(convert(30, 4), "132")

    def test_base16(self):
        self.assertEqual(convert(316, 16), "13C")

    def test_base_16_2(self):
        self.assertEqual(convert(15, 16), "F")

    def test_base_16_3(self):
        self.assertEqual(convert(10, 16), "A")

    def test_base_16_4(self):
        self.assertEqual(convert(11, 16), "B")

    def test_base_16_5(self):
        self.assertEqual(convert(13, 16), "D")

    def test_base_16_6(self):
        self.assertEqual(convert(14, 16), "E")


if __name__ == "__main__":
    unittest.main()
