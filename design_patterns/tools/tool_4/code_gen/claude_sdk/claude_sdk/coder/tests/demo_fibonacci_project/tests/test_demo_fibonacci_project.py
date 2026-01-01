"""Tests for demo_fibonacci_project module."""
import unittest
import sys
from pathlib import Path

# Add the src directory to the path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from demo_fibonacci_project import fibonacci, fibonacci_sequence


class TestFibonacci(unittest.TestCase):
    """Test cases for Fibonacci functions."""
    
    def test_fibonacci_zero(self):
        """Test fibonacci(0) returns 0."""
        self.assertEqual(fibonacci(0), 0)
    
    def test_fibonacci_one(self):
        """Test fibonacci(1) returns 1."""
        self.assertEqual(fibonacci(1), 1)
    
    def test_fibonacci_ten(self):
        """Test fibonacci(10) returns 55."""
        self.assertEqual(fibonacci(10), 55)
    
    def test_fibonacci_negative(self):
        """Test fibonacci raises error for negative input."""
        with self.assertRaises(ValueError):
            fibonacci(-1)
    
    def test_fibonacci_sequence(self):
        """Test fibonacci_sequence returns correct list."""
        self.assertEqual(fibonacci_sequence(7), [0, 1, 1, 2, 3, 5, 8])
    
    def test_fibonacci_sequence_empty(self):
        """Test fibonacci_sequence(0) returns empty list."""
        self.assertEqual(fibonacci_sequence(0), [])


if __name__ == '__main__':
    unittest.main()
