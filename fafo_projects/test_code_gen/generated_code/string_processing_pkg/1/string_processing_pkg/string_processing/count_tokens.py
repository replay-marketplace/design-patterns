"""
count_tokens function.
"""

import re

def count_tokens(text: str) -> int:
    """
    Estimate the token count of a text string.
    
    This function provides a simple estimation of tokens by:
    1. Splitting on whitespace to get words
    2. Counting punctuation as separate tokens
    3. Applying a rough approximation for subword tokenization
    
    Note: This is a simplified estimation. For accurate token counts,
    use a proper tokenizer like tiktoken for OpenAI models.
    
    Args:
        text: The text to count tokens for
    
    Returns:
        int: Estimated number of tokens
    
    Examples:
        >>> count_tokens("Hello World")
        2
        >>> count_tokens("This is a test.")
        5
    """
    if not text:
        return 0
    
    # Split on whitespace to get initial word count
    words = text.split()
    
    token_count = 0
    
    for word in words:
        # Count punctuation separately
        # Remove punctuation and count it
        punctuation = re.findall(r'[^\w\s]', word)
        token_count += len(punctuation)
        
        # Remove punctuation from word
        clean_word = re.sub(r'[^\w]', '', word)
        
        if clean_word:
            # Estimate subword tokens
            # Rough approximation: 1 token per 4 characters for longer words
            if len(clean_word) <= 4:
                token_count += 1
            else:
                # Longer words may be split into multiple tokens
                token_count += max(1, len(clean_word) // 4)
    
    return token_count
