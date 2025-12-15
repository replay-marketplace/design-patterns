"""
Search and replace function - Find and replace pattern in text.
"""


def search_and_replace(text: str, old: str, new: str) -> str:
    """
    Find and replace all occurrences of a pattern in text.

    Args:
        text: The input text to search in.
        old: The pattern to find (treated as literal string).
        new: The replacement string.

    Returns:
        The text with all occurrences of old replaced with new.

    Example:
        >>> search_and_replace("Hello World", "World", "Python")
        'Hello Python'
    """
    return text.replace(old, new)

