# API Signature

## Agent Chat Functions

### Basic Functions:
- `simple_chat(prompt: str) -> str` - Send prompt, return response
- `chat_agent_code_config(prompt: str, system: str) -> str` - Control randomness, low temp, no max token
- `chat_agent_code_json(prompt: str, agent_type: str) -> str` - Responds only with JSON code; picks system based on agent_type

### Description
Use DeepSeek API, set it up for code generation.

### Environment Variables
- `DEEPSEEK_API_KEY` - Your DeepSeek API key (required)
