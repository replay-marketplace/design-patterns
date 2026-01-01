import unittest
import os
import tempfile
import shutil
import json
from unittest.mock import patch, MagicMock

import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from coder_platform.coder_platform.src.project_generator import generate_project


class TestGenerateProject(unittest.TestCase):
    """Test cases for the generate_project function."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.test_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        """Clean up test fixtures."""
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
    
    @patch('coder_platform.coder_platform.src.project_generator.coder')
    @patch('coder_platform.coder_platform.src.project_generator.store_files_into_dir')
    def test_generate_project_with_valid_prompt(self, mock_store, mock_coder):
        """Test generate_project with a valid prompt."""
        mock_coder.return_value = json.dumps({
            "files": [
                {"path": "main.py", "content": "print('Hello')"}
            ]
        })
        mock_store.return_value = self.test_dir
        
        result = generate_project("Create a hello world program", self.test_dir)
        
        self.assertEqual(result, self.test_dir)
        mock_coder.assert_called_once_with("Create a hello world program")
        mock_store.assert_called_once()
    
    @patch('coder_platform.coder_platform.src.project_generator.coder')
    @patch('coder_platform.coder_platform.src.project_generator.store_files_into_dir')
    def test_generate_project_without_output_dir(self, mock_store, mock_coder):
        """Test generate_project creates temp directory when none provided."""
        mock_coder.return_value = json.dumps({"files": []})
        temp_path = tempfile.mkdtemp(prefix="generated_project_")
        mock_store.return_value = temp_path
        
        result = generate_project("Create a project")
        
        self.assertTrue(result.startswith(tempfile.gettempdir()) or os.path.isabs(result))
        mock_coder.assert_called_once()
        
        # Cleanup
        if os.path.exists(temp_path):
            shutil.rmtree(temp_path)
    
    def test_generate_project_with_empty_prompt(self):
        """Test generate_project raises error with empty prompt."""
        with self.assertRaises(ValueError):
            generate_project("")
    
    def test_generate_project_with_whitespace_prompt(self):
        """Test generate_project raises error with whitespace-only prompt."""
        with self.assertRaises(ValueError):
            generate_project("   ")
    
    @patch('coder_platform.coder_platform.src.project_generator.coder')
    @patch('coder_platform.coder_platform.src.project_generator.store_files_into_dir')
    def test_generate_project_creates_output_dir(self, mock_store, mock_coder):
        """Test generate_project creates output directory if it doesn't exist."""
        mock_coder.return_value = json.dumps({"files": []})
        new_dir = os.path.join(self.test_dir, "new_subdir")
        mock_store.return_value = new_dir
        
        result = generate_project("Create a project", new_dir)
        
        self.assertTrue(os.path.exists(new_dir))


if __name__ == '__main__':
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestGenerateProject)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Write test result to file
    os.makedirs('../replay', exist_ok=True)
    with open('../replay/test_bool.txt', 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')
