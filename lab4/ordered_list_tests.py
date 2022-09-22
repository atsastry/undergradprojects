import unittest
from ordered_list import *


class TestLab4(unittest.TestCase):

    def test_simple(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
        t_list.add(10)
        self.assertEqual(t_list.pop(0), 10)

    def test_simple_02(self):
        x_list = OrderedList()
        x_list.add(10)
        self.assertEqual(x_list.python_list(), [10])
        self.assertFalse(x_list.add(10))
        x_list.add(5)
        self.assertEqual(x_list.python_list(), [5, 10])
        x_list.add(30)
        self.assertEqual(x_list.python_list(), [5, 10, 30])
        self.assertFalse(x_list.add(10))
        x_list.add(50)
        self.assertEqual(x_list.python_list(), [5, 10, 30, 50])

    def test_simple_03(self):
        y_list = OrderedList()
        y_list.add(5)
        y_list.add(10)
        y_list.add(15)
        y_list.add(12)
        self.assertEqual(y_list.python_list(), [5, 10, 12, 15])

    def test_simple_04(self):
        a_list = OrderedList()
        a_list.add(5)
        a_list.add(10)
        a_list.add(15)
        a_list.add(12)
        a_list.remove(10)
        self.assertEqual(a_list.python_list(), [5, 12, 15])

    def test_simple_05(self):
        a_list = OrderedList()
        a_list.add(5)
        a_list.add(10)
        a_list.add(15)
        a_list.add(12)
        self.assertFalse(a_list.remove(100))

    def test_simple_06(self):
        b_list = OrderedList()
        b_list.add(1)
        b_list.add(2)
        b_list.add(3)
        self.assertEqual(b_list.index(2), 1)

    def test_simple_07(self):
        b_list = OrderedList()
        b_list.add(1)
        b_list.add(2)
        b_list.add(3)
        self.assertEqual(b_list.index(4), None)

    # pop does not work if you try to pop middle elements
    def test_simple_08(self):
        c_list = OrderedList()
        c_list.add(3)
        c_list.add(6)
        c_list.add(9)
        c_list.add(12)
        self.assertEqual(c_list.pop(0), 3)

    def test_simple_09(self):
        c_list = OrderedList()
        c_list.add(3)
        c_list.add(6)
        c_list.add(9)
        c_list.add(12)
        try:
            c_list.pop(-1)
            self.fail()
        except IndexError:
            self.assertRaises(IndexError)

    def test_simple_10(self):
        d_list = OrderedList()
        d_list.add(1)
        d_list.add(2)
        d_list.add(3)
        d_list.add(4)
        d_list.add(5)
        self.assertFalse(d_list.search(6))

    def test_simple_11(self):
        g_list = OrderedList()
        g_list.add(10)
        g_list.add(20)
        g_list.add(30)
        g_list.add(40)
        g_list.add(50)
        self.assertFalse(g_list.search(6))

    def test_simple_12(self):
        k_list = OrderedList()
        k_list.add(10)
        k_list.add(20)
        k_list.add(15)
        k_list.add(19)
        self.assertEqual(k_list.python_list(), [10, 15, 19, 20])

    def test_simple_13(self):
        c_list = OrderedList()
        c_list.add(3)
        c_list.add(6)
        c_list.add(9)
        c_list.add(12)
        self.assertEqual(c_list.pop(1), 6)

    def test_simple_14(self):
        c_list = OrderedList()
        c_list.add(10)
        self.assertEqual(c_list.python_list(), [10])

    def test_simple_15(self):
        k_list = OrderedList()
        k_list.add(10)
        k_list.add(30)
        k_list.add(52)
        k_list.add(1)
        self.assertEqual(k_list.python_list(), [1, 10, 30, 52])



if __name__ == '__main__':
    unittest.main()