import unittest
from src.word_counter import count_words


class TestWordCounter(unittest.TestCase):
    """Test cases for the count_words function."""
    
    def test_simple_sentence(self):
        """Test counting words in a simple sentence."""
        self.assertEqual(count_words("hello world"), 2)
    
    def test_empty_string(self):
        """Test counting words in an empty string."""
        self.assertEqual(count_words(""), 0)
    
    def test_whitespace_only(self):
        """Test counting words in a string with only whitespace."""
        self.assertEqual(count_words("   "), 0)
    
    def test_single_word(self):
        """Test counting a single word."""
        self.assertEqual(count_words("hello"), 1)
    
    def test_multiple_spaces(self):
        """Test counting words with multiple spaces between them."""
        self.assertEqual(count_words("hello    world   test"), 3)
    
    def test_leading_trailing_spaces(self):
        """Test counting words with leading and trailing spaces."""
        self.assertEqual(count_words("  hello world  "), 2)
    
    def test_newlines_and_tabs(self):
        """Test counting words separated by newlines and tabs."""
        self.assertEqual(count_words("hello\nworld\ttest"), 3)
    
    def test_long_sentence(self):
        """Test counting words in a longer sentence."""
        self.assertEqual(count_words("The quick brown fox jumps over the lazy dog"), 9)


if __name__ == '__main__':
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestWordCounter)
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
