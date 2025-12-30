import unittest
import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.merge_sort import merge_sort, merge


class TestMergeSort(unittest.TestCase):
    """Test cases for merge_sort and merge functions."""
    
    def test_merge_sort_empty_list(self):
        """Test merge_sort with an empty list."""
        result = merge_sort([])
        self.assertEqual(result, [])
    
    def test_merge_sort_single_element(self):
        """Test merge_sort with a single element list."""
        result = merge_sort([5])
        self.assertEqual(result, [5])
    
    def test_merge_sort_two_elements(self):
        """Test merge_sort with two elements."""
        result = merge_sort([3, 1])
        self.assertEqual(result, [1, 3])
    
    def test_merge_sort_already_sorted(self):
        """Test merge_sort with an already sorted list."""
        result = merge_sort([1, 2, 3, 4, 5])
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_merge_sort_reverse_sorted(self):
        """Test merge_sort with a reverse sorted list."""
        result = merge_sort([5, 4, 3, 2, 1])
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_merge_sort_unsorted_list(self):
        """Test merge_sort with an unsorted list."""
        result = merge_sort([3, 1, 4, 1, 5, 9, 2, 6])
        self.assertEqual(result, [1, 1, 2, 3, 4, 5, 6, 9])
    
    def test_merge_sort_with_duplicates(self):
        """Test merge_sort with duplicate elements."""
        result = merge_sort([5, 2, 5, 2, 5, 2])
        self.assertEqual(result, [2, 2, 2, 5, 5, 5])
    
    def test_merge_sort_negative_numbers(self):
        """Test merge_sort with negative numbers."""
        result = merge_sort([-3, -1, -4, -1, -5])
        self.assertEqual(result, [-5, -4, -3, -1, -1])
    
    def test_merge_sort_mixed_numbers(self):
        """Test merge_sort with mixed positive and negative numbers."""
        result = merge_sort([3, -1, 4, -1, 5, -9, 2, -6])
        self.assertEqual(result, [-9, -6, -1, -1, 2, 3, 4, 5])
    
    def test_merge_sort_returns_new_list(self):
        """Test that merge_sort returns a new list and doesn't modify original."""
        original = [3, 1, 2]
        result = merge_sort(original)
        self.assertEqual(result, [1, 2, 3])
        self.assertEqual(original, [3, 1, 2])  # Original should be unchanged
    
    def test_merge_empty_lists(self):
        """Test merge with two empty lists."""
        result = merge([], [])
        self.assertEqual(result, [])
    
    def test_merge_one_empty_list(self):
        """Test merge with one empty list."""
        result = merge([1, 2, 3], [])
        self.assertEqual(result, [1, 2, 3])
        result = merge([], [1, 2, 3])
        self.assertEqual(result, [1, 2, 3])
    
    def test_merge_two_sorted_lists(self):
        """Test merge with two sorted lists."""
        result = merge([1, 3, 5], [2, 4, 6])
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])
    
    def test_merge_overlapping_ranges(self):
        """Test merge with overlapping value ranges."""
        result = merge([1, 2, 3], [2, 3, 4])
        self.assertEqual(result, [1, 2, 2, 3, 3, 4])
    
    def test_merge_different_lengths(self):
        """Test merge with lists of different lengths."""
        result = merge([1, 5], [2, 3, 4, 6, 7])
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7])


if __name__ == '__main__':
    # Create replay directory if it doesn't exist
    os.makedirs('../replay', exist_ok=True)
    
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestMergeSort)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Write test result to file
    with open('../replay/test_blind_bool.txt', 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')
