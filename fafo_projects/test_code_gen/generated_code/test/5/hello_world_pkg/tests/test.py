"""
Test file for the hello_world package.
"""

from hello_world import greet, say_goodbye


def test_greet():
    """Test greet function."""
    print("Testing greet()...")
    greet()
    print("✓ greet() test passed")


def test_say_goodbye():
    """Test say_goodbye function."""
    print("Testing say_goodbye()...")
    say_goodbye()
    print("✓ say_goodbye() test passed")


if __name__ == "__main__":
    print("Running tests...\n")
    
    test_greet()
    test_say_goodbye()
    
    print("\nAll tests passed!")
