import unittest, os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../classes')))
from calc import BasicCalculator, ScientificCalculator

class TestBasicCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = BasicCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.calculate(10, 5, '+'), 15)
        self.assertEqual(self.calc.calculate(-3, -7, '+'), -10)

    def test_subtraction(self):
        self.assertEqual(self.calc.calculate(10, 5, '-'), 5)
        self.assertEqual(self.calc.calculate(-3, -7, '-'), 4)

    def test_multiplication(self):
        self.assertEqual(self.calc.calculate(10, 5, '*'), 50)
        self.assertEqual(self.calc.calculate(0, 5, '*'), 0)
        self.assertEqual(self.calc.calculate(-3, 5, '*'), -15)

    def test_division(self):
        self.assertEqual(self.calc.calculate(10, 5, '/'), 2)
        self.assertEqual(self.calc.calculate(-10, 5, '/'), -2)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.calculate(10, 0, '/')

class TestScientificCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = ScientificCalculator()

    def test_power(self):
        self.assertEqual(self.calc.calculate(2, 3, '^'), 8)

    def test_square_root(self):
        self.assertEqual(self.calc.calculate(9, None, '√'), 3)

    def test_remainder(self):
        self.assertEqual(self.calc.calculate(10, 3, '%'), 1)

    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            self.calc.calculate(5, 3, '#')

if __name__ == '__main__':
    unittest.main()