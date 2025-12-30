import unittest
from src.linear_search import linear_search


class TestLinearSearch(unittest.TestCase):
    """Test cases for linear search algorithm."""
    
    def test_element_found_at_beginning(self):
        """Test finding element at the beginning of array."""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(linear_search(arr, 1), 0)
    
    def test_element_found_at_end(self):
        """Test finding element at the end of array."""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(linear_search(arr, 5), 4)
    
    def test_element_found_in_middle(self):
        """Test finding element in the middle of array."""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(linear_search(arr, 3), 2)
    
    def test_element_not_found(self):
        """Test when element is not in array."""
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(linear_search(arr, 10), -1)
    
    def test_empty_array(self):
        """Test search in empty array."""
        arr = []
        self.assertEqual(linear_search(arr, 1), -1)
    
    def test_single_element_found(self):
        """Test search in single element array where element exists."""
        arr = [42]
        self.assertEqual(linear_search(arr, 42), 0)
    
    def test_single_element_not_found(self):
        """Test search in single element array where element doesn't exist."""
        arr = [42]
        self.assertEqual(linear_search(arr, 10), -1)
    
    def test_duplicate_elements(self):
        """Test that first occurrence is returned for duplicates."""
        arr = [1, 2, 3, 2, 4]
        self.assertEqual(linear_search(arr, 2), 1)
    
    def test_string_elements(self):
        """Test search with string elements."""
        arr = ['apple', 'banana', 'cherry']
        self.assertEqual(linear_search(arr, 'banana'), 1)
    
    def test_negative_numbers(self):
        """Test search with negative numbers."""
        arr = [-5, -3, -1, 0, 2, 4]
        self.assertEqual(linear_search(arr, -3), 1)


if __name__ == '__main__':
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestLinearSearch)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Write test result to file
    with open('../replay/test_bool.txt', 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')
