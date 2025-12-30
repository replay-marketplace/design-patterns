import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from solution import reverse_string

class TestReverseString(unittest.TestCase):
    """Test cases for reverse_string function."""
    
    def test_simple_string(self):
        """Test reversing a simple string."""
        self.assertEqual(reverse_string("hello"), "olleh")
    
    def test_empty_string(self):
        """Test reversing an empty string."""
        self.assertEqual(reverse_string(""), "")
    
    def test_single_character(self):
        """Test reversing a single character string."""
        self.assertEqual(reverse_string("a"), "a")
    
    def test_palindrome(self):
        """Test reversing a palindrome."""
        self.assertEqual(reverse_string("racecar"), "racecar")
    
    def test_string_with_spaces(self):
        """Test reversing a string with spaces."""
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")
    
    def test_string_with_numbers(self):
        """Test reversing a string containing numbers."""
        self.assertEqual(reverse_string("abc123"), "321cba")
    
    def test_string_with_special_characters(self):
        """Test reversing a string with special characters."""
        self.assertEqual(reverse_string("!@#$%"), "%$#@!")

if __name__ == '__main__':
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestReverseString)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Write test result to file
    import os
    os.makedirs('../replay', exist_ok=True)
    with open('../replay/test_blind_bool.txt', 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')
