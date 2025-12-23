"""
Test file for the hello_world package.
"""

from hello_world import say_hello, say_world


def test_say_hello():
    """Test say_hello function."""
    print("Testing say_hello...")
    say_hello()
    print("say_hello test passed!")


def test_say_world():
    """Test say_world function."""
    print("Testing say_world...")
    say_world()
    print("say_world test passed!")


if __name__ == "__main__":
    print("Running tests...\n")
    
    test_say_hello()
    test_say_world()
    
    print("\nAll tests passed!")
