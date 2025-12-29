
import unittest
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from app import create_app, index, api_status, api_stats

class TestFlaskHackerWebsite(unittest.TestCase):
    """Test cases for Flask Hacker Website API."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
    
    def test_create_app_returns_flask_instance(self):
        """Test that create_app returns a Flask application instance."""
        from flask import Flask
        app = create_app()
        self.assertIsInstance(app, Flask)
    
    def test_index_returns_string(self):
        """Test that index route returns HTML string."""
        with self.app.app_context():
            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertIsInstance(response.data.decode('utf-8'), str)
    
    def test_api_status_returns_dict(self):
        """Test that api_status returns JSON dict."""
        with self.app.app_context():
            response = self.client.get('/api/status')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, 'application/json')
            data = response.get_json()
            self.assertIsInstance(data, dict)
    
    def test_api_stats_returns_dict(self):
        """Test that api_stats returns JSON dict with fake hacker stats."""
        with self.app.app_context():
            response = self.client.get('/api/stats')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, 'application/json')
            data = response.get_json()
            self.assertIsInstance(data, dict)

if __name__ == '__main__':
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestFlaskHackerWebsite)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Write test result to file
    os.makedirs(os.path.join(os.path.dirname(__file__), '..', 'replay'), exist_ok=True)
    with open(os.path.join(os.path.dirname(__file__), '..', 'replay', 'test_blind_bool.txt'), 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')
