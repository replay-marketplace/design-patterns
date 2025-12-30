def are_anagrams(str1: str, str2: str) -> bool:
    """
    Check if two strings are anagrams of each other.
    
    Anagrams are words or phrases that contain the same characters
    with the same frequencies, ignoring case and spaces.
    
    Args:
        str1: First string to compare
        str2: Second string to compare
    
    Returns:
        True if the strings are anagrams, False otherwise
    """
    # Normalize: convert to lowercase and remove spaces
    normalized1 = str1.lower().replace(" ", "")
    normalized2 = str2.lower().replace(" ", "")
    
    # If lengths differ after normalization, they can't be anagrams
    if len(normalized1) != len(normalized2):
        return False
    
    # Sort characters and compare
    return sorted(normalized1) == sorted(normalized2)
