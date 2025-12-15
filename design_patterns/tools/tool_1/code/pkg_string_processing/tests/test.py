"""
Tests for pkg_string_processing package.
"""

import sys
import os

# Add the package to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'package'))

from code.append_string import append_string
from code.search_and_delete import search_and_delete
from code.search_and_replace import search_and_replace
from code.strip_markdown import strip_markdown
from code.count_tokens import count_tokens


def test_append_string():
    """Test append_string function."""
    assert append_string("Hello", " World") == "Hello World"
    assert append_string("", "test") == "test"
    assert append_string("base", "") == "base"
    print("✓ append_string tests passed")


def test_search_and_delete():
    """Test search_and_delete function."""
    assert search_and_delete("Hello World Hello", "Hello ") == "World Hello"
    assert search_and_delete("Hello World", "Hello ") == "World"
    assert search_and_delete("test", "x") == "test"
    assert search_and_delete("abcabc", "abc") == ""
    print("✓ search_and_delete tests passed")


def test_search_and_replace():
    """Test search_and_replace function."""
    assert search_and_replace("Hello World", "World", "Python") == "Hello Python"
    assert search_and_replace("test", "x", "y") == "test"
    assert search_and_replace("abcabc", "abc", "xyz") == "xyzxyz"
    print("✓ search_and_replace tests passed")


def test_strip_markdown():
    """Test strip_markdown function."""
    assert "Header" in strip_markdown("# Header")
    assert "bold" in strip_markdown("**bold**")
    assert "italic" in strip_markdown("*italic*")
    assert "link" in strip_markdown("[link](url)")
    print("✓ strip_markdown tests passed")


def test_count_tokens():
    """Test count_tokens function."""
    assert count_tokens("Hello world") > 0
    assert count_tokens("") == 0
    assert count_tokens("a") == 1
    assert count_tokens("This is a longer text") > 0
    print("✓ count_tokens tests passed")


if __name__ == "__main__":
    print("Running tests for pkg_string_processing...\n")
    test_append_string()
    test_search_and_delete()
    test_search_and_replace()
    test_strip_markdown()
    test_count_tokens()
    print("\nAll tests passed! ✓")

