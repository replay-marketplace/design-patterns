"""
Test file for the hello_world package.
"""

from hello_world import greet, say_goodbye


def test_greet():
    """Test greet function."""
    result = greet()
    assert result == "Hello, World!"
    print("✓ test_greet passed")
    
    result = greet("Alice")
    assert result == "Hello, Alice!"
    print("✓ test_greet with name passed")


def test_say_goodbye():
    """Test say_goodbye function."""
    result = say_goodbye()
    assert result == "Goodbye, World!"
    print("✓ test_say_goodbye passed")
    
    result = say_goodbye("Bob")
    assert result == "Goodbye, Bob!"
    print("✓ test_say_goodbye with name passed")


if __name__ == "__main__":
    print("Running tests...\n")
    
    test_greet()
    test_say_goodbye()
    
    print("\nAll tests passed!")
