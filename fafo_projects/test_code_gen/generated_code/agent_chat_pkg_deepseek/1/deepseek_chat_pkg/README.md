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

## Configuration

Set your DeepSeek API key as an environment variable:

```bash
export DEEPSEEK_API_KEY="your-api-key-here"
```

## Requirements

- Python >= 3.7
- requests >= 2.28.0
