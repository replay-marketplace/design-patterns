"""Tests for demo_calculator_project module."""
import unittest
import sys
from pathlib import Path

# Add the src directory to the path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from demo_calculator_project import add, subtract, multiply, divide


class TestCalculator(unittest.TestCase):
    """Test cases for calculator functions."""
    
    def test_add(self):
        """Test addition."""
        self.assertEqual(add(2, 3), 5)
    
    def test_subtract(self):
        """Test subtraction."""
        self.assertEqual(subtract(5, 3), 2)
    
    def test_multiply(self):
        """Test multiplication."""
        self.assertEqual(multiply(4, 3), 12)
    
    def test_divide(self):
        """Test division."""
        self.assertEqual(divide(10, 2), 5)
    
    def test_divide_by_zero(self):
        """Test division by zero raises error."""
        with self.assertRaises(ValueError):
            divide(10, 0)


if __name__ == '__main__':
    unittest.main()
