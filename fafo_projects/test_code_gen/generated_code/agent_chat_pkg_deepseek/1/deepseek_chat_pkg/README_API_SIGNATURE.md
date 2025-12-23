# API Signature

`simple_chat(prompt: str) -> str` - Send prompt, return response

## Description

Sends a prompt to the DeepSeek API configured for code generation and returns the response.

## Parameters

- `prompt` (str): The prompt to send to the DeepSeek API

## Returns

- `str`: The response from the DeepSeek API

## Example

```python
from deepseek_chat import simple_chat

response = simple_chat("Write a Python function to reverse a string")
print(response)
```
