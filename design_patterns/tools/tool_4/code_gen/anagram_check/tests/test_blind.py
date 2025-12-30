import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from solution import are_anagrams

class TestAreAnagrams(unittest.TestCase):
    """Test cases for are_anagrams function."""
    
    def test_simple_anagrams(self):
        """Test simple anagram pairs."""
        self.assertTrue(are_anagrams("listen", "silent"))
        self.assertTrue(are_anagrams("evil", "vile"))
        self.assertTrue(are_anagrams("dusty", "study"))
    
    def test_not_anagrams(self):
        """Test strings that are not anagrams."""
        self.assertFalse(are_anagrams("hello", "world"))
        self.assertFalse(are_anagrams("abc", "def"))
        self.assertFalse(are_anagrams("test", "testing"))
    
    def test_case_insensitive(self):
        """Test that comparison is case-insensitive."""
        self.assertTrue(are_anagrams("Listen", "Silent"))
        self.assertTrue(are_anagrams("EVIL", "vile"))
        self.assertTrue(are_anagrams("Dusty", "STUDY"))
    
    def test_ignores_spaces(self):
        """Test that spaces are ignored."""
        self.assertTrue(are_anagrams("a gentleman", "elegant man"))
        self.assertTrue(are_anagrams("the eyes", "they see"))
        self.assertTrue(are_anagrams("slot machines", "cash lost in me"))
    
    def test_empty_strings(self):
        """Test empty strings."""
        self.assertTrue(are_anagrams("", ""))
        self.assertTrue(are_anagrams("   ", ""))
    
    def test_single_characters(self):
        """Test single character strings."""
        self.assertTrue(are_anagrams("a", "a"))
        self.assertTrue(are_anagrams("A", "a"))
        self.assertFalse(are_anagrams("a", "b"))
    
    def test_different_lengths_after_removing_spaces(self):
        """Test strings with different character counts."""
        self.assertFalse(are_anagrams("abc", "abcd"))
        self.assertFalse(are_anagrams("aab", "abb"))
    
    def test_same_string(self):
        """Test identical strings."""
        self.assertTrue(are_anagrams("test", "test"))
        self.assertTrue(are_anagrams("hello world", "hello world"))

if __name__ == '__main__':
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestAreAnagrams)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Write test result to file
    with open('../replay/test_blind_bool.txt', 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')
