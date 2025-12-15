"""
Package String Processing - A Python package with string processing utilities.

This package provides useful string manipulation and analysis functions.
"""

from .append_string import append_string
from .search_and_delete import search_and_delete
from .search_and_replace import search_and_replace
from .strip_markdown import strip_markdown
from .count_tokens import count_tokens

__version__ = "0.1.0"
__all__ = [
    "append_string",
    "search_and_delete",
    "search_and_replace",
    "strip_markdown",
    "count_tokens",
]
