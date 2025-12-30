import unittest
import sys
import os

# Add parent directory to path to import src module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src import binary_search


class TestBinarySearch(unittest.TestCase):
    """Test cases for binary search algorithm."""
    
    def test_element_found_middle(self):
        """Test finding element in the middle of array."""
        arr = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(binary_search(arr, 4), 3)
    
    def test_element_found_beginning(self):
        """Test finding element at the beginning of array."""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(arr, 1), 0)
    
    def test_element_found_end(self):
        """Test finding element at the end of array."""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(arr, 5), 4)
    
    def test_element_not_found(self):
        """Test searching for element not in array."""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(binary_search(arr, 10), -1)
    
    def test_empty_array(self):
        """Test searching in empty array."""
        arr = []
        self.assertEqual(binary_search(arr, 5), -1)
    
    def test_single_element_found(self):
        """Test finding element in single-element array."""
        arr = [5]
        self.assertEqual(binary_search(arr, 5), 0)
    
    def test_single_element_not_found(self):
        """Test not finding element in single-element array."""
        arr = [5]
        self.assertEqual(binary_search(arr, 3), -1)
    
    def test_two_elements(self):
        """Test searching in two-element array."""
        arr = [1, 2]
        self.assertEqual(binary_search(arr, 1), 0)
        self.assertEqual(binary_search(arr, 2), 1)
        self.assertEqual(binary_search(arr, 3), -1)
    
    def test_negative_numbers(self):
        """Test searching with negative numbers."""
        arr = [-10, -5, 0, 5, 10]
        self.assertEqual(binary_search(arr, -5), 1)
        self.assertEqual(binary_search(arr, 0), 2)
    
    def test_large_array(self):
        """Test searching in large array."""
        arr = list(range(0, 10000, 2))  # Even numbers 0-9998
        self.assertEqual(binary_search(arr, 5000), 2500)
        self.assertEqual(binary_search(arr, 5001), -1)


if __name__ == '__main__':
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestBinarySearch)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Write test result to file
    import os
    os.makedirs('../replay', exist_ok=True)
    with open('../replay/test_bool.txt', 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')
