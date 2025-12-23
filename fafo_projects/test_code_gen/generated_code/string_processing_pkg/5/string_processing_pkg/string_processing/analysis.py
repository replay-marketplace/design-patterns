"""String analysis functions."""

import re


def count_tokens(text: str) -> int:
    """Estimate token count for text.
    
    This function provides a simple estimation of token count based on
    whitespace and punctuation splitting. The estimation follows these rules:
    - Words are split by whitespace
    - Punctuation marks are counted as separate tokens
    - Numbers are counted as tokens
    
    Note: This is a simple approximation and may not match exact tokenization
    used by specific language models (like GPT tokenizers).
    
    Args:
        text: The text to analyze
        
    Returns:
        Estimated number of tokens
        
    Examples:
        >>> count_tokens("Hello, world!")
        4
        >>> count_tokens("This is a test.")
        5
        >>> count_tokens("")
        0
    """
    if not text or not text.strip():
        return 0
    
    # Split on whitespace and punctuation while keeping them
    # This regex splits on word boundaries and keeps punctuation as separate tokens
    tokens = re.findall(r'\b\w+\b|[^\w\s]', text)
    
    # Filter out empty tokens
    tokens = [t for t in tokens if t.strip()]
    
    return len(tokens)
