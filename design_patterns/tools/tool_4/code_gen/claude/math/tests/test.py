import unittest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.add import add
from src.sub import sub
from src.mult import mult
from src.div import div


class TestMathOperations(unittest.TestCase):
    """Test cases for basic math operations."""

    def test_add(self):
        """Test addition operation."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_sub(self):
        """Test subtraction operation."""
        self.assertEqual(sub(5, 3), 2)
        self.assertEqual(sub(1, 1), 0)
        self.assertEqual(sub(0, 5), -5)

    def test_mult(self):
        """Test multiplication operation."""
        self.assertEqual(mult(2, 3), 6)
        self.assertEqual(mult(-2, 3), -6)
        self.assertEqual(mult(0, 5), 0)

    def test_div(self):
        """Test division operation."""
        self.assertEqual(div(6, 2), 3)
        self.assertEqual(div(7, 2), 3)
        self.assertEqual(div(-6, 2), -3)

    def test_div_by_zero(self):
        """Test division by zero raises error."""
        with self.assertRaises(ValueError):
            div(5, 0)


if __name__ == '__main__':
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestMathOperations)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Ensure replay directory exists
    os.makedirs('../replay', exist_ok=True)

    # Write test result to file
    with open('../replay/test_bool.txt', 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')
