"""
Test file for the string_processing package.
"""

from string_processing import (
    append_string,
    search_and_delete,
    search_and_replace,
    strip_markdown,
    count_tokens
)


def test_append_string():
    """Test append_string function."""
    print("Testing append_string...")
    result = append_string("Hello", " World")
    assert result == "Hello World", f"Expected 'Hello World', got '{result}'"
    
    result = append_string("", "Test")
    assert result == "Test", f"Expected 'Test', got '{result}'"
    
    result = append_string("Test", "")
    assert result == "Test", f"Expected 'Test', got '{result}'"
    
    print("  ✓ append_string tests passed")


def test_search_and_delete():
    """Test search_and_delete function."""
    print("Testing search_and_delete...")
    result = search_and_delete("Hello World", "World")
    assert result == "Hello ", f"Expected 'Hello ', got '{result}'"
    
    result = search_and_delete("test test test", "test")
    assert result == "  ", f"Expected '  ', got '{result}'"
    
    result = search_and_delete("Hello World", "xyz")
    assert result == "Hello World", f"Expected 'Hello World', got '{result}'"
    
    print("  ✓ search_and_delete tests passed")


def test_search_and_replace():
    """Test search_and_replace function."""
    print("Testing search_and_replace...")
    result = search_and_replace("Hello World", "World", "Python")
    assert result == "Hello Python", f"Expected 'Hello Python', got '{result}'"
    
    result = search_and_replace("test test test", "test", "demo")
    assert result == "demo demo demo", f"Expected 'demo demo demo', got '{result}'"
    
    result = search_and_replace("Hello World", "xyz", "abc")
    assert result == "Hello World", f"Expected 'Hello World', got '{result}'"
    
    print("  ✓ search_and_replace tests passed")


def test_strip_markdown():
    """Test strip_markdown function."""
    print("Testing strip_markdown...")
    
    # Test headers
    result = strip_markdown("# Header 1")
    assert result == "Header 1", f"Expected 'Header 1', got '{result}'"
    
    result = strip_markdown("## Header 2")
    assert result == "Header 2", f"Expected 'Header 2', got '{result}'"
    
    # Test bold
    result = strip_markdown("**bold text**")
    assert result == "bold text", f"Expected 'bold text', got '{result}'"
    
    # Test italic
    result = strip_markdown("*italic text*")
    assert result == "italic text", f"Expected 'italic text', got '{result}'"
    
    # Test links
    result = strip_markdown("[link text](http://example.com)")
    assert result == "link text", f"Expected 'link text', got '{result}'"
    
    # Test code
    result = strip_markdown("`code`")
    assert result == "code", f"Expected 'code', got '{result}'"
    
    # Test complex markdown
    result = strip_markdown("# Title\n\n**Bold** and *italic* with [link](url)")
    assert "Title" in result and "Bold" in result and "italic" in result and "link" in result
    
    print("  ✓ strip_markdown tests passed")


def test_count_tokens():
    """Test count_tokens function."""
    print("Testing count_tokens...")
    
    result = count_tokens("Hello World")
    assert result > 0, f"Expected positive token count, got {result}"
    
    result = count_tokens("")
    assert result == 0, f"Expected 0 tokens for empty string, got {result}"
    
    # Longer text should have more tokens
    short_text = "Hello"
    long_text = "Hello World, this is a longer text with many more words"
    short_count = count_tokens(short_text)
    long_count = count_tokens(long_text)
    assert long_count > short_count, f"Expected longer text to have more tokens: {short_count} vs {long_count}"
    
    print("  ✓ count_tokens tests passed")


if __name__ == "__main__":
    print("Running tests...\n")
    
    test_append_string()
    test_search_and_delete()
    test_search_and_replace()
    test_strip_markdown()
    test_count_tokens()
    
    print("\nAll tests passed!")
