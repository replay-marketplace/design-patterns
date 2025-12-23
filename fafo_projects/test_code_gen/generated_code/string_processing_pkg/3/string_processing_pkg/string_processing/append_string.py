"""
append_string function.
"""

def append_string(base: str, addition: str) -> str:
    """
    Concatenate two strings together.
    
    Args:
        base (str): The base string to append to
        addition (str): The string to append
    
    Returns:
        str: The concatenated result of base + addition
    
    Examples:
        >>> append_string("Hello", " World")
        'Hello World'
        >>> append_string("Python", " Programming")
        'Python Programming'
    """
    return base + addition
