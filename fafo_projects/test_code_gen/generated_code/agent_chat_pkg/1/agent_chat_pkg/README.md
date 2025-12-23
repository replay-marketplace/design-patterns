# agent_chat Package

A Python package for interacting with Anthropic's Claude AI (model: claude-sonnet-4-20250514) for chat and code generation tasks.

## API Signatures

- `simple_chat(prompt: str) -> str` - Send a prompt to Claude and return the response
- `chat_agent_code_config(prompt: str, system: str) -> str` - Send a prompt with custom system message and low temperature
- `chat_agent_code_json(prompt: str, agent_type: str) -> str` - Send a prompt and get a JSON-only response

## Installation

```bash
cd agent_chat_pkg
pip install -e .
```

## Setup

Set your Anthropic API key as an environment variable:

```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

Or in Python:

```python
import os
os.environ['ANTHROPIC_API_KEY'] = 'your-api-key-here'
```

## Usage

```python
from agent_chat import simple_chat, chat_agent_code_config, chat_agent_code_json

# Simple chat
response = simple_chat("What is the capital of France?")
print(response)

# Chat with custom configuration (low temperature, no max token limit)
response = chat_agent_code_config(
    prompt="Write a Python function to calculate factorial",
    system="You are an expert Python developer."
)
print(response)

# Chat that returns JSON only
response = chat_agent_code_json(
    prompt="Create a JSON schema for a user profile",
    agent_type="python"
)
print(response)
```

## Function Signatures

### simple_chat(prompt: str) -> str

Send a prompt to Claude and return the response.

**Parameters:**
- `prompt` (str): The prompt to send to the AI

**Returns:**
- `str`: The AI's response

**Raises:**
- `ValueError`: If ANTHROPIC_API_KEY is not set
- `Exception`: If the API call fails

### chat_agent_code_config(prompt: str, system: str) -> str

Send a prompt to Claude with custom system message and low temperature.
Controls randomness with low temperature (0.0) and uses a higher max token limit (8192).

**Parameters:**
- `prompt` (str): The prompt to send to the AI
- `system` (str): The system message to configure the AI's behavior

**Returns:**
- `str`: The AI's response

**Raises:**
- `ValueError`: If ANTHROPIC_API_KEY is not set
- `Exception`: If the API call fails

### chat_agent_code_json(prompt: str, agent_type: str) -> str

Send a prompt to Claude and get a JSON-only response.
Picks system message based on agent_type.

**Parameters:**
- `prompt` (str): The prompt to send to the AI
- `agent_type` (str): The type of agent - options include:
  - `'python'`: Python code generation assistant
  - `'javascript'`: JavaScript code generation assistant
  - `'data'`: Data structuring assistant
  - `'default'`: Generic code generation assistant

**Returns:**
- `str`: The AI's JSON response

**Raises:**
- `ValueError`: If ANTHROPIC_API_KEY is not set
- `Exception`: If the API call fails

## Running Tests

```bash
cd tests
chmod +x setup_and_run.sh
./setup_and_run.sh
```

This will create a virtual environment, install dependencies, install the package, and run the tests.

## Model Information

This package uses the `claude-sonnet-4-20250514` model from Anthropic.

## Requirements

- Python >= 3.6
- anthropic >= 0.18.0
- python-dotenv >= 1.0.0 (for environment variable management)
