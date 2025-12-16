"""
Function 3: Data validation utility.
"""


def function_three(email: str) -> bool:
    """
    Validate if a string is a valid email address format.

    Args:
        email: The email string to validate.

    Returns:
        True if the email format is valid, False otherwise.

    Example:
        >>> function_three("user@example.com")
        True
        >>> function_three("invalid-email")
        False
    """
    import re

    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


