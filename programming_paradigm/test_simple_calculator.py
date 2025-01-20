import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(3, 2), 1)
        self.assertEqual(self.calc.subtract(5, 2), 3)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(5, 1), 5)
        
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        
        self.assertRaises(None, SimpleCalculator, 10, 0)