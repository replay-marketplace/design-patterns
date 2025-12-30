import unittest
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.word_counter import count_words

class TestCountWords(unittest.TestCase):
    """Test cases for count_words function."""
    
    def test_simple_sentence(self):
        """Test counting words in a simple sentence."""
        self.assertEqual(count_words("hello world"), 2)
    
    def test_empty_string(self):
        """Test counting words in an empty string."""
        self.assertEqual(count_words(""), 0)
    
    def test_single_word(self):
        """Test counting a single word."""
        self.assertEqual(count_words("hello"), 1)
    
    def test_multiple_spaces(self):
        """Test counting words with multiple spaces between them."""
        self.assertEqual(count_words("hello    world"), 2)
    
    def test_leading_trailing_spaces(self):
        """Test counting words with leading and trailing spaces."""
        self.assertEqual(count_words("  hello world  "), 2)
    
    def test_tabs_and_newlines(self):
        """Test counting words separated by tabs and newlines."""
        self.assertEqual(count_words("hello\tworld\nfoo"), 3)
    
    def test_only_whitespace(self):
        """Test counting words in a string with only whitespace."""
        self.assertEqual(count_words("   \t\n  "), 0)
    
    def test_longer_sentence(self):
        """Test counting words in a longer sentence."""
        self.assertEqual(count_words("The quick brown fox jumps over the lazy dog"), 9)

if __name__ == '__main__':
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestCountWords)
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
