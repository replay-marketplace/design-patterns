import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from solution import quick_sort, quick_sort_inplace, partition


class TestQuickSort(unittest.TestCase):
    """Test cases for quick sort algorithm functions."""
    
    def test_quick_sort_empty_list(self):
        """Test quick_sort with empty list."""
        result = quick_sort([])
        self.assertEqual(result, [])
    
    def test_quick_sort_single_element(self):
        """Test quick_sort with single element."""
        result = quick_sort([5])
        self.assertEqual(result, [5])
    
    def test_quick_sort_sorted_list(self):
        """Test quick_sort with already sorted list."""
        result = quick_sort([1, 2, 3, 4, 5])
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_quick_sort_reverse_sorted(self):
        """Test quick_sort with reverse sorted list."""
        result = quick_sort([5, 4, 3, 2, 1])
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_quick_sort_unsorted_list(self):
        """Test quick_sort with unsorted list."""
        result = quick_sort([3, 1, 4, 1, 5, 9, 2, 6])
        self.assertEqual(result, [1, 1, 2, 3, 4, 5, 6, 9])
    
    def test_quick_sort_duplicates(self):
        """Test quick_sort with duplicate elements."""
        result = quick_sort([3, 3, 3, 1, 1, 2, 2])
        self.assertEqual(result, [1, 1, 2, 2, 3, 3, 3])
    
    def test_quick_sort_negative_numbers(self):
        """Test quick_sort with negative numbers."""
        result = quick_sort([-3, 1, -4, 1, 5, -9, 2])
        self.assertEqual(result, [-9, -4, -3, 1, 1, 2, 5])
    
    def test_quick_sort_returns_new_list(self):
        """Test that quick_sort returns a new list."""
        original = [3, 1, 2]
        result = quick_sort(original)
        self.assertEqual(result, [1, 2, 3])
        self.assertEqual(original, [3, 1, 2])  # Original unchanged
    
    def test_quick_sort_inplace_empty_list(self):
        """Test quick_sort_inplace with empty list."""
        arr = []
        quick_sort_inplace(arr)
        self.assertEqual(arr, [])
    
    def test_quick_sort_inplace_single_element(self):
        """Test quick_sort_inplace with single element."""
        arr = [5]
        quick_sort_inplace(arr)
        self.assertEqual(arr, [5])
    
    def test_quick_sort_inplace_unsorted_list(self):
        """Test quick_sort_inplace with unsorted list."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        quick_sort_inplace(arr)
        self.assertEqual(arr, [1, 1, 2, 3, 4, 5, 6, 9])
    
    def test_quick_sort_inplace_reverse_sorted(self):
        """Test quick_sort_inplace with reverse sorted list."""
        arr = [5, 4, 3, 2, 1]
        quick_sort_inplace(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])
    
    def test_quick_sort_inplace_with_bounds(self):
        """Test quick_sort_inplace with explicit low and high bounds."""
        arr = [5, 3, 1, 4, 2]
        quick_sort_inplace(arr, 1, 3)
        self.assertEqual(arr[1:4], [1, 3, 4])
    
    def test_quick_sort_inplace_returns_none(self):
        """Test that quick_sort_inplace returns None."""
        arr = [3, 1, 2]
        result = quick_sort_inplace(arr)
        self.assertIsNone(result)
    
    def test_partition_basic(self):
        """Test partition function returns valid pivot index."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        pivot_idx = partition(arr, 0, len(arr) - 1)
        self.assertGreaterEqual(pivot_idx, 0)
        self.assertLess(pivot_idx, len(arr))
    
    def test_partition_elements_arranged(self):
        """Test partition arranges elements correctly around pivot."""
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        pivot_idx = partition(arr, 0, len(arr) - 1)
        pivot_value = arr[pivot_idx]
        for i in range(pivot_idx):
            self.assertLessEqual(arr[i], pivot_value)
        for i in range(pivot_idx + 1, len(arr)):
            self.assertGreaterEqual(arr[i], pivot_value)
    
    def test_partition_two_elements(self):
        """Test partition with two elements."""
        arr = [2, 1]
        pivot_idx = partition(arr, 0, 1)
        self.assertIn(pivot_idx, [0, 1])


if __name__ == '__main__':
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestQuickSort)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Write test result to file
    os.makedirs('../replay', exist_ok=True)
    with open('../replay/test_blind_bool.txt', 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')
