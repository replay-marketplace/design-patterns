"""
Test file for the hello_world package.
"""

from hello_world import print_hello_world, get_hello_world


def test_print_hello_world():
    """Test print_hello_world function."""
    print("Testing print_hello_world...")
    print_hello_world()
    print("✓ print_hello_world test passed")


def test_get_hello_world():
    """Test get_hello_world function."""
    print("Testing get_hello_world...")
    result = get_hello_world()
    assert result == "Hello, World!", f"Expected 'Hello, World!' but got '{result}'"
    print(f"✓ get_hello_world test passed: {result}")


if __name__ == "__main__":
    print("Running tests...\n")
    
    test_print_hello_world()
    test_get_hello_world()
    
    print("\nAll tests passed!")

