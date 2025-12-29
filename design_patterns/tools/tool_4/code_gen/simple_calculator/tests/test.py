import unittest
from src.calculator import add


class TestCalculator(unittest.TestCase):
    """Test cases for the calculator add function."""
    
    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        self.assertEqual(add(2, 3), 5)
    
    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        self.assertEqual(add(-2, -3), -5)
    
    def test_add_mixed_numbers(self):
        """Test adding a positive and negative number."""
        self.assertEqual(add(-2, 3), 1)
    
    def test_add_zeros(self):
        """Test adding zeros."""
        self.assertEqual(add(0, 0), 0)
    
    def test_add_floats(self):
        """Test adding floating point numbers."""
        self.assertAlmostEqual(add(1.5, 2.5), 4.0)


if __name__ == '__main__':
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestCalculator)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Write test result to file
    with open('../replay/test_bool.txt', 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')
