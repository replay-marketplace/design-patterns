import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from string_processing import (
    append_string,
    search_and_delete,
    search_and_replace,
    strip_markdown,
    count_tokens
)


class TestBasicStringProcessing:
    """Test basic string processing functions."""

    def test_append_string_basic(self):
        result = append_string("Hello", " World")
        assert result == "Hello World"

    def test_append_string_empty_base(self):
        result = append_string("", "World")
        assert result == "World"

    def test_append_string_empty_addition(self):
        result = append_string("Hello", "")
        assert result == "Hello"

    def test_append_string_both_empty(self):
        result = append_string("", "")
        assert result == ""

    def test_search_and_delete_basic(self):
        result = search_and_delete("Hello World", "World")
        assert result == "Hello "

    def test_search_and_delete_multiple_occurrences(self):
        result = search_and_delete("foo bar foo baz foo", "foo")
        assert result == " bar  baz "

    def test_search_and_delete_not_found(self):
        result = search_and_delete("Hello World", "xyz")
        assert result == "Hello World"

    def test_search_and_delete_empty_pattern(self):
        result = search_and_delete("Hello World", "")
        assert result == "Hello World"

    def test_search_and_replace_basic(self):
        result = search_and_replace("Hello World", "World", "Python")
        assert result == "Hello Python"

    def test_search_and_replace_multiple(self):
        result = search_and_replace("foo bar foo baz", "foo", "qux")
        assert result == "qux bar qux baz"

    def test_search_and_replace_not_found(self):
        result = search_and_replace("Hello World", "xyz", "abc")
        assert result == "Hello World"

    def test_search_and_replace_empty_old(self):
        result = search_and_replace("Hello World", "", "xyz")
        assert result == "Hello World"

    def test_strip_markdown_headers(self):
        result = strip_markdown("# Header 1\n## Header 2")
        assert result == "Header 1\nHeader 2"

    def test_strip_markdown_bold(self):
        result = strip_markdown("This is **bold** text")
        assert result == "This is bold text"

    def test_strip_markdown_italic(self):
        result = strip_markdown("This is *italic* text")
        assert result == "This is italic text"

    def test_strip_markdown_links(self):
        result = strip_markdown("[Link text](https://example.com)")
        assert result == "Link text"

    def test_strip_markdown_code(self):
        result = strip_markdown("`inline code` and ```block code```")
        assert result == "inline code and block code"

    def test_strip_markdown_complex(self):
        text = "# Title\n\nThis is **bold** and *italic* with [a link](url) and `code`."
        result = strip_markdown(text)
        assert "#" not in result
        assert "**" not in result
        assert "*" not in result
        assert "[" not in result
        assert "]" not in result
        assert "(" not in result or "url" not in result
        assert "`" not in result


class TestAnalysis:
    """Test analysis functions."""

    def test_count_tokens_empty(self):
        result = count_tokens("")
        assert result == 0

    def test_count_tokens_single_word(self):
        result = count_tokens("Hello")
        assert result > 0

    def test_count_tokens_sentence(self):
        result = count_tokens("Hello, how are you?")
        assert result > 0

    def test_count_tokens_longer_text(self):
        text = "This is a longer piece of text with multiple words and sentences."
        result = count_tokens(text)
        assert result > 5

    def test_count_tokens_whitespace(self):
        result = count_tokens("   ")
        assert result >= 0

    def test_count_tokens_special_chars(self):
        result = count_tokens("Hello! How are you? I'm fine.")
        assert result > 0

    def test_count_tokens_comparison(self):
        short = count_tokens("Hello")
        long = count_tokens("Hello World, this is a much longer text")
        assert long > short
