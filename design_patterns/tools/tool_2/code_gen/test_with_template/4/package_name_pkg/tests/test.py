# Test file

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from package_name import greet

def test_greet():
    """Test the greet function"""
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Bob") == "Hello, Bob!"
    assert greet("") == "Hello, !"
    print("All tests passed!")

if __name__ == "__main__":
    test_greet()

