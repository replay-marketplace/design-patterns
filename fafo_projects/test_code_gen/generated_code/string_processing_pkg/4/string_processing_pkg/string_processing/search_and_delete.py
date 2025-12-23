"""
search_and_delete function.
"""

def search_and_delete(text: str, pattern: str) -> str:
    """
    Find and remove all occurrences of a pattern from text.
    
    Args:
        text: The input text
        pattern: The pattern to remove
    
    Returns:
        str: Text with pattern removed
    """
    return text.replace(pattern, "")
