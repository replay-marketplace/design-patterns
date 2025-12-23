"""
Test file for the hello_world package.
"""

from hello_world import say_hello, greet_user


def test_say_hello():
    """Test say_hello function."""
    result = say_hello()
    assert result == "Hello, World!", f"Expected 'Hello, World!' but got '{result}'"
    print("✓ test_say_hello passed")


def test_greet_user():
    """Test greet_user function."""
    result = greet_user("Alice")
    assert result == "Hello, Alice!", f"Expected 'Hello, Alice!' but got '{result}'"
    
    result = greet_user("Bob")
    assert result == "Hello, Bob!", f"Expected 'Hello, Bob!' but got '{result}'"
    print("✓ test_greet_user passed")


if __name__ == "__main__":
    print("Running tests...\n")
    
    test_say_hello()
    test_greet_user()
    
    print("\nAll tests passed!")

