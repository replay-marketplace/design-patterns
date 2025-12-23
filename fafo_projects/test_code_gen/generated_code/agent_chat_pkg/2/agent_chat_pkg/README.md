# agent_chat Package

A Python package for interacting with Anthropic's Claude AI for chat and code generation tasks.

## Installation

```bash
cd agent_chat_pkg
pip install -e .
```

## Setup

You need to set your Anthropic API key as an environment variable:

```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

Or create a `.env` file:

```
ANTHROPIC_API_KEY=your-api-key-here
```

## Usage

```python
from agent_chat import simple_chat, chat_agent_code_config, chat_agent_code_json

# Simple chat
response = simple_chat("What is Python?")
print(response)

# Chat with custom system message and low temperature
system_msg = "You are a helpful coding assistant."
response = chat_agent_code_config(
    "Write a function to calculate factorial",
    system_msg
)
print(response)

# Get JSON-only response
response = chat_agent_code_json(
    "Create a JSON object representing a user profile",
    "json_generator"
)
print(response)
```

## Function Signatures

### simple_chat(prompt: str) -> str

Send a prompt to Claude and return the response.

**Parameters:**
- `prompt` (str): The prompt to send to Claude

**Returns:**
- `str`: The response from Claude

**Model Configuration:**
- Model: claude-sonnet-4-20250514
- Max tokens: 16,000

### chat_agent_code_config(prompt: str, system: str) -> str

Send a prompt with custom system message and low temperature for more deterministic responses.

**Parameters:**
- `prompt` (str): The prompt to send to Claude
- `system` (str): The system message to configure Claude's behavior

**Returns:**
- `str`: The response from Claude

**Model Configuration:**
- Model: claude-sonnet-4-20250514
- Max tokens: 16,000
- Temperature: 0.0 (low randomness)

### chat_agent_code_json(prompt: str, agent_type: str) -> str

Send a prompt and get a JSON-only response. The system message is automatically selected based on the agent_type.

**Parameters:**
- `prompt` (str): The prompt to send to Claude
- `agent_type` (str): The type of agent (determines system message)
  - `"json_generator"`: For JSON generation tasks
  - `"code_generator"`: For code generation tasks
  - `"data_processor"`: For data processing tasks
  - `"default"`: Default JSON assistant

**Returns:**
- `str`: The JSON response from Claude

**Model Configuration:**
- Model: claude-sonnet-4-20250514
- Max tokens: 16,000
- Temperature: 0.0 (low randomness)

## Running Tests

```bash
cd tests
chmod +x setup_and_run.sh
./setup_and_run.sh
```

This will create a virtual environment, install dependencies, install the package, and run the tests.

## Requirements

- Python >= 3.7
- anthropic >= 0.18.0
- python-dotenv >= 1.0.0 (optional, for .env file support)

## License

MIT
