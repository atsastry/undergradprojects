import unittest
import perm_lex

# Starter test cases - write more!

class TestAssign1(unittest.TestCase):

    def test_perm_gen_lex(self):
        # this test case tests an input string with two characters
        self.assertEqual(perm_lex.perm_gen_lex('ab'),['ab','ba'])
        # this test case tests an input string of one character
        self.assertEqual(perm_lex.perm_gen_lex('a'), ['a'])
        # this test case tests an empty string
        self.assertEqual(perm_lex.perm_gen_lex(""), [])
        # this test case tests an iput slightly longer
        self.assertEqual(perm_lex.perm_gen_lex("abc"), ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])

if __name__ == "__main__":
        unittest.main()
