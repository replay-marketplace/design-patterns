import unittest
from src.two_sum import two_sum


class TestTwoSum(unittest.TestCase):
    """Test cases for two_sum function that finds two numbers adding to target."""
    
    def test_basic_case(self):
        """Test basic case with solution at beginning of array."""
        result = two_sum([2, 7, 11, 15], 9)
        self.assertEqual(result, [0, 1])
    
    def test_solution_at_end(self):
        """Test case where solution is at the end of array."""
        result = two_sum([1, 2, 3, 4, 5], 9)
        self.assertEqual(result, [3, 4])
    
    def test_negative_numbers(self):
        """Test case with negative numbers."""
        result = two_sum([-1, -2, -3, -4, -5], -8)
        self.assertEqual(result, [2, 4])
    
    def test_mixed_positive_negative(self):
        """Test case with mixed positive and negative numbers."""
        result = two_sum([-3, 4, 3, 90], 0)
        self.assertEqual(result, [0, 2])
    
    def test_zero_target(self):
        """Test case where target is zero."""
        result = two_sum([0, 4, 3, 0], 0)
        self.assertEqual(result, [0, 3])
    
    def test_no_solution(self):
        """Test case where no solution exists."""
        result = two_sum([1, 2, 3], 10)
        self.assertEqual(result, [])
    
    def test_two_elements(self):
        """Test case with only two elements."""
        result = two_sum([3, 3], 6)
        self.assertEqual(result, [0, 1])
    
    def test_large_numbers(self):
        """Test case with large numbers."""
        result = two_sum([1000000, 500000, 500000], 1000000)
        self.assertEqual(result, [1, 2])


if __name__ == '__main__':
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestTwoSum)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Write test result to file
    with open('../replay/test_bool.txt', 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')