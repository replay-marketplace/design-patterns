import unittest
from src.two_sum import two_sum

class TestTwoSum(unittest.TestCase):
    """Test cases for two_sum function."""
    
    def test_example_case(self):
        """Test the example from documentation."""
        result = two_sum([2, 7, 11, 15], 9)
        self.assertEqual(result, [0, 1])
    
    def test_target_at_end(self):
        """Test when target numbers are at the end of the list."""
        result = two_sum([1, 2, 3, 4, 5], 9)
        self.assertEqual(result, [3, 4])
    
    def test_negative_numbers(self):
        """Test with negative numbers in the list."""
        result = two_sum([-1, -2, -3, -4, -5], -8)
        self.assertEqual(result, [2, 4])
    
    def test_mixed_positive_negative(self):
        """Test with mixed positive and negative numbers."""
        result = two_sum([-3, 4, 3, 90], 0)
        self.assertEqual(result, [0, 2])
    
    def test_no_solution(self):
        """Test when no solution exists."""
        result = two_sum([1, 2, 3], 100)
        self.assertEqual(result, [])
    
    def test_two_elements(self):
        """Test with only two elements."""
        result = two_sum([3, 3], 6)
        self.assertEqual(result, [0, 1])
    
    def test_zero_target(self):
        """Test with zero as target."""
        result = two_sum([0, 4, 3, 0], 0)
        self.assertEqual(result, [0, 3])
    
    def test_large_numbers(self):
        """Test with large numbers."""
        result = two_sum([1000000, 500000, 500000], 1000000)
        self.assertEqual(result, [1, 2])

if __name__ == '__main__':
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestTwoSum)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Write test result to file
    with open('../replay/test_blind_bool.txt', 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')
