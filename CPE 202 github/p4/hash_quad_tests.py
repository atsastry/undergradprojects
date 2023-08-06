import unittest
from hash_quad import *

class TestList(unittest.TestCase):

    def test_01a(self):
        ht = HashTable(6)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_table_size(), 7)

    def test_01b(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_num_items(), 1)

    def test_01c(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertAlmostEqual(ht.get_load_factor(), 1/7)

    def test_01d(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_all_keys(), ["cat"])
        ht.insert("dog", 10)
        ht.insert("stuff", 15)
        self.assertEqual(ht.get_all_keys(), ["stuff", "cat", "dog"])

    def test_01e(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.in_table("cat"), True)

    def test_01f(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_value("cat"), 5)

    def test_01g(self):
        ht = HashTable(7)
        ht.insert("cat", 5)
        self.assertEqual(ht.get_index("cat"), 3)

    def test_02(self):
        ht = HashTable(7)
        ht.insert("a", 0)
        self.assertEqual(ht.get_index("a"), 6)
        ht.insert("h", 0)
        self.assertEqual(ht.get_index("h"), 0)
        ht.insert("o", 0)
        self.assertEqual(ht.get_index("o"), 3)
        ht.insert("v", 0) # Causes rehash
        ht.insert("v", 20)
        self.assertEqual(ht.get_value("v"), 20)
        self.assertEqual(ht.get_index("a"), 12)
        self.assertEqual(ht.get_index("h"), 2)
        self.assertEqual(ht.get_index("o"), 9)
        self.assertEqual(ht.get_index("v"), 16)

    def test_diff_value(self):
        ht = HashTable(6)
        ht.insert("cat", 5)
        ht.insert("cat", 1)
        self.assertEqual(ht.get_value("cat"), 1)

    def test_prime(self):
        ht = HashTable(1)
        self.assertEqual(ht.next_prime(1), 2)
        self.assertTrue(ht.is_prime(3))
        self.assertTrue(ht.next_prime(3))

    def test_more_is_prime(self):
        ht = HashTable(10)
        self.assertFalse(ht.is_prime(121))

    def test_in_table(self):
        ht = HashTable(20)
        ht.insert("hello", 8)
        self.assertTrue(ht.in_table("hello"))
        self.assertFalse(ht.in_table("a"))
        self.assertEqual(ht.get_index("b"), None)
        self.assertEqual(ht.get_value("b"), None)

    def test_diff_value_2(self):
        ht = HashTable(2)
        ht.insert("h", 1)
        # print(ht.hash)
        self.assertEqual(ht.get_index("h"), 0)
        ht.insert("i", 3)
        self.assertEqual(ht.get_index("i"), 0)
        ht.insert("h", 2)
        self.assertEqual(ht.get_value("h"), 2)
        self.assertEqual(ht.get_index("h"), 4)

    def test_get_index(self):
        ht = HashTable(4)
        ht.insert("cat")
        ht.insert("catapult")
        #ht.insert("b")
        # print(ht.hash)
        self.assertEqual(ht.get_index("catapults"), None)
        ht.insert("catapultss")
        ht.insert("catapults", 1)
        ht.insert("catapults", 2)
        self.assertEqual(ht.get_value("catapults"), 2)



if __name__ == '__main__':
   unittest.main()