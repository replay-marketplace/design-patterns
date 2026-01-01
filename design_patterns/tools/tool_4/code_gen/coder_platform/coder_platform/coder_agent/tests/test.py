import unittest
import json
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

from coder_platform.coder_agent.src.coder import coder


class TestCoderAgent(unittest.TestCase):
    """Test cases for the coder agent function."""
    
    def test_coder_returns_string(self):
        """Test that coder returns a string."""
        result = coder("Create a simple hello world program")
        self.assertIsInstance(result, str)
    
    def test_coder_returns_valid_json(self):
        """Test that coder returns valid JSON."""
        result = coder("Create a function that adds two numbers")
        try:
            parsed = json.loads(result)
            self.assertIsInstance(parsed, list)
        except json.JSONDecodeError:
            self.fail("coder() did not return valid JSON")
    
    def test_coder_json_structure(self):
        """Test that the JSON has correct structure with path and contents."""
        result = coder("Create a simple calculator class")
        parsed = json.loads(result)
        self.assertIsInstance(parsed, list)
        self.assertGreater(len(parsed), 0)
        for item in parsed:
            self.assertIn('path', item)
            self.assertIn('contents', item)
            self.assertIsInstance(item['path'], str)
            self.assertIsInstance(item['contents'], str)
    
    def test_coder_includes_main_file(self):
        """Test that the response includes a main code file."""
        result = coder("Create a fibonacci function")
        parsed = json.loads(result)
        paths = [item['path'] for item in parsed]
        has_code_file = any(p.endswith('.py') for p in paths)
        self.assertTrue(has_code_file, "Response should include at least one .py file")


if __name__ == '__main__':
    # Create replay directory if it doesn't exist
    os.makedirs(os.path.join(os.path.dirname(__file__), '..', 'replay'), exist_ok=True)
    
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestCoderAgent)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Write test result to file
    with open(os.path.join(os.path.dirname(__file__), '..', 'replay', 'test_bool.txt'), 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')
