"""
Package 01 - A Python package with five utility functions.

This package provides five useful functions that can be imported and used
in other projects.
"""

from .function_1 import function_one
from .function_2 import function_two
from .function_3 import function_three
from .function_4 import function_four
from .function_5 import function_five

__version__ = "0.1.0"
__all__ = [
    "function_one",
    "function_two",
    "function_three",
    "function_four",
    "function_five",
]

