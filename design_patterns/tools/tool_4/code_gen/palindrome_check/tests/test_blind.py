import unittest
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the function to test
from solution import is_palindrome

class TestIsPalindrome(unittest.TestCase):
    """Test cases for is_palindrome function."""
    
    def test_simple_palindrome(self):
        """Test simple palindrome string."""
        self.assertTrue(is_palindrome("racecar"))
    
    def test_simple_non_palindrome(self):
        """Test simple non-palindrome string."""
        self.assertFalse(is_palindrome("hello"))
    
    def test_single_character(self):
        """Test single character is a palindrome."""
        self.assertTrue(is_palindrome("a"))
    
    def test_empty_string(self):
        """Test empty string is a palindrome."""
        self.assertTrue(is_palindrome(""))
    
    def test_two_same_characters(self):
        """Test two same characters is a palindrome."""
        self.assertTrue(is_palindrome("aa"))
    
    def test_two_different_characters(self):
        """Test two different characters is not a palindrome."""
        self.assertFalse(is_palindrome("ab"))
    
    def test_palindrome_with_spaces(self):
        """Test palindrome with spaces (exact match)."""
        self.assertTrue(is_palindrome("a a"))
    
    def test_longer_palindrome(self):
        """Test longer palindrome string."""
        self.assertTrue(is_palindrome("madam"))
    
    def test_even_length_palindrome(self):
        """Test even length palindrome."""
        self.assertTrue(is_palindrome("abba"))
    
    def test_even_length_non_palindrome(self):
        """Test even length non-palindrome."""
        self.assertFalse(is_palindrome("abcd"))

if __name__ == '__main__':
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestIsPalindrome)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Write test result to file
    with open('../replay/test_blind_bool.txt', 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')
