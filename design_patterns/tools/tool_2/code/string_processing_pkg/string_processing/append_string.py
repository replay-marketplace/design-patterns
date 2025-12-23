"""Append string function - Concatenate strings."""


def append_string(base: str, addition: str) -> str:
    """
    Concatenate two strings together.

    Args:
        base: The base string to append to.
        addition: The string to append to the base.

    Returns:
        The concatenated string.

    Example:
        >>> result = append_string("Hello", " World")
        >>> print(result)
        'Hello World'
    """
    if not isinstance(base, str):
        raise TypeError("base must be a string")
    if not isinstance(addition, str):
        raise TypeError("addition must be a string")
    
    return base + addition


