"""
Count tokens function - Estimate token count in text.
"""


def count_tokens(text: str) -> int:
    """
    Estimate the number of tokens in a text string.
    
    Uses a simple approximation: ~4 characters per token for English text.
    This is a rough estimate and may vary based on the actual tokenizer used.

    Args:
        text: The input text to count tokens for.

    Returns:
        An estimated token count.

    Example:
        >>> count_tokens("Hello world")
        3
    """
    if not text:
        return 0
    
    # Simple approximation: ~4 characters per token
    # This is a rough estimate for English text
    # Actual tokenizers may vary significantly
    char_count = len(text)
    estimated_tokens = char_count // 4
    
    # Minimum of 1 token for non-empty strings
    if char_count > 0 and estimated_tokens == 0:
        estimated_tokens = 1
    
    return estimated_tokens

