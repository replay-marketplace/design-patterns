def longest_common_prefix(strs: list[str]) -> str:
    """
    Find the longest common prefix among an array of strings.
    
    Args:
        strs: A list of strings to find the common prefix from.
        
    Returns:
        The longest common prefix string. Returns empty string if no common prefix exists.
    """
    if not strs:
        return ""
    
    if len(strs) == 1:
        return strs[0]
    
    # Find the shortest string length to limit our search
    min_length = min(len(s) for s in strs)
    
    if min_length == 0:
        return ""
    
    prefix = ""
    
    # Check each character position
    for i in range(min_length):
        # Get the character at position i from the first string
        current_char = strs[0][i]
        
        # Check if all strings have the same character at position i
        if all(s[i] == current_char for s in strs):
            prefix += current_char
        else:
            break
    
    return prefix
