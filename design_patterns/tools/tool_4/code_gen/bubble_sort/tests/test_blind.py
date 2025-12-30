import unittest
from main import bubble_sort

class TestBubbleSort(unittest.TestCase):
    """Test cases for bubble_sort function."""
    
    def test_empty_list(self):
        """Test sorting an empty list."""
        result = bubble_sort([])
        self.assertEqual(result, [])
    
    def test_single_element(self):
        """Test sorting a list with a single element."""
        result = bubble_sort([5])
        self.assertEqual(result, [5])
    
    def test_already_sorted(self):
        """Test sorting an already sorted list."""
        result = bubble_sort([1, 2, 3, 4, 5])
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_reverse_sorted(self):
        """Test sorting a reverse sorted list."""
        result = bubble_sort([5, 4, 3, 2, 1])
        self.assertEqual(result, [1, 2, 3, 4, 5])
    
    def test_unsorted_list(self):
        """Test sorting an unsorted list."""
        result = bubble_sort([3, 1, 4, 1, 5, 9, 2, 6])
        self.assertEqual(result, [1, 1, 2, 3, 4, 5, 6, 9])
    
    def test_duplicate_elements(self):
        """Test sorting a list with duplicate elements."""
        result = bubble_sort([3, 3, 3, 1, 1, 2, 2])
        self.assertEqual(result, [1, 1, 2, 2, 3, 3, 3])
    
    def test_negative_numbers(self):
        """Test sorting a list with negative numbers."""
        result = bubble_sort([-3, -1, -4, -1, -5])
        self.assertEqual(result, [-5, -4, -3, -1, -1])
    
    def test_mixed_positive_negative(self):
        """Test sorting a list with mixed positive and negative numbers."""
        result = bubble_sort([3, -1, 4, -1, 5, -9, 2, -6])
        self.assertEqual(result, [-9, -6, -1, -1, 2, 3, 4, 5])
    
    def test_returns_new_list(self):
        """Test that bubble_sort returns a new list and doesn't modify the original."""
        original = [3, 1, 2]
        result = bubble_sort(original)
        self.assertEqual(result, [1, 2, 3])
        # Check that original list is unchanged
        self.assertEqual(original, [3, 1, 2])
    
    def test_two_elements(self):
        """Test sorting a list with two elements."""
        result = bubble_sort([2, 1])
        self.assertEqual(result, [1, 2])

if __name__ == '__main__':
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestBubbleSort)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Write test result to file
    with open('../replay/test_blind_bool.txt', 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')
