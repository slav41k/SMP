import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_addition(self):
        self.calc.num1 = 5
        self.calc.num2 = 10
        self.calc.operator = '+'
        self.assertEqual(self.calc.calculate(), 15)

    def test_division_by_zero(self):
        self.calc.num1 = 5
        self.calc.num2 = 0
        self.calc.operator = '/'
        with self.assertRaises(ZeroDivisionError):
            self.calc.calculate()

    def test_square_root(self):
        self.calc.num1 = 16
        self.calc.operator = '√'
        self.assertEqual(self.calc.calculate(), 4)

if __name__ == '__main__':
    unittest.main()