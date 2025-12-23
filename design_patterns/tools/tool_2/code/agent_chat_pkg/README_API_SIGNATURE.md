# Agent Chat Package

## API Signatures

### Basic

- `simple_chat(prompt: str) -> str` - Send prompt, return response
- `chat_agent_code_json(prompt: str) -> Tuple[str, int, int]` - Sets up agent to respond only with JSON code, sets temperature to low, no max token length for coding. Returns JSON string, input_prompt_word_count, output_prompt_word_count.
