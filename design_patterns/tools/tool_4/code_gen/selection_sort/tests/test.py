import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from src.selection_sort import selection_sort


class TestSelectionSort(unittest.TestCase):
    """Test cases for selection sort algorithm."""
    
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
    
    def test_random_order(self):
        """Test sorting an array in random order."""
        self.assertEqual(selection_sort([64, 34, 25, 12, 22, 11, 90]), [11, 12, 22, 25, 34, 64, 90])
    
    def test_with_duplicates(self):
        """Test sorting an array with duplicate elements."""
        self.assertEqual(selection_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]), [1, 1, 2, 3, 4, 5, 5, 6, 9])
    
    def test_negative_numbers(self):
        """Test sorting an array with negative numbers."""
        self.assertEqual(selection_sort([-5, 3, -2, 0, 7, -1]), [-5, -2, -1, 0, 3, 7])
    
    def test_all_same_elements(self):
        """Test sorting an array where all elements are the same."""
        self.assertEqual(selection_sort([7, 7, 7, 7]), [7, 7, 7, 7])
    
    def test_two_elements(self):
        """Test sorting an array with two elements."""
        self.assertEqual(selection_sort([2, 1]), [1, 2])
    
    def test_original_unchanged(self):
        """Test that the original array is not modified."""
        original = [3, 1, 2]
        selection_sort(original)
        self.assertEqual(original, [3, 1, 2])


if __name__ == '__main__':
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestSelectionSort)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Write test result to file
    with open('../replay/test_bool.txt', 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')
