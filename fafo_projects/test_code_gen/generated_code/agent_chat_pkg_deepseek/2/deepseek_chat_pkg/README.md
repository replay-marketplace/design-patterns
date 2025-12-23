# DeepSeek Chat Package

A Python package for interacting with the DeepSeek API for code generation.

## Installation

```bash
pip install -e .
```

## Usage

```python
from deepseek_chat import simple_chat

response = simple_chat("Write a Python function to calculate factorial")
print(response)
```

## Requirements

- Python >= 3.7
- deepseek-api

## API Signature

`simple_chat(prompt: str) -> str` - Send prompt to DeepSeek API and return response
