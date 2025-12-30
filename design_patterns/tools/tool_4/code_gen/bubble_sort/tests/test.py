import unittest
from src.bubble_sort import bubble_sort


class TestBubbleSort(unittest.TestCase):
    """Test cases for bubble sort algorithm."""
    
    def test_empty_array(self):
        """Test sorting an empty array."""
        self.assertEqual(bubble_sort([]), [])
    
    def test_single_element(self):
        """Test sorting an array with single element."""
        self.assertEqual(bubble_sort([5]), [5])
    
    def test_already_sorted(self):
        """Test sorting an already sorted array."""
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
    
    def test_reverse_sorted(self):
        """Test sorting a reverse sorted array."""
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
    
    def test_unsorted_array(self):
        """Test sorting an unsorted array."""
        self.assertEqual(bubble_sort([64, 34, 25, 12, 22, 11, 90]), [11, 12, 22, 25, 34, 64, 90])
    
    def test_duplicate_elements(self):
        """Test sorting an array with duplicate elements."""
        self.assertEqual(bubble_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]), [1, 1, 2, 3, 4, 5, 5, 6, 9])
    
    def test_negative_numbers(self):
        """Test sorting an array with negative numbers."""
        self.assertEqual(bubble_sort([-5, 3, -2, 0, 7, -1]), [-5, -2, -1, 0, 3, 7])
    
    def test_original_unchanged(self):
        """Test that original array is not modified."""
        original = [3, 1, 2]
        bubble_sort(original)
        self.assertEqual(original, [3, 1, 2])


if __name__ == '__main__':
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestBubbleSort)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Write test result to file
    with open('../replay/test_bool.txt', 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')
