"""
search_and_replace function.
"""

def search_and_replace(text: str, old: str, new: str) -> str:
    """
    Find and replace all occurrences of a pattern in text.
    
    Args:
        text: The text to search in
        old: The pattern to find
        new: The replacement string
    
    Returns:
        str: The text with all occurrences of old replaced with new
    
    Examples:
        >>> search_and_replace("Hello World", "World", "Python")
        'Hello Python'
        >>> search_and_replace("foo bar foo", "foo", "baz")
        'baz bar baz'
    """
    return text.replace(old, new)
