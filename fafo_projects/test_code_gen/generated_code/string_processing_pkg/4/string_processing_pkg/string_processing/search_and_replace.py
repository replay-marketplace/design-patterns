"""
search_and_replace function.
"""

def search_and_replace(text: str, old: str, new: str) -> str:
    """
    Find and replace all occurrences of a pattern.
    
    Args:
        text: The input text
        old: The pattern to find
        new: The replacement string
    
    Returns:
        str: Text with replacements made
    """
    return text.replace(old, new)
