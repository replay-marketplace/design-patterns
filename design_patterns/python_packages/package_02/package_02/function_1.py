"""
Function 1: Greeting formatter that uses package_01 functionality.
"""

from package_01 import function_one as format_text


def function_one(name: str, greeting: str = "Hello") -> str:
    """
    Create a formatted greeting message using package_01's function_one.

    This function uses function_one from package_01 to format a greeting
    message with a name.

    Args:
        name: The name to include in the greeting.
        greeting: The greeting word (default: "Hello").

    Returns:
        A formatted greeting string.

    Example:
        >>> function_one("Alice")
        'Hello Alice!'
        >>> function_one("Bob", greeting="Hi")
        'Hi Bob!'
    """
    return format_text(name, prefix=f"{greeting} ", suffix="!")

