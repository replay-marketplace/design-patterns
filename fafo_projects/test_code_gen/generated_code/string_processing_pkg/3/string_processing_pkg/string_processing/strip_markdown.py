"""
strip_markdown function.
"""

import re

def strip_markdown(text: str) -> str:
    """
    Remove markdown formatting from text.
    
    This function removes common markdown syntax including:
    - Headers (# ## ###)
    - Bold (**text** or __text__)
    - Italic (*text* or _text_)
    - Links ([text](url))
    - Images (![alt](url))
    - Code blocks (```code``` or `code`)
    - Strikethrough (~~text~~)
    - Blockquotes (> text)
    - Horizontal rules (--- or ***)
    - List markers (- * +)
    
    Args:
        text (str): The markdown text to strip
    
    Returns:
        str: The text with markdown formatting removed
    
    Examples:
        >>> strip_markdown("# Header")
        'Header'
        >>> strip_markdown("This is **bold** text")
        'This is bold text'
        >>> strip_markdown("[Link](http://example.com)")
        'Link'
    """
    # Remove code blocks (triple backticks)
    text = re.sub(r'```[\s\S]*?```', '', text)
    
    # Remove inline code
    text = re.sub(r'`([^`]+)`', r'\1', text)
    
    # Remove images
    text = re.sub(r'!\[([^\]]*)\]\([^\)]+\)', r'\1', text)
    
    # Remove links
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    
    # Remove headers
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)
    
    # Remove bold
    text = re.sub(r'\*\*([^\*]+)\*\*', r'\1', text)
    text = re.sub(r'__([^_]+)__', r'\1', text)
    
    # Remove italic
    text = re.sub(r'\*([^\*]+)\*', r'\1', text)
    text = re.sub(r'_([^_]+)_', r'\1', text)
    
    # Remove strikethrough
    text = re.sub(r'~~([^~]+)~~', r'\1', text)
    
    # Remove blockquotes
    text = re.sub(r'^>\s+', '', text, flags=re.MULTILINE)
    
    # Remove horizontal rules
    text = re.sub(r'^(---|\*\*\*|___)\s*$', '', text, flags=re.MULTILINE)
    
    # Remove list markers
    text = re.sub(r'^[\*\-\+]\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'^\d+\.\s+', '', text, flags=re.MULTILINE)
    
    # Clean up extra whitespace
    text = re.sub(r'\n\s*\n', '\n\n', text)
    text = text.strip()
    
    return text
