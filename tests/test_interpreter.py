import unittest
from interpreter import *

class TestInterpreter(unittest.TestCase):

    def evaluate_expression(self, expression):
        tokens = list(tokenize(expression))
        parser = Parser(tokens)
        tree = parser.parse()
        evaluator = Evaluator()
        return evaluator.eval(tree)

    def test_basic_addition(self):
        self.assertEqual(self.evaluate_expression("3 + 4"), 7)

    def test_multiplication_and_subtraction(self):
        self.assertEqual(self.evaluate_expression("10 - 2 * 3"), 4)

    def test_parentheses(self):
        self.assertEqual(self.evaluate_expression("(10 - 2) * 3"), 24)

if __name__ == '__main__':
    unittest.main()
