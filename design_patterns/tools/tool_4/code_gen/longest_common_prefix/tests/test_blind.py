import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from blind import longest_common_prefix

class TestLongestCommonPrefix(unittest.TestCase):
    """Test cases for longest_common_prefix function."""
    
    def test_common_prefix_exists(self):
        """Test when there is a common prefix among all strings."""
        strs = ["flower", "flow", "flight"]
        self.assertEqual(longest_common_prefix(strs), "fl")
    
    def test_no_common_prefix(self):
        """Test when there is no common prefix."""
        strs = ["dog", "racecar", "car"]
        self.assertEqual(longest_common_prefix(strs), "")
    
    def test_empty_list(self):
        """Test with an empty list of strings."""
        strs = []
        self.assertEqual(longest_common_prefix(strs), "")
    
    def test_single_string(self):
        """Test with a single string in the list."""
        strs = ["alone"]
        self.assertEqual(longest_common_prefix(strs), "alone")
    
    def test_all_same_strings(self):
        """Test when all strings are identical."""
        strs = ["test", "test", "test"]
        self.assertEqual(longest_common_prefix(strs), "test")
    
    def test_empty_string_in_list(self):
        """Test when one of the strings is empty."""
        strs = ["abc", "", "ab"]
        self.assertEqual(longest_common_prefix(strs), "")
    
    def test_all_empty_strings(self):
        """Test when all strings are empty."""
        strs = ["", "", ""]
        self.assertEqual(longest_common_prefix(strs), "")
    
    def test_single_character_prefix(self):
        """Test when common prefix is a single character."""
        strs = ["apple", "ape", "april"]
        self.assertEqual(longest_common_prefix(strs), "ap")
    
    def test_full_string_is_prefix(self):
        """Test when one string is a prefix of others."""
        strs = ["ab", "abc", "abcd"]
        self.assertEqual(longest_common_prefix(strs), "ab")
    
    def test_two_strings(self):
        """Test with exactly two strings."""
        strs = ["interview", "internet"]
        self.assertEqual(longest_common_prefix(strs), "inter")

if __name__ == '__main__':
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestLongestCommonPrefix)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Write test result to file
    os.makedirs('../replay', exist_ok=True)
    with open('../replay/test_blind_bool.txt', 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')
