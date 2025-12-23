"""Basic string processing functions."""

import re


def append_string(base: str, addition: str) -> str:
    """Concatenate two strings.
    
    Args:
        base: The base string
        addition: The string to append
        
    Returns:
        The concatenated string
        
    Examples:
        >>> append_string("Hello", " World")
        'Hello World'
        >>> append_string("", "World")
        'World'
    """
    return base + addition


def search_and_delete(text: str, pattern: str) -> str:
    """Find and remove all occurrences of a pattern from text.
    
    Args:
        text: The text to process
        pattern: The pattern to find and remove
        
    Returns:
        The text with all occurrences of the pattern removed
        
    Examples:
        >>> search_and_delete("Hello World", "World")
        'Hello '
        >>> search_and_delete("foo bar foo", "foo")
        ' bar '
    """
    if not pattern:
        return text
    return text.replace(pattern, "")


def search_and_replace(text: str, old: str, new: str) -> str:
    """Find and replace all occurrences of a pattern in text.
    
    Args:
        text: The text to process
        old: The pattern to find
        new: The replacement string
        
    Returns:
        The text with all occurrences replaced
        
    Examples:
        >>> search_and_replace("Hello World", "World", "Python")
        'Hello Python'
        >>> search_and_replace("foo bar foo", "foo", "baz")
        'baz bar baz'
    """
    if not old:
        return text
    return text.replace(old, new)


def strip_markdown(text: str) -> str:
    """Remove markdown formatting from text.
    
    Removes common markdown elements including:
    - Headers (# ## ###)
    - Bold (**text** or __text__)
    - Italic (*text* or _text_)
    - Links ([text](url))
    - Inline code (`code`)
    - Code blocks (```code```)
    - Strikethrough (~~text~~)
    - Blockquotes (>)
    - Horizontal rules (--- or ***)
    - List markers (- * +)
    
    Args:
        text: The markdown text to process
        
    Returns:
        Plain text with markdown formatting removed
        
    Examples:
        >>> strip_markdown("# Header")
        'Header'
        >>> strip_markdown("This is **bold** text")
        'This is bold text'
    """
    # Remove code blocks first (```code```)
    text = re.sub(r'```[\s\S]*?```', lambda m: m.group(0).replace('```', ''), text)
    text = re.sub(r'```', '', text)
    
    # Remove inline code (`code`)
    text = re.sub(r'`([^`]+)`', r'\1', text)
    
    # Remove headers (# ## ###)
    text = re.sub(r'^#{1,6}\s+', '', text, flags=re.MULTILINE)
    
    # Remove bold (**text** or __text__)
    text = re.sub(r'\*\*([^*]+)\*\*', r'\1', text)
    text = re.sub(r'__([^_]+)__', r'\1', text)
    
    # Remove italic (*text* or _text_)
    text = re.sub(r'\*([^*]+)\*', r'\1', text)
    text = re.sub(r'_([^_]+)_', r'\1', text)
    
    # Remove strikethrough (~~text~~)
    text = re.sub(r'~~([^~]+)~~', r'\1', text)
    
    # Remove links [text](url)
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    
    # Remove images ![alt](url)
    text = re.sub(r'!\[([^\]]*)\]\([^)]+\)', r'\1', text)
    
    # Remove blockquotes
    text = re.sub(r'^>\s+', '', text, flags=re.MULTILINE)
    
    # Remove horizontal rules
    text = re.sub(r'^(-{3,}|\*{3,}|_{3,})$', '', text, flags=re.MULTILINE)
    
    # Remove list markers
    text = re.sub(r'^[\s]*[-*+]\s+', '', text, flags=re.MULTILINE)
    text = re.sub(r'^[\s]*\d+\.\s+', '', text, flags=re.MULTILINE)
    
    return text
