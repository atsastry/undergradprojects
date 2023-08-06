import unittest
from binary_search_tree import *

class TestLab5(unittest.TestCase):

    def test_simple(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        bst.insert(10, 'stuff')
        bst.insert(9, 'what')
        bst.insert(11, 'next')
        self.assertTrue(bst.search(10))
        self.assertFalse(bst.search(16))
        self.assertEqual(bst.find_min(), (9, 'what'))
        bst.insert(12, 'other')
        self.assertEqual(bst.find_max(), (12, 'other'))
        self.assertEqual(bst.tree_height(), 2)
        self.assertEqual(bst.inorder_list(), [9, 10, 11, 12])
        self.assertEqual(bst.preorder_list(), [10, 9, 11, 12])
        self.assertEqual(bst.level_order_list(), [10, 9, 11, 12])

    def test_simple_2(self):
        bst_2 = BinarySearchTree()
        self.assertTrue(bst_2.is_empty())
        bst_2.insert(10, 'paul')
        bst_2.insert(9, 'hatal')
        bst_2.insert(11, 'imgettingsick')
        bst_2.insert(20, 'test')
        bst_2.insert(50, 'right')
        self.assertEqual(bst_2.tree_height(), 3)
        bst_2.insert(51, 'more')
        bst_2.insert(55, 'dang')
        bst_2.insert(40, 'hearth')
        bst_2.insert(15, 'ogre')
        bst_2.insert(90, 'womeninstem')
        self.assertEqual(bst_2.tree_height(), 6)

    def test_simple_3(self):
        bst_3 = BinarySearchTree()
        self.assertTrue(bst_3.is_empty())
        bst_3.insert(23, 'paul')
        self.assertEqual(bst_3.tree_height(), 0)
        bst_3.insert(90, 'teach')
        bst_3.insert(11, 'imgettingsick')
        self.assertEqual(bst_3.tree_height(), 1)
        bst_3.insert(51, 'test')
        bst_3.insert(31, 'right')
        self.assertTrue(bst_3.search(23))
        self.assertFalse(bst_3.search(20))
        self.assertEqual(bst_3.tree_height(), 3)

    def test_simple_4(self):
        bst_4 = BinarySearchTree()
        self.assertTrue(bst_4.is_empty())
        bst_4.insert(10, 'wettext')
        bst_4.insert(9, 'ciar')
        bst_4.insert(5, 'spru')
        bst_4.insert(100, 'al')
        bst_4.insert(31, 'maddie')
        self.assertFalse(bst_4.search(23))
        self.assertFalse(bst_4.search(20))
        self.assertEqual(bst_4.tree_height(), 2)

    def test_simple_5(self):
        bst_5 = BinarySearchTree()
        bst_5.insert(5, 'hi')
        bst_5.insert(4, 'rally')
        self.assertEqual(bst_5.level_order_list(), [5, 4])
        self.assertEqual(bst_5.find_min(), (4, 'rally'))

    def test_simple_6(self):
        bst_6 = BinarySearchTree()
        bst_6.insert(10, 'first')
        bst_6.insert(20, 'second')
        bst_6.insert(5, "third")
        bst_6.insert(25, 'fourth')
        bst_6.insert(1, 'fifth')
        self.assertEqual(bst_6.tree_height(), 2)

    def test_simple_7(self):
        bst_7 = BinarySearchTree()
        self.assertFalse(bst_7.search(1), None)
        bst_7.insert(1, 'dawg')
        bst_7.insert(0, 'lol')
        bst_7.insert(2, 'box')
        self.assertTrue(bst_7.search(0))
        self.assertFalse(bst_7.search(0.5))
        self.assertFalse(bst_7.search(3))
        bst_7.insert(1, 'dawg')

    def test_simple_8(self):
        bst_8 = BinarySearchTree()
        self.assertEqual(bst_8.find_min(), None)
        self.assertEqual(bst_8.find_max(), None)
        self.assertEqual(bst_8.preorder_list(), [])
        self.assertEqual(bst_8.level_order_list(), [])

    def test_simple_9(self):
        bst_9 = BinarySearchTree()
        bst_9.insert(10)
        self.assertFalse(bst_9.search(1))
        self.assertFalse(bst_9.search(20))

    def test_simple_10(self):
        bst_10 = BinarySearchTree()
        bst_10.insert(16)
        bst_10.insert(8)
        bst_10.insert(20)
        self.assertEqual(bst_10.search(4), False)
        self.assertEqual(bst_10.search(25), False)
        self.assertFalse(bst_10.search(4))
        self.assertFalse(bst_10.search(25))

    def test_simple_11(self):
        bst_11 = BinarySearchTree()
        bst_11.insert(20)
        bst_11.insert(30)
        bst_11.insert(10)
        self.assertFalse(bst_11.search(1))
        self.assertFalse(bst_11.search(35))



if __name__ == '__main__': 
    unittest.main()