import unittest
from src.calculator import mult

class TestMult(unittest.TestCase):
    def test_mult_positive(self):
        self.assertEqual(mult(3, 4), 12)
    def test_mult_negative(self):
        self.assertEqual(mult(-3, 4), -12)
    def test_mult_zero(self):
        self.assertEqual(mult(0, 5), 0)

if __name__ == '__main__':
    unittest.main()