import unittest
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the function to test
from src.merge_sorted import merge_sorted_arrays

class TestMergeSortedArrays(unittest.TestCase):
    """Test cases for merge_sorted_arrays function."""
    
    def test_basic_merge(self):
        """Test basic merge of two sorted arrays."""
        result = merge_sorted_arrays([1, 3, 5], [2, 4, 6])
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])
    
    def test_empty_first_array(self):
        """Test merge when first array is empty."""
        result = merge_sorted_arrays([], [1, 2, 3])
        self.assertEqual(result, [1, 2, 3])
    
    def test_empty_second_array(self):
        """Test merge when second array is empty."""
        result = merge_sorted_arrays([1, 2, 3], [])
        self.assertEqual(result, [1, 2, 3])
    
    def test_both_empty_arrays(self):
        """Test merge when both arrays are empty."""
        result = merge_sorted_arrays([], [])
        self.assertEqual(result, [])
    
    def test_single_element_arrays(self):
        """Test merge of single element arrays."""
        result = merge_sorted_arrays([1], [2])
        self.assertEqual(result, [1, 2])
    
    def test_duplicate_elements(self):
        """Test merge with duplicate elements."""
        result = merge_sorted_arrays([1, 2, 3], [2, 3, 4])
        self.assertEqual(result, [1, 2, 2, 3, 3, 4])
    
    def test_negative_numbers(self):
        """Test merge with negative numbers."""
        result = merge_sorted_arrays([-5, -3, -1], [-4, -2, 0])
        self.assertEqual(result, [-5, -4, -3, -2, -1, 0])
    
    def test_different_length_arrays(self):
        """Test merge of arrays with different lengths."""
        result = merge_sorted_arrays([1, 5], [2, 3, 4, 6, 7])
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7])
    
    def test_all_elements_from_first_smaller(self):
        """Test when all elements from first array are smaller."""
        result = merge_sorted_arrays([1, 2, 3], [4, 5, 6])
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])
    
    def test_all_elements_from_second_smaller(self):
        """Test when all elements from second array are smaller."""
        result = merge_sorted_arrays([4, 5, 6], [1, 2, 3])
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])

if __name__ == '__main__':
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestMergeSortedArrays)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Ensure replay directory exists
    os.makedirs('../replay', exist_ok=True)
    
    # Write test result to file
    with open('../replay/test_blind_bool.txt', 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')
