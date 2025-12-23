"""
count_tokens function.
"""

import re

def count_tokens(text: str) -> int:
    """
    Estimate token count for text.
    
    This function provides a rough estimate of token count using a simple
    heuristic. It splits text on whitespace and punctuation, which approximates
    the behavior of many tokenizers. For more accurate token counting with
    specific models (like GPT), consider using the tiktoken library.
    
    The estimation method:
    - Splits on whitespace
    - Treats punctuation as separate tokens
    - Counts words and punctuation marks
    
    Args:
        text (str): The text to count tokens for
    
    Returns:
        int: Estimated number of tokens
    
    Examples:
        >>> count_tokens("Hello World")
        2
        >>> count_tokens("Hello, World!")
        4
        >>> count_tokens("")
        0
    """
    if not text:
        return 0
    
    # Split on whitespace and punctuation
    # This regex splits on whitespace and keeps punctuation as separate tokens
    tokens = re.findall(r'\w+|[^\w\s]', text)
    
    return len(tokens)
