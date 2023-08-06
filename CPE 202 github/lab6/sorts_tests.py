import unittest
from sorts import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        nums = [23, 10]
        comps = selection_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 23])

    def test_selection_sort_2(self):
        nums_2 = [12, 10, 13, 1]
        comps = selection_sort(nums_2)
        self.assertEqual(comps, 6)
        self.assertEqual(nums_2, [1, 10, 12, 13])

    def test_selection_sort_3(self):
        nums_3 = [10, 20, 12, 7, 18]
        comps_3 = selection_sort(nums_3)
        self.assertEqual(comps_3, 10)
        self.assertEqual(nums_3, [7, 10, 12, 18, 20])

    # this doesn't pass, says comparisons should be 0
    def test_selection_sort_4(self):
        nums_4 = [1, 1, 1, 1, 1, 1, 1, 1]
        comps = selection_sort(nums_4)
        self.assertEqual(comps, 28)
        self.assertEqual(nums_4, [1, 1, 1, 1, 1, 1, 1, 1])

    def test_selection_sort_5(self):
        nums_5 = []
        comps = selection_sort(nums_5)
        self.assertEqual(comps, 0)
        self.assertEqual(nums_5, [])

# test below is wrong for comparisons
    def test_insertion_sort(self):
        nums = [12, 3, 4]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 3)
        self.assertEquals(nums, [3, 4, 12])

    def test_insertion_sort_2(self):
        nums_2 = [1, 10, 100, 42, 34, 56]
        comps = insertion_sort(nums_2)
        self.assertEqual(comps, 9)
        self.assertEqual(nums_2, [1, 10, 34, 42, 56, 100])

    def test_insertion_sort_3(self):
        nums_3 = [1, 1, 1, 1, 1, 1, 1, 1]
        comps = insertion_sort(nums_3)
        self.assertEqual(comps, 7)
        self.assertEqual(nums_3, [1, 1, 1, 1, 1, 1, 1, 1])

    def test_insertion_sort_4(self):
        nums_4 = []
        comps = insertion_sort(nums_4)
        self.assertEqual(comps, 0)
        self.assertEqual(nums_4, [])



if __name__ == '__main__':
    unittest.main()