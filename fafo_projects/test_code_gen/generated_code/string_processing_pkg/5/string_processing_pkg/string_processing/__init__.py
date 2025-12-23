"""String processing package for basic string operations and analysis."""

from .basic import (
    append_string,
    search_and_delete,
    search_and_replace,
    strip_markdown
)

from .analysis import count_tokens

__all__ = [
    'append_string',
    'search_and_delete',
    'search_and_replace',
    'strip_markdown',
    'count_tokens'
]

__version__ = "0.1.0"
