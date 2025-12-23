# API Signature

## Basic Functions

- `simple_chat(prompt: str) -> str` - Send prompt, return response
- `chat_agent_code_config(prompt: str, system: str) -> str` - Control randomness, low temp, no max token
- `chat_agent_code_json(prompt: str, agent_type: str) -> str` - Responds only with JSON code; picks system based on agent_type

## Description

This package provides chat agent functions using Anthropic AI with Claude Sonnet 4.5 model.
All functions use `model="claude-sonnet-4-5-20250929"` with max tokens set to 16k.
