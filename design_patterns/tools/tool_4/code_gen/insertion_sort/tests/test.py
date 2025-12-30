import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from src.insertion_sort import insertion_sort


class TestInsertionSort(unittest.TestCase):
    """Test cases for insertion sort algorithm."""
    
    def test_empty_array(self):
        """Test sorting an empty array."""
        self.assertEqual(insertion_sort([]), [])
    
    def test_single_element(self):
        """Test sorting an array with a single element."""
        self.assertEqual(insertion_sort([5]), [5])
    
    def test_already_sorted(self):
        """Test sorting an already sorted array."""
        self.assertEqual(insertion_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
    
    def test_reverse_sorted(self):
        """Test sorting a reverse sorted array."""
        self.assertEqual(insertion_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
    
    def test_unsorted_array(self):
        """Test sorting an unsorted array."""
        self.assertEqual(insertion_sort([3, 1, 4, 1, 5, 9, 2, 6]), [1, 1, 2, 3, 4, 5, 6, 9])
    
    def test_negative_numbers(self):
        """Test sorting an array with negative numbers."""
        self.assertEqual(insertion_sort([-3, 1, -4, 1, 5, -9]), [-9, -4, -3, 1, 1, 5])
    
    def test_duplicate_elements(self):
        """Test sorting an array with duplicate elements."""
        self.assertEqual(insertion_sort([3, 3, 3, 1, 1, 2]), [1, 1, 2, 3, 3, 3])
    
    def test_two_elements(self):
        """Test sorting an array with two elements."""
        self.assertEqual(insertion_sort([2, 1]), [1, 2])
    
    def test_original_unchanged(self):
        """Test that the original array is not modified."""
        original = [3, 1, 2]
        insertion_sort(original)
        self.assertEqual(original, [3, 1, 2])


if __name__ == '__main__':
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestInsertionSort)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Write test result to file
    with open('../replay/test_bool.txt', 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')
