import unittest
import sys
import os

# Add parent directory to path to import src module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

# Import the binary_search function from the src module
from src.binary_search import binary_search


class TestBinarySearch(unittest.TestCase):
    """Test cases for binary_search function."""
    
    def test_target_found_in_middle(self):
        """Test finding target in the middle of array."""
        arr = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(binary_search(arr, 4), 3)
    
    def test_target_found_at_beginning(self):
        """Test finding target at the beginning of array."""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(arr, 1), 0)
    
    def test_target_found_at_end(self):
        """Test finding target at the end of array."""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(arr, 5), 4)
    
    def test_target_not_found(self):
        """Test when target is not in array."""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(arr, 10), -1)
    
    def test_empty_array(self):
        """Test with empty array."""
        arr = []
        self.assertEqual(binary_search(arr, 5), -1)
    
    def test_single_element_found(self):
        """Test with single element array where target is found."""
        arr = [5]
        self.assertEqual(binary_search(arr, 5), 0)
    
    def test_single_element_not_found(self):
        """Test with single element array where target is not found."""
        arr = [5]
        self.assertEqual(binary_search(arr, 3), -1)
    
    def test_two_elements_found_first(self):
        """Test with two elements, target is first."""
        arr = [1, 2]
        self.assertEqual(binary_search(arr, 1), 0)
    
    def test_two_elements_found_second(self):
        """Test with two elements, target is second."""
        arr = [1, 2]
        self.assertEqual(binary_search(arr, 2), 1)
    
    def test_negative_numbers(self):
        """Test with negative numbers in array."""
        arr = [-10, -5, 0, 5, 10]
        self.assertEqual(binary_search(arr, -5), 1)
    
    def test_target_smaller_than_all(self):
        """Test when target is smaller than all elements."""
        arr = [10, 20, 30, 40, 50]
        self.assertEqual(binary_search(arr, 5), -1)
    
    def test_target_larger_than_all(self):
        """Test when target is larger than all elements."""
        arr = [10, 20, 30, 40, 50]
        self.assertEqual(binary_search(arr, 100), -1)


if __name__ == '__main__':
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestBinarySearch)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Ensure replay directory exists
    replay_dir = os.path.join(os.path.dirname(__file__), '..', 'replay')
    os.makedirs(replay_dir, exist_ok=True)
    
    # Write test result to file
    with open(os.path.join(replay_dir, 'test_blind_bool.txt'), 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')
