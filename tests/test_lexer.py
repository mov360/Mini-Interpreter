import unittest
from interpreter import *

class TestLexer(unittest.TestCase):

    def test_number_token(self):
        tokens = list(tokenize("123"))
        self.assertEqual(tokens, [('NUM', '123')])

    def test_variable_token(self):
        tokens = list(tokenize("variable"))
        self.assertEqual(tokens, [('VARIABLE', 'variable')])

    def test_addition_token(self):
        tokens = list(tokenize("+"))
        self.assertEqual(tokens, [('PLUS', '+')])

    def test_multiple_tokens(self):
        tokens = list(tokenize("x + 2"))
        self.assertEqual(tokens, [('VARIABLE', 'x'), ('PLUS', '+'), ('NUM', '2')])

    def test_invalid_token(self):
        with self.assertRaises(SyntaxError):
            list(tokenize("!"))

if __name__ == '__main__':
    unittest.main()
