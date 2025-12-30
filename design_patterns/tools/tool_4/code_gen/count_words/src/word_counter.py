def count_words(text: str) -> int:
    """Count the number of words in a string.
    
    Words are defined as sequences of characters separated by whitespace.
    
    Args:
        text: The input string to count words in.
        
    Returns:
        The number of words in the string.
    """
    if not text or not text.strip():
        return 0
    
    words = text.split()
    return len(words)
