import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from simple_function import greet, add_numbers


def test_greet():
    """Test the greet function."""
    assert greet("Alice") == "Hello, Alice!"
    assert greet("") == "Hello, !"
    print("✓ test_greet passed")


def test_add_numbers():
    """Test the add_numbers function."""
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
    print("✓ test_add_numbers passed")


if __name__ == "__main__":
    test_greet()
    test_add_numbers()
    print("All tests passed!")