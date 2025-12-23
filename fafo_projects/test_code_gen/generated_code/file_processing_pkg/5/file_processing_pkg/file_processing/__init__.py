"""File Processing Package

A package for file processing operations including reading, writing,
and directory management.
"""

from .save_text_to_file import save_text_to_file
from .read_file_content import read_file_content
from .create_directory_structure import create_directory_structure
from .file_exists import file_exists
from .dir_exists import dir_exists

__all__ = [
    'save_text_to_file',
    'read_file_content',
    'create_directory_structure',
    'file_exists',
    'dir_exists',
]

__version__ = '0.1.0'
