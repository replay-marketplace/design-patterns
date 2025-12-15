"""
Function 1: String manipulation utility.
"""


def function_one(text: str, prefix: str = "", suffix: str = "") -> str:
    """
    Add a prefix and/or suffix to a text string.

    Args:
        text: The input text string.
        prefix: Optional prefix to add to the text.
        suffix: Optional suffix to add to the text.

    Returns:
        The text with prefix and/or suffix added.

    Example:
        >>> function_one("world", prefix="Hello ", suffix="!")
        'Hello world!'
    """
    return f"{prefix}{text}{suffix}"

