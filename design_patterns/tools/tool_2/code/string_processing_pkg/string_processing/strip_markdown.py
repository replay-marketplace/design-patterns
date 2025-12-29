"""Strip markdown function - Remove markdown formatting from text."""

import re


def strip_markdown(text: str) -> str:
    """
    Remove markdown formatting from text.

    Args:
        text: The text containing markdown formatting.

    Returns:
        The text with markdown formatting removed.

    Example:
        >>> result = strip_markdown("# Hello **World**")
        >>> print(result)
        'Hello World'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    # Remove headers (# ## ### etc.)
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)
    
    # Remove bold (**text** or __text__)
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
    text = re.sub(r'__(.*?)__', r'\1', text)
    
    # Remove italic (*text* or _text_)
    text = re.sub(r'\*(.*?)\*', r'\1', text)
    text = re.sub(r'_(.*?)_', r'\1', text)
    
    # Remove code blocks (```code```)
    text = re.sub(r'```[\s\S]*?```', '', text)
    
    # Remove inline code (`code`)
    text = re.sub(r'`([^`]+)`', r'\1', text)
    
    # Remove links [text](url)
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    
    # Remove images ![alt](url)
    text = re.sub(r'!\[([^\]]*)\]\([^\)]+\)', r'\1', text)
    
    # Remove strikethrough (~~text~~)
    text = re.sub(r'~~(.*?)~~', r'\1', text)
    
    # Remove horizontal rules (--- or ***)
    text = re.sub(r'^[-*]{3,}$', '', text, flags=re.MULTILINE)
    
    # Remove list markers (- * + or numbered)
    text = re.sub(r'^[\s]*[-*+]\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'^[\s]*\d+\.\s+', '', text, flags=re.MULTILINE)
    
    # Remove blockquotes (>)
    text = re.sub(r'^>\s+', '', text, flags=re.MULTILINE)
    
    # Clean up extra whitespace
    text = re.sub(r'\n\s*\n', '\n\n', text)
    text = text.strip()
    
    return text



