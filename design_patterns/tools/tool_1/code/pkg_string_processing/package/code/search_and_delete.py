"""
Search and delete function - Find and remove pattern from text.
"""


def search_and_delete(text: str, pattern: str) -> str:
    """
    Find and remove all occurrences of a pattern from text.

    Args:
        text: The input text to search in.
        pattern: The pattern to find and remove (treated as literal string).

    Returns:
        The text with all occurrences of the pattern removed.

    Example:
        >>> search_and_delete("Hello World", "Hello ")
        'World'
    """
    return text.replace(pattern, "")

