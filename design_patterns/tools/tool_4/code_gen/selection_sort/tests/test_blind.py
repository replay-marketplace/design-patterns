import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from selection_sort import selection_sort

class TestSelectionSort(unittest.TestCase):
    """Test cases for selection_sort function."""
    
    def test_empty_array(self):
        """Test sorting an empty array."""
        self.assertEqual(selection_sort([]), [])
    
    def test_single_element(self):
        """Test sorting an array with a single element."""
        self.assertEqual(selection_sort([5]), [5])
    
    def test_already_sorted(self):
        """Test sorting an already sorted array."""
        self.assertEqual(selection_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
    
    def test_reverse_sorted(self):
        """Test sorting a reverse sorted array."""
        self.assertEqual(selection_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
    
    def test_unsorted_array(self):
        """Test sorting an unsorted array."""
        self.assertEqual(selection_sort([3, 1, 4, 1, 5, 9, 2, 6]), [1, 1, 2, 3, 4, 5, 6, 9])
    
    def test_duplicate_elements(self):
        """Test sorting an array with duplicate elements."""
        self.assertEqual(selection_sort([3, 3, 3, 1, 1, 2]), [1, 1, 2, 3, 3, 3])
    
    def test_negative_numbers(self):
        """Test sorting an array with negative numbers."""
        self.assertEqual(selection_sort([-3, -1, -4, -1, -5]), [-5, -4, -3, -1, -1])
    
    def test_mixed_positive_negative(self):
        """Test sorting an array with mixed positive and negative numbers."""
        self.assertEqual(selection_sort([3, -1, 4, -1, 5, -9, 2, -6]), [-9, -6, -1, -1, 2, 3, 4, 5])
    
    def test_two_elements(self):
        """Test sorting an array with two elements."""
        self.assertEqual(selection_sort([2, 1]), [1, 2])
    
    def test_returns_list(self):
        """Test that the function returns a list."""
        result = selection_sort([3, 1, 2])
        self.assertIsInstance(result, list)

if __name__ == '__main__':
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestSelectionSort)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Write test result to file
    with open('../replay/test_blind_bool.txt', 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')
