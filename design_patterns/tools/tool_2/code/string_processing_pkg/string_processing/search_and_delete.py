"""Search and delete function - Find and remove pattern from text."""


def search_and_delete(text: str, pattern: str) -> str:
    """
    Find and remove all occurrences of a pattern from text.

    Args:
        text: The text to search in.
        pattern: The pattern to find and remove.

    Returns:
        The text with all occurrences of the pattern removed.

    Example:
        >>> result = search_and_delete("Hello World Hello", "Hello")
        >>> print(result)
        ' World '
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not isinstance(pattern, str):
        raise TypeError("pattern must be a string")
    
    return text.replace(pattern, "")



