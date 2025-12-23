"""
Test file for the hello_world package.
"""

from hello_world import greet, say_goodbye


def test_greet():
    """Test greet function."""
    result = greet("Alice")
    assert result == "Hello, Alice!", f"Expected 'Hello, Alice!' but got '{result}'"
    
    result_default = greet()
    assert result_default == "Hello, World!", f"Expected 'Hello, World!' but got '{result_default}'"
    
    print("✓ test_greet passed")


def test_say_goodbye():
    """Test say_goodbye function."""
    result = say_goodbye("Bob")
    assert result == "Goodbye, Bob!", f"Expected 'Goodbye, Bob!' but got '{result}'"
    
    result_default = say_goodbye()
    assert result_default == "Goodbye, World!", f"Expected 'Goodbye, World!' but got '{result_default}'"
    
    print("✓ test_say_goodbye passed")


if __name__ == "__main__":
    print("Running tests...\n")
    
    test_greet()
    test_say_goodbye()
    
    print("\nAll tests passed!")

