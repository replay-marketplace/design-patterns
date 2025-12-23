"""
search_and_delete function.
"""

def search_and_delete(text: str, pattern: str) -> str:
    """
    Find and remove all occurrences of a pattern from text.
    
    Args:
        text: The text to search in
        pattern: The pattern to find and remove
    
    Returns:
        str: The text with all occurrences of the pattern removed
    
    Examples:
        >>> search_and_delete("Hello World", "World")
        'Hello '
        >>> search_and_delete("test test test", "test")
        '  '
    """
    return text.replace(pattern, "")
