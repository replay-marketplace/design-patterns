
import unittest
from main import add

class TestAddFunction(unittest.TestCase):
    """Test cases for the add function."""
    
    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        result = add(2.0, 3.0)
        self.assertEqual(result, 5.0)
    
    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        result = add(-2.0, -3.0)
        self.assertEqual(result, -5.0)
    
    def test_add_mixed_numbers(self):
        """Test adding a positive and negative number."""
        result = add(5.0, -3.0)
        self.assertEqual(result, 2.0)
    
    def test_add_zero(self):
        """Test adding zero to a number."""
        result = add(5.0, 0.0)
        self.assertEqual(result, 5.0)
    
    def test_add_floats(self):
        """Test adding floating point numbers."""
        result = add(1.5, 2.5)
        self.assertEqual(result, 4.0)
    
    def test_add_returns_float(self):
        """Test that add returns a float."""
        result = add(1.0, 2.0)
        self.assertIsInstance(result, float)

if __name__ == '__main__':
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestAddFunction)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Write test result to file
    with open('../replay/test_blind_bool.txt', 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')
