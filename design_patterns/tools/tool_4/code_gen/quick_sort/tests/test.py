import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.quick_sort import quick_sort, quick_sort_inplace, partition


class TestQuickSort(unittest.TestCase):
    """Test cases for quick sort algorithm implementation."""
    
    def test_empty_array(self):
        """Test sorting an empty array."""
        self.assertEqual(quick_sort([]), [])
    
    def test_single_element(self):
        """Test sorting an array with single element."""
        self.assertEqual(quick_sort([5]), [5])
    
    def test_two_elements_sorted(self):
        """Test sorting an already sorted two-element array."""
        self.assertEqual(quick_sort([1, 2]), [1, 2])
    
    def test_two_elements_unsorted(self):
        """Test sorting an unsorted two-element array."""
        self.assertEqual(quick_sort([2, 1]), [1, 2])
    
    def test_multiple_elements(self):
        """Test sorting an array with multiple elements."""
        self.assertEqual(quick_sort([64, 34, 25, 12, 22, 11, 90]), [11, 12, 22, 25, 34, 64, 90])
    
    def test_already_sorted(self):
        """Test sorting an already sorted array."""
        self.assertEqual(quick_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
    
    def test_reverse_sorted(self):
        """Test sorting a reverse sorted array."""
        self.assertEqual(quick_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
    
    def test_duplicates(self):
        """Test sorting an array with duplicate elements."""
        self.assertEqual(quick_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]), [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9])
    
    def test_negative_numbers(self):
        """Test sorting an array with negative numbers."""
        self.assertEqual(quick_sort([-5, 3, -2, 0, 7, -1]), [-5, -2, -1, 0, 3, 7])
    
    def test_all_same_elements(self):
        """Test sorting an array where all elements are the same."""
        self.assertEqual(quick_sort([5, 5, 5, 5, 5]), [5, 5, 5, 5, 5])
    
    def test_original_unchanged(self):
        """Test that quick_sort does not modify the original array."""
        original = [3, 1, 4, 1, 5]
        original_copy = original.copy()
        quick_sort(original)
        self.assertEqual(original, original_copy)
    
    def test_inplace_sort(self):
        """Test in-place quick sort."""
        arr = [64, 34, 25, 12, 22, 11, 90]
        quick_sort_inplace(arr)
        self.assertEqual(arr, [11, 12, 22, 25, 34, 64, 90])
    
    def test_partition(self):
        """Test partition function returns correct pivot index."""
        arr = [10, 80, 30, 90, 40, 50, 70]
        pivot_idx = partition(arr, 0, len(arr) - 1)
        # After partition, all elements before pivot_idx should be <= arr[pivot_idx]
        # and all elements after should be > arr[pivot_idx]
        for i in range(pivot_idx):
            self.assertLessEqual(arr[i], arr[pivot_idx])
        for i in range(pivot_idx + 1, len(arr)):
            self.assertGreater(arr[i], arr[pivot_idx])
    
    def test_large_array(self):
        """Test sorting a larger array."""
        import random
        arr = list(range(100))
        random.shuffle(arr)
        self.assertEqual(quick_sort(arr), list(range(100)))


if __name__ == '__main__':
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestQuickSort)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Write test result to file
    os.makedirs('../replay', exist_ok=True)
    with open('../replay/test_bool.txt', 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')