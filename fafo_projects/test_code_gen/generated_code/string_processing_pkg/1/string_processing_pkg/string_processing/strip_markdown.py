"""
strip_markdown function.
"""

import re

def strip_markdown(text: str) -> str:
    """
    Remove markdown formatting from text.
    
    This function removes common markdown elements including:
    - Headers (# ## ### etc.)
    - Bold (**text** or __text__)
    - Italic (*text* or _text_)
    - Links ([text](url))
    - Images (![alt](url))
    - Code blocks (```code``` or `code`)
    - Strikethrough (~~text~~)
    - Blockquotes (> text)
    - Horizontal rules (--- or ***)
    - List markers (- or * or 1.)
    
    Args:
        text: The markdown text to strip
    
    Returns:
        str: The text with markdown formatting removed
    
    Examples:
        >>> strip_markdown("# Header")
        'Header'
        >>> strip_markdown("**bold** and *italic*")
        'bold and italic'
        >>> strip_markdown("[link](http://example.com)")
        'link'
    """
    # Remove code blocks first (triple backticks)
    text = re.sub(r'```[\s\S]*?```', '', text)
    
    # Remove inline code
    text = re.sub(r'`([^`]+)`', r'\1', text)
    
    # Remove images
    text = re.sub(r'!\[([^\]]*)\]\([^\)]+\)', r'\1', text)
    
    # Remove links
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    
    # Remove headers
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)
    
    # Remove bold (** or __)
    text = re.sub(r'\*\*([^\*]+)\*\*', r'\1', text)
    text = re.sub(r'__([^_]+)__', r'\1', text)
    
    # Remove italic (* or _)
    text = re.sub(r'\*([^\*]+)\*', r'\1', text)
    text = re.sub(r'_([^_]+)_', r'\1', text)
    
    # Remove strikethrough
    text = re.sub(r'~~([^~]+)~~', r'\1', text)
    
    # Remove blockquotes
    text = re.sub(r'^>\s+', '', text, flags=re.MULTILINE)
    
    # Remove horizontal rules
    text = re.sub(r'^(\*{3,}|-{3,}|_{3,})$', '', text, flags=re.MULTILINE)
    
    # Remove list markers
    text = re.sub(r'^[\*\-\+]\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'^\d+\.\s+', '', text, flags=re.MULTILINE)
    
    # Clean up extra whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = text.strip()
    
    return text
