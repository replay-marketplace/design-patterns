import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.app import create_app


class TestFlaskApp(unittest.TestCase):
    """Test cases for the Flask hacker website application."""
    
    def setUp(self):
        """Set up test client before each test."""
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
    
    def test_index_returns_200(self):
        """Test that the index page returns a 200 status code."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_index_contains_title(self):
        """Test that the index page contains the expected title."""
        response = self.client.get('/')
        self.assertIn(b'NEXUS', response.data)
    
    def test_index_contains_html_structure(self):
        """Test that the index page contains proper HTML structure."""
        response = self.client.get('/')
        self.assertIn(b'<!DOCTYPE html>', response.data)
        self.assertIn(b'</html>', response.data)
    
    def test_api_status_returns_200(self):
        """Test that the status API returns a 200 status code."""
        response = self.client.get('/api/status')
        self.assertEqual(response.status_code, 200)
    
    def test_api_status_returns_json(self):
        """Test that the status API returns valid JSON."""
        response = self.client.get('/api/status')
        self.assertEqual(response.content_type, 'application/json')
    
    def test_api_status_contains_required_fields(self):
        """Test that the status API contains required fields."""
        response = self.client.get('/api/status')
        data = response.get_json()
        self.assertIn('status', data)
        self.assertIn('uptime', data)
        self.assertIn('timestamp', data)
        self.assertEqual(data['status'], 'operational')
    
    def test_api_stats_returns_200(self):
        """Test that the stats API returns a 200 status code."""
        response = self.client.get('/api/stats')
        self.assertEqual(response.status_code, 200)
    
    def test_api_stats_returns_json(self):
        """Test that the stats API returns valid JSON."""
        response = self.client.get('/api/stats')
        self.assertEqual(response.content_type, 'application/json')
    
    def test_api_stats_contains_required_fields(self):
        """Test that the stats API contains required fields."""
        response = self.client.get('/api/stats')
        data = response.get_json()
        self.assertIn('nodes_online', data)
        self.assertIn('requests_per_second', data)
        self.assertIn('latency_ms', data)
        self.assertIn('encryption_bits', data)
    
    def test_create_app_returns_flask_instance(self):
        """Test that create_app returns a Flask application instance."""
        from flask import Flask
        app = create_app()
        self.assertIsInstance(app, Flask)


if __name__ == '__main__':
    # Create test suite and run tests
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestFlaskApp)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Ensure replay directory exists
    os.makedirs('../replay', exist_ok=True)
    
    # Write test result to file
    with open('../replay/test_bool.txt', 'w') as f:
        if result.wasSuccessful():
            f.write('PASSED')
        else:
            f.write('FAILED')