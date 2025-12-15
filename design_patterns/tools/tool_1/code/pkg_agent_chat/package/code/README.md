# pkg_agent_chat

A Python package with agent chat utilities.

## Installation

```bash
pip install -e .
```

## Function Signatures

### Basic

- `simple_chat(prompt: str) -> str` - Send prompt, return response
- `chat_agent_code_config(prompt, system) -> str` - Control randomness, low temp, no max token
- `chat_agent_code_json(prompt, agent_type)` - Responds only with JSON code; picks system based on agent_type

