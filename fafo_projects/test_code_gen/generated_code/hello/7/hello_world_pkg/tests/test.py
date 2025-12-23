# Test file for hello world functions
import sys
import os

# Add parent directory to path to import the package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from hello_world import hello, goodbye, see_ya_later


def test_hello():
    """Test the hello function"""
    result = hello()
    assert result == "Hello, World!"
    assert isinstance(result, str)


def test_goodbye():
    """Test the goodbye function"""
    result = goodbye()
    assert result == "Goodbye!"
    assert isinstance(result, str)


def test_see_ya_later():
    """Test the see_ya_later function"""
    result = see_ya_later()
    assert result == "See ya later!"
    assert isinstance(result, str)
