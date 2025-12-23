# string_processing Package

A Python package for string processing and analysis operations.

## Installation

```bash
cd string_processing_pkg
pip install -e .
```

## Usage

```python
from string_processing import (
    append_string,
    search_and_delete,
    search_and_replace,
    strip_markdown,
    count_tokens
)

# Basic operations
result = append_string("Hello", " World")
text = search_and_delete("Hello World", "World")
text = search_and_replace("Hello World", "World", "Python")
plain = strip_markdown("# Title\n**bold** text")

# Analysis
token_count = count_tokens("This is a sample text")
```

## Function Signatures

### Basic Operations

#### append_string(base: str, addition: str) -> str

Concatenate two strings.

**Parameters:**
- `base` (str): The base string
- `addition` (str): The string to append

**Returns:**
- str: Concatenated string

#### search_and_delete(text: str, pattern: str) -> str

Find and remove all occurrences of a pattern from text.

**Parameters:**
- `text` (str): The input text
- `pattern` (str): The pattern to remove

**Returns:**
- str: Text with pattern removed

#### search_and_replace(text: str, old: str, new: str) -> str

Find and replace all occurrences of a pattern.

**Parameters:**
- `text` (str): The input text
- `old` (str): The pattern to find
- `new` (str): The replacement string

**Returns:**
- str: Text with replacements made

#### strip_markdown(text: str) -> str

Remove markdown formatting from text.

**Parameters:**
- `text` (str): Markdown formatted text

**Returns:**
- str: Plain text without markdown

### Analysis

#### count_tokens(text: str) -> int

Estimate token count for text (approximation based on words and punctuation).

**Parameters:**
- `text` (str): The input text

**Returns:**
- int: Estimated token count

## Running Tests

```bash
cd tests
chmod +x setup_and_run.sh
./setup_and_run.sh
```

This will create a virtual environment, install dependencies, install the package, and run the tests.
