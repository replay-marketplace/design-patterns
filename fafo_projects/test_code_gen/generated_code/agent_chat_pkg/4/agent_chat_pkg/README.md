# Agent Chat - DeepSeek API Integration

A Python package for interacting with the DeepSeek API, specifically configured for code generation tasks.

## Features

- **Simple Chat**: Basic prompt-response interaction
- **Configurable Code Generation**: Control temperature and system prompts for deterministic code generation
- **JSON-Only Responses**: Get structured JSON responses with automatic agent type selection

## Installation

```bash
pip install -e .
```

## Configuration

1. Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```

2. Add your DeepSeek API key to `.env`:
```
DEEPSEEK_API_KEY=your_actual_api_key_here
```

## Usage

### Simple Chat

```python
from agent_chat import simple_chat

response = simple_chat("Write a Python function to calculate factorial")
print(response)
```

### Configurable Code Generation

```python
from agent_chat import chat_agent_code_config

response = chat_agent_code_config(
    prompt="Create a binary search function",
    system="You are an expert Python developer focused on algorithms"
)
print(response)
```

### JSON-Only Responses

```python
from agent_chat import chat_agent_code_json

# Python agent
response = chat_agent_code_json(
    prompt="Generate a JSON schema for a user profile",
    agent_type="python"
)
print(response)

# JavaScript agent
response = chat_agent_code_json(
    prompt="Create a package.json configuration",
    agent_type="javascript"
)
print(response)
```

## Agent Types

The following agent types are supported for `chat_agent_code_json`:

- `python` - Python code generation
- `javascript` - JavaScript/TypeScript code generation
- `java` - Java code generation
- `cpp` - C++ code generation
- `general` - General purpose code generation
- `json` - Pure JSON responses

## API Reference

See [README_API_SIGNATURE.md](README_API_SIGNATURE.md) for detailed API documentation.

## Testing

```bash
cd tests
bash setup_and_run.sh
```

Or manually:

```bash
pip install -r tests/requirements.txt
pytest tests/test.py -v
```

## Requirements

- Python >= 3.7
- requests >= 2.28.0
- python-dotenv >= 1.0.0

## License

MIT License
