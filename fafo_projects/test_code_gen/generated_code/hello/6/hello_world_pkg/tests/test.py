"""
Test file for the hello_world package.
"""

from hello_world import hello, goodbye, see_ya_later


def test_hello():
    """Test hello function."""
    result = hello()
    print(f"hello() returned: {result}")
    assert result == "Hello, World!"
    print("✓ test_hello passed")


def test_goodbye():
    """Test goodbye function."""
    result = goodbye()
    print(f"goodbye() returned: {result}")
    assert result == "Goodbye, World!"
    print("✓ test_goodbye passed")


def test_see_ya_later():
    """Test see_ya_later function."""
    result = see_ya_later()
    print(f"see_ya_later() returned: {result}")
    assert result == "See ya later, World!"
    print("✓ test_see_ya_later passed")


if __name__ == "__main__":
    print("Running tests...\n")
    
    test_hello()
    test_goodbye()
    test_see_ya_later()
    
    print("\nAll tests passed!")

