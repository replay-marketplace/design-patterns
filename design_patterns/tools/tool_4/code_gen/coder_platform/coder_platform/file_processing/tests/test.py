import unittest
import os
import shutil
import tempfile
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.file_manager import store_files_into_dir, load_files_from_dir


class TestFileManager(unittest.TestCase):
    """Test cases for file storage and loading functionality."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.test_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        """Clean up test fixtures."""
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
    
    def test_store_files_into_dir_creates_directory(self):
        """Test that store_files_into_dir creates the directory if it doesn't exist."""
        new_dir = os.path.join(self.test_dir, 'new_subdir')
        content = "Test content"
        
        result = store_files_into_dir(content, new_dir)
        
        self.assertTrue(os.path.exists(new_dir))
        self.assertTrue(os.path.isfile(result))
    
    def test_store_files_into_dir_returns_valid_path(self):
        """Test that store_files_into_dir returns a valid file path."""
        content = "Hello, World!"
        
        result = store_files_into_dir(content, self.test_dir)
        
        self.assertTrue(os.path.exists(result))
        self.assertTrue(result.startswith(self.test_dir))
    
    def test_store_files_into_dir_stores_content_correctly(self):
        """Test that the stored file contains the correct content."""
        content = "This is test content\nWith multiple lines"
        
        result = store_files_into_dir(content, self.test_dir)
        
        with open(result, 'r', encoding='utf-8') as f:
            stored_content = f.read()
        
        self.assertEqual(stored_content, content)
    
    def test_store_files_into_dir_creates_unique_files(self):
        """Test that multiple calls create unique files."""
        content1 = "Content 1"
        content2 = "Content 2"
        
        result1 = store_files_into_dir(content1, self.test_dir)
        result2 = store_files_into_dir(content2, self.test_dir)
        
        self.assertNotEqual(result1, result2)
        self.assertTrue(os.path.exists(result1))
        self.assertTrue(os.path.exists(result2))
    
    def test_load_files_from_dir_returns_list(self):
        """Test that load_files_from_dir returns a list."""
        result = load_files_from_dir(self.test_dir)
        
        self.assertIsInstance(result, list)
    
    def test_load_files_from_dir_empty_directory(self):
        """Test loading from an empty directory returns empty list."""
        result = load_files_from_dir(self.test_dir)
        
        self.assertEqual(result, [])
    
    def test_load_files_from_dir_nonexistent_directory(self):
        """Test loading from a nonexistent directory returns empty list."""
        result = load_files_from_dir('/nonexistent/path/12345')
        
        self.assertEqual(result, [])
    
    def test_load_files_from_dir_returns_correct_structure(self):
        """Test that loaded files have correct dictionary structure."""
        content = "Test content"
        store_files_into_dir(content, self.test_dir)
        
        result = load_files_from_dir(self.test_dir)
        
        self.assertEqual(len(result), 1)
        self.assertIn('filename', result[0])
        self.assertIn('content', result[0])
    
    def test_load_files_from_dir_returns_correct_content(self):
        """Test that loaded files contain the correct content."""
        content = "Expected content here"
        store_files_into_dir(content, self.test_dir)
        
        result = load_files_from_dir(self.test_dir)
        
        self.assertEqual(result[0]['content'], content)
    
    def test_store_and_load_multiple_files(self):
        """Test storing and loading multiple files."""
        contents = ["Content A", "Content B", "Content C"]
        
        for content in contents:
            store_files_into_dir(content, self.test_dir)
        
        result = load_files_from_dir(self.test_dir)
        
        self.assertEqual(len(result), 3)
        loaded_contents = [f['content'] for f in result]
        for content in contents:
            self.assertIn(content, loaded_contents)
    
    def test_store_empty_content(self):
        """Test storing empty content."""
        content = ""
        
        result = store_files_into_dir(content, self.test_dir)
        
        self.assertTrue(os.path.exists(result))
        with open(result, 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), "")
    
    def test_store_unicode_content(self):
        """Test storing unicode content."""
        content = "Hello 世界 🌍 émojis"
        
        result = store_files_into_dir(content, self.test_dir)
        
        loaded = load_files_from_dir(self.test_dir)
        self.assertEqual(loaded[0]['content'], content)


if __name__ == '__main__':
    # Create replay directory if it doesn't exist
    replay_dir = os.path.join(os.path.dirname(__file__), '..', 'replay')
    os.makedirs(replay_dir, exist_ok=True)
    
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestFileManager)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Write test result to file
    with open(os.path.join(replay_dir, 'test_bool.txt'), 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')