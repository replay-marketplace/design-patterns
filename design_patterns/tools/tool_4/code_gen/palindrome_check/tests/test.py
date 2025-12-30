import unittest
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.palindrome import is_palindrome


class TestPalindrome(unittest.TestCase):
    """Test cases for palindrome checker function."""
    
    def test_simple_palindrome(self):
        """Test simple palindrome words."""
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome("radar"))
    
    def test_single_character(self):
        """Test single character strings are palindromes."""
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("Z"))
    
    def test_empty_string(self):
        """Test empty string is a palindrome."""
        self.assertTrue(is_palindrome(""))
    
    def test_not_palindrome(self):
        """Test strings that are not palindromes."""
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))
        self.assertFalse(is_palindrome("python"))
    
    def test_case_insensitive(self):
        """Test that palindrome check is case insensitive."""
        self.assertTrue(is_palindrome("RaceCar"))
        self.assertTrue(is_palindrome("Level"))
        self.assertTrue(is_palindrome("MadAm"))
    
    def test_with_spaces_and_punctuation(self):
        """Test palindromes with spaces and punctuation."""
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))
        self.assertTrue(is_palindrome("No 'x' in Nixon"))
    
    def test_numeric_palindrome(self):
        """Test numeric string palindromes."""
        self.assertTrue(is_palindrome("12321"))
        self.assertTrue(is_palindrome("11211"))
        self.assertFalse(is_palindrome("12345"))
    
    def test_two_characters(self):
        """Test two character strings."""
        self.assertTrue(is_palindrome("aa"))
        self.assertTrue(is_palindrome("AA"))
        self.assertFalse(is_palindrome("ab"))


if __name__ == '__main__':
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestPalindrome)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Write test result to file
    with open('../replay/test_bool.txt', 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')
