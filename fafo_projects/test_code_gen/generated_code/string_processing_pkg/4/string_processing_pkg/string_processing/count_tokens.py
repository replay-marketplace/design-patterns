"""
count_tokens function.
"""

import re

def count_tokens(text: str) -> int:
    """
    Estimate token count for text.
    
    This is a simple approximation based on words and punctuation.
    A more accurate count would require a tokenizer like tiktoken.
    
    Approximation rules:
    - Each word is roughly 1 token
    - Punctuation marks are separate tokens
    - Numbers are tokens
    - Common contractions count as 2 tokens
    
    Args:
        text: The input text
    
    Returns:
        int: Estimated token count
    """
    if not text:
        return 0
    
    # Split on whitespace and count words
    words = text.split()
    token_count = 0
    
    for word in words:
        # Count alphanumeric sequences
        alphanumeric = re.findall(r'\w+', word)
        token_count += len(alphanumeric)
        
        # Count punctuation marks
        punctuation = re.findall(r'[^\w\s]', word)
        token_count += len(punctuation)
    
    # Adjust for common patterns (rough approximation)
    # Most tokens are slightly less than words due to subword tokenization
    # But punctuation adds tokens, so this is a reasonable estimate
    
    return max(1, token_count)
