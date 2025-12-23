"""
search_and_delete function.
"""

def search_and_delete(text: str, pattern: str) -> str:
    """
    Find and remove all occurrences of a pattern from text.
    
    Args:
        text (str): The text to search in
        pattern (str): The pattern to find and remove
    
    Returns:
        str: The text with all occurrences of pattern removed
    
    Examples:
        >>> search_and_delete("Hello World", "World")
        'Hello '
        >>> search_and_delete("foo bar foo", "foo")
        ' bar '
    """
    return text.replace(pattern, "")
