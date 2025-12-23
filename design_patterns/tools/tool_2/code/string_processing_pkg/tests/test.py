"""Tests for string_processing package."""

import os
import sys

# Add parent directory to path to import package
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from string_processing import (
    append_string,
    search_and_delete,
    search_and_replace,
    strip_markdown
)


def test_append_string():
    """Test append_string function."""
    print("Testing append_string...")
    
    try:
        result = append_string("Hello", " World")
        assert result == "Hello World"
        print("✓ append_string test passed")
        
        # Test with empty strings
        result = append_string("", "test")
        assert result == "test"
        
        result = append_string("test", "")
        assert result == "test"
        
        print("✓ append_string edge cases passed")
    except Exception as e:
        print(f"✗ append_string test failed: {e}")


def test_search_and_delete():
    """Test search_and_delete function."""
    print("\nTesting search_and_delete...")
    
    try:
        result = search_and_delete("Hello World Hello", "Hello")
        assert result == " World "
        print("✓ search_and_delete test passed")
        
        # Test with no matches
        result = search_and_delete("Hello World", "Python")
        assert result == "Hello World"
        
        # Test with empty pattern
        result = search_and_delete("Hello World", "")
        assert result == "Hello World"
        
        print("✓ search_and_delete edge cases passed")
    except Exception as e:
        print(f"✗ search_and_delete test failed: {e}")


def test_search_and_replace():
    """Test search_and_replace function."""
    print("\nTesting search_and_replace...")
    
    try:
        result = search_and_replace("Hello World", "World", "Python")
        assert result == "Hello Python"
        print("✓ search_and_replace test passed")
        
        # Test with multiple occurrences
        result = search_and_replace("Hello World Hello", "Hello", "Hi")
        assert result == "Hi World Hi"
        
        # Test with no matches
        result = search_and_replace("Hello World", "Python", "Java")
        assert result == "Hello World"
        
        print("✓ search_and_replace edge cases passed")
    except Exception as e:
        print(f"✗ search_and_replace test failed: {e}")


def test_strip_markdown():
    """Test strip_markdown function."""
    print("\nTesting strip_markdown...")
    
    try:
        # Test headers
        result = strip_markdown("# Hello World")
        assert "Hello World" in result
        assert "#" not in result
        
        # Test bold
        result = strip_markdown("Hello **World**")
        assert "Hello World" in result
        assert "**" not in result
        
        # Test italic
        result = strip_markdown("Hello *World*")
        assert "Hello World" in result
        assert "*" not in result or result.count("*") == 0
        
        # Test code blocks
        result = strip_markdown("Hello ```code``` World")
        assert "code" not in result or "```" not in result
        
        # Test links
        result = strip_markdown("Hello [World](https://example.com)")
        assert "Hello World" in result
        assert "https://example.com" not in result
        
        print("✓ strip_markdown test passed")
    except Exception as e:
        print(f"✗ strip_markdown test failed: {e}")


if __name__ == "__main__":
    test_append_string()
    test_search_and_delete()
    test_search_and_replace()
    test_strip_markdown()
    print("\nAll tests completed!")


