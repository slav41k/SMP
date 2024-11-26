import sys
import os
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from function import get_number, get_operator, calculate, save_to_memory, recall_memory, show_history, add_to_history

class TestCalculatorFunctions(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculate(10, 5, '+'), 15)

    def test_subtraction(self):
        self.assertEqual(calculate(10, 5, '-'), 5)

    def test_multiplication(self):
        self.assertEqual(calculate(10, 5, '*'), 50)

    def test_division(self):
        self.assertEqual(calculate(10, 5, '/'), 2)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculate(10, 0, '/')

    def test_power(self):
        self.assertEqual(calculate(2, 3, '^'), 8)

    def test_square_root(self):
        self.assertEqual(calculate(9, None, '√'), 3)

    def test_remainder(self):
        self.assertEqual(calculate(10, 3, '%'), 1)

    def test_memory(self):
        save_to_memory(42)
        self.assertEqual(recall_memory(), 42)

if __name__ == '__main__':
    unittest.main()