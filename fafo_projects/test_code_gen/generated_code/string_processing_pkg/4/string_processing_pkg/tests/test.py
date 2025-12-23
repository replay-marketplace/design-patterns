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
    
    result = append_string("", "test")
    assert result == "test", f"Expected 'test', got '{result}'"
    
    result = append_string("test", "")
    assert result == "test", f"Expected 'test', got '{result}'"
    
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
    result = strip_markdown("# Title")
    assert result == "Title", f"Expected 'Title', got '{result}'"
    
    # Test bold
    result = strip_markdown("**bold text**")
    assert result == "bold text", f"Expected 'bold text', got '{result}'"
    
    # Test italic
    result = strip_markdown("*italic text*")
    assert result == "italic text", f"Expected 'italic text', got '{result}'"
    
    # Test links
    result = strip_markdown("[link text](http://example.com)")
    assert result == "link text", f"Expected 'link text', got '{result}'"
    
    # Test inline code
    result = strip_markdown("`code`")
    assert result == "code", f"Expected 'code', got '{result}'"
    
    # Test complex markdown
    markdown = """# Title
**bold** and *italic* text
[link](http://example.com)
`code`"""
    result = strip_markdown(markdown)
    assert "#" not in result, "Headers should be removed"
    assert "**" not in result, "Bold markers should be removed"
    assert "*" not in result, "Italic markers should be removed"
    assert "[" not in result and "]" not in result, "Link markers should be removed"
    assert "`" not in result, "Code markers should be removed"
    
    print("  ✓ strip_markdown tests passed")


def test_count_tokens():
    """Test count_tokens function."""
    print("Testing count_tokens...")
    
    # Simple text
    result = count_tokens("Hello World")
    assert result > 0, "Token count should be positive"
    assert result >= 2, f"Expected at least 2 tokens, got {result}"
    
    # Empty string
    result = count_tokens("")
    assert result == 0, f"Expected 0 tokens for empty string, got {result}"
    
    # Text with punctuation
    result = count_tokens("Hello, World!")
    assert result >= 4, f"Expected at least 4 tokens (2 words + 2 punctuation), got {result}"
    
    # Longer text
    text = "This is a longer text with multiple words and punctuation marks."
    result = count_tokens(text)
    assert result >= 10, f"Expected at least 10 tokens, got {result}"
    
    print("  ✓ count_tokens tests passed")


if __name__ == "__main__":
    print("Running tests...\n")
    
    test_append_string()
    test_search_and_delete()
    test_search_and_replace()
    test_strip_markdown()
    test_count_tokens()
    
    print("\n✓ All tests passed!")
