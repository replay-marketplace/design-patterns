def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome.
    
    A palindrome is a string that reads the same forwards and backwards.
    This function ignores case and non-alphanumeric characters.
    
    Args:
        s: The string to check.
        
    Returns:
        True if the string is a palindrome, False otherwise.
    """
    # Clean the string: remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the cleaned string equals its reverse
    return cleaned == cleaned[::-1]
