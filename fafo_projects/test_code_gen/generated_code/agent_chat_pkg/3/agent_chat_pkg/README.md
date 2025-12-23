# Agent Chat Package

A Python package for interacting with Anthropic's Claude AI (Sonnet 4.5) for various chat and code generation tasks.

## Features

- **Simple Chat**: Basic chat functionality with Claude
- **Configurable Chat**: Chat with custom system messages and low temperature for deterministic outputs
- **JSON Response Chat**: Get JSON-only responses with agent-type-specific system messages

## Installation

```bash
pip install -e .
```

## Requirements

- Python >= 3.7
- anthropic >= 0.18.0
- ANTHROPIC_API_KEY environment variable

## Usage

### Setup

First, set your Anthropic API key as an environment variable:

```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

### Simple Chat

```python
from agent_chat import simple_chat

response = simple_chat("What is the capital of France?")
print(response)
```

### Chat with Custom Configuration

```python
from agent_chat import chat_agent_code_config

system_message = "You are a helpful Python programming assistant."
prompt = "Write a function to calculate fibonacci numbers."

response = chat_agent_code_config(prompt, system_message)
print(response)
```

### JSON-Only Response

```python
from agent_chat import chat_agent_code_json
import json

prompt = "Generate a JSON object with user data including name, age, and email."
response = chat_agent_code_json(prompt, "data")

# Parse the JSON response
data = json.loads(response)
print(data)
```

## Agent Types

The `chat_agent_code_json` function supports the following agent types:

- `python`: Python code generation assistant
- `javascript`: JavaScript code generation assistant
- `data`: Data analysis assistant
- `general`: General code generation assistant (default)

## Model Configuration

- **Model**: claude-sonnet-4-5-20250929
- **Max Tokens**: 16,000
- **Temperature**: 
  - Simple chat: Default (1.0)
  - Code config: Low (0.2)
  - JSON response: Low (0.3)

## Testing

Run tests with:

```bash
cd tests
bash setup_and_run.sh
```

Or manually:

```bash
pip install -r tests/requirements.txt
pytest tests/test.py -v
```

## API Reference

See [README_API_SIGNATURE.md](README_API_SIGNATURE.md) for detailed API signatures.

## License

MIT License
