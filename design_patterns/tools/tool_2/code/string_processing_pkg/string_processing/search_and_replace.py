"""Search and replace function - Find and replace pattern in text."""


def search_and_replace(text: str, old: str, new: str) -> str:
    """
    Find and replace all occurrences of a pattern in text.

    Args:
        text: The text to search in.
        old: The pattern to find.
        new: The replacement string.

    Returns:
        The text with all occurrences of old replaced with new.

    Example:
        >>> result = search_and_replace("Hello World", "World", "Python")
        >>> print(result)
        'Hello Python'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not isinstance(old, str):
        raise TypeError("old must be a string")
    if not isinstance(new, str):
        raise TypeError("new must be a string")
    
    return text.replace(old, new)


