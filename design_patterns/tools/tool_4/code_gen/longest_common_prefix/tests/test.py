import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from src import longest_common_prefix


class TestLongestCommonPrefix(unittest.TestCase):
    """Test cases for longest_common_prefix function."""
    
    def test_common_prefix_exists(self):
        """Test when there is a common prefix among strings."""
        result = longest_common_prefix(["flower", "flow", "flight"])
        self.assertEqual(result, "fl")
    
    def test_no_common_prefix(self):
        """Test when there is no common prefix."""
        result = longest_common_prefix(["dog", "racecar", "car"])
        self.assertEqual(result, "")
    
    def test_empty_list(self):
        """Test with an empty list."""
        result = longest_common_prefix([])
        self.assertEqual(result, "")
    
    def test_single_string(self):
        """Test with a single string in the list."""
        result = longest_common_prefix(["alone"])
        self.assertEqual(result, "alone")
    
    def test_identical_strings(self):
        """Test when all strings are identical."""
        result = longest_common_prefix(["test", "test", "test"])
        self.assertEqual(result, "test")
    
    def test_empty_string_in_list(self):
        """Test when one of the strings is empty."""
        result = longest_common_prefix(["abc", "", "ab"])
        self.assertEqual(result, "")
    
    def test_all_empty_strings(self):
        """Test when all strings are empty."""
        result = longest_common_prefix(["", "", ""])
        self.assertEqual(result, "")
    
    def test_single_character_prefix(self):
        """Test when common prefix is a single character."""
        result = longest_common_prefix(["apple", "ape", "april"])
        self.assertEqual(result, "ap")
    
    def test_full_string_is_prefix(self):
        """Test when one string is a prefix of others."""
        result = longest_common_prefix(["ab", "abc", "abcd"])
        self.assertEqual(result, "ab")
    
    def test_two_strings(self):
        """Test with exactly two strings."""
        result = longest_common_prefix(["interview", "internet"])
        self.assertEqual(result, "inter")


if __name__ == '__main__':
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestLongestCommonPrefix)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Write test result to file
    import os
    os.makedirs('../replay', exist_ok=True)
    with open('../replay/test_bool.txt', 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')
