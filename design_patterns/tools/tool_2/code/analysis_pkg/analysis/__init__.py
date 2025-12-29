"""
Package Analysis - A Python package for code and directory analysis.

This package provides functions for analyzing directories, files, and Python code.
"""

from .count_loc import count_loc
from .count_words import count_words
from .count_files import count_files
from .count_file_types import count_file_types
from .count_function_defs import count_function_defs
from .get_path_to_file import get_path_to_file
from .count_python_imports import count_python_imports
from .count_python_functions import count_python_functions

__version__ = "0.1.0"
__all__ = [
    "count_loc",
    "count_words",
    "count_files",
    "count_file_types",
    "count_function_defs",
    "get_path_to_file",
    "count_python_imports",
    "count_python_functions",
]



