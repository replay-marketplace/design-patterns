# String Processing Package

A Python package for common string processing operations including concatenation, search and replace, markdown stripping, and token counting.

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

# Concatenate strings
result = append_string("Hello", " World")
print(result)  # "Hello World"

# Find and remove text
result = search_and_delete("Hello World", "World")
print(result)  # "Hello "

# Find and replace text
result = search_and_replace("Hello World", "World", "Python")
print(result)  # "Hello Python"

# Remove markdown formatting
result = strip_markdown("# Header\n\nThis is **bold** text")
print(result)  # "Header\n\nThis is bold text"

# Count tokens
token_count = count_tokens("Hello World")
print(token_count)  # 2
```

## Function Signatures

### append_string(base: str, addition: str) -> str

Concatenate two strings together.

**Parameters:**
- `base` (str): The base string to append to
- `addition` (str): The string to append

**Returns:**
- str: The concatenated result of base + addition

**Example:**
```python
append_string("Hello", " World")  # "Hello World"
```

### search_and_delete(text: str, pattern: str) -> str

Find and remove all occurrences of a pattern from text.

**Parameters:**
- `text` (str): The text to search in
- `pattern` (str): The pattern to find and remove

**Returns:**
- str: The text with all occurrences of pattern removed

**Example:**
```python
search_and_delete("Hello World", "World")  # "Hello "
```

### search_and_replace(text: str, old: str, new: str) -> str

Find and replace all occurrences of a pattern with a new string.

**Parameters:**
- `text` (str): The text to search in
- `old` (str): The pattern to find
- `new` (str): The replacement string

**Returns:**
- str: The text with all occurrences of old replaced with new

**Example:**
```python
search_and_replace("Hello World", "World", "Python")  # "Hello Python"
```

### strip_markdown(text: str) -> str

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

**Parameters:**
- `text` (str): The markdown text to strip

**Returns:**
- str: The text with markdown formatting removed

**Example:**
```python
strip_markdown("# Header")  # "Header"
strip_markdown("This is **bold** text")  # "This is bold text"
```

### count_tokens(text: str) -> int

Estimate token count for text.

This function provides a rough estimate of token count using a simple heuristic. It splits text on whitespace and punctuation, which approximates the behavior of many tokenizers.

**Parameters:**
- `text` (str): The text to count tokens for

**Returns:**
- int: Estimated number of tokens

**Example:**
```python
count_tokens("Hello World")  # 2
count_tokens("Hello, World!")  # 4
```

## Running Tests

```bash
cd tests
chmod +x setup_and_run.sh
./setup_and_run.sh
```

This will create a virtual environment, install dependencies, install the package, and run the tests.

## License

MIT License
