# pkg_string_processing

A Python package with string processing utilities.

## Installation

```bash
pip install -e .
```

## Function Signatures

### Basic

- `append_string(base: str, addition: str) -> str` - Concatenate strings
- `search_and_delete(text: str, pattern: str) -> str` - Find and remove
- `search_and_replace(text: str, old: str, new: str) -> str` - Find and replace
- `strip_markdown(text: str) -> str` - Remove markdown formatting

### Analysis

- `count_tokens(text: str) -> int` - Estimate token count

