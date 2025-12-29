"""
Package String Processing - A Python package with string processing utilities.

This package provides functions for string manipulation and processing.
"""

from .append_string import append_string
from .search_and_delete import search_and_delete
from .search_and_replace import search_and_replace
from .strip_markdown import strip_markdown

__version__ = "0.1.0"
__all__ = [
    "append_string",
    "search_and_delete",
    "search_and_replace",
    "strip_markdown",
]



