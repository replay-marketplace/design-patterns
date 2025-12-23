# Test file

import sys
sys.path.insert(0, '../package_name')

from greet import greet

def test_greet():
    """Test the greet function."""
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Bob") == "Hello, Bob!"
    assert greet("") == "Hello, !"
    print("All tests passed!")

if __name__ == "__main__":
    test_greet()

