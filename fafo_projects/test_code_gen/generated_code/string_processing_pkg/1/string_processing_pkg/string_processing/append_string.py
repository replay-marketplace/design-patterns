"""
append_string function.
"""

def append_string(base: str, addition: str) -> str:
    """
    Concatenate two strings together.
    
    Args:
        base: The base string to append to
        addition: The string to append to the base
    
    Returns:
        str: The concatenated string
    
    Examples:
        >>> append_string("Hello", " World")
        'Hello World'
        >>> append_string("Python", " Programming")
        'Python Programming'
    """
    return base + addition
