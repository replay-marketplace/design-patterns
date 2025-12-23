"""
search_and_replace function.
"""

def search_and_replace(text: str, old: str, new: str) -> str:
    """
    Find and replace all occurrences of a pattern with a new string.
    
    Args:
        text (str): The text to search in
        old (str): The pattern to find
        new (str): The replacement string
    
    Returns:
        str: The text with all occurrences of old replaced with new
    
    Examples:
        >>> search_and_replace("Hello World", "World", "Python")
        'Hello Python'
        >>> search_and_replace("foo bar foo", "foo", "baz")
        'baz bar baz'
    """
    return text.replace(old, new)
