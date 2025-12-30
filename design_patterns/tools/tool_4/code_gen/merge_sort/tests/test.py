import unittest
import os
import sys

from src.merge_sort import merge_sort, merge


class TestMergeSort(unittest.TestCase):
    """Test cases for merge sort algorithm implementation."""
    
    def test_empty_array(self):
        """Test sorting an empty array."""
        self.assertEqual(merge_sort([]), [])
    
    def test_single_element(self):
        """Test sorting an array with a single element."""
        self.assertEqual(merge_sort([5]), [5])
    
    def test_two_elements_sorted(self):
        """Test sorting an array with two already sorted elements."""
        self.assertEqual(merge_sort([1, 2]), [1, 2])
    
    def test_two_elements_unsorted(self):
        """Test sorting an array with two unsorted elements."""
        self.assertEqual(merge_sort([2, 1]), [1, 2])
    
    def test_multiple_elements(self):
        """Test sorting an array with multiple elements."""
        self.assertEqual(merge_sort([64, 34, 25, 12, 22, 11, 90]), [11, 12, 22, 25, 34, 64, 90])
    
    def test_already_sorted(self):
        """Test sorting an already sorted array."""
        self.assertEqual(merge_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
    
    def test_reverse_sorted(self):
        """Test sorting a reverse sorted array."""
        self.assertEqual(merge_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
    
    def test_duplicate_elements(self):
        """Test sorting an array with duplicate elements."""
        self.assertEqual(merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])
    
    def test_negative_numbers(self):
        """Test sorting an array with negative numbers."""
        self.assertEqual(merge_sort([-5, 3, -2, 8, -1, 0]), [-5, -2, -1, 0, 3, 8])
    
    def test_all_same_elements(self):
        """Test sorting an array where all elements are the same."""
        self.assertEqual(merge_sort([7, 7, 7, 7]), [7, 7, 7, 7])
    
    def test_original_unchanged(self):
        """Test that the original array is not modified."""
        original = [3, 1, 4, 1, 5]
        original_copy = original.copy()
        merge_sort(original)
        self.assertEqual(original, original_copy)
    
    def test_merge_function(self):
        """Test the merge helper function directly."""
        self.assertEqual(merge([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(merge([], [1, 2, 3]), [1, 2, 3])
        self.assertEqual(merge([1, 2, 3], []), [1, 2, 3])
        self.assertEqual(merge([], []), [])


if __name__ == '__main__':
    # Create replay directory if it doesn't exist
    os.makedirs('../replay', exist_ok=True)
    
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestMergeSort)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Write test result to file
    with open('../replay/test_bool.txt', 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')