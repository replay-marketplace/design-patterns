"""Chat agent with configurable parameters for code generation"""

import requests
from typing import Optional
from .config import DeepSeekConfig


def chat_agent_code_config(
    prompt: str,
    system: str,
    model: Optional[str] = None,
    temperature: float = 0.2
) -> str:
    """
    Send a prompt with custom system message and controlled randomness.
    Configured for code generation with low temperature and no max token limit.
    
    Args:
        prompt: The user prompt to send
        system: The system message to set context/behavior
        model: Optional model name (defaults to deepseek-coder)
        temperature: Temperature for response randomness (default: 0.2 for deterministic code)
    
    Returns:
        str: The response from the API
    
    Raises:
        ValueError: If API key is not set or invalid parameters
        requests.RequestException: If API request fails
    """
    if not prompt or not isinstance(prompt, str):
        raise ValueError("Prompt must be a non-empty string")
    
    if not system or not isinstance(system, str):
        raise ValueError("System message must be a non-empty string")
    
    if not 0 <= temperature <= 2:
        raise ValueError("Temperature must be between 0 and 2")
    
    model = model or DeepSeekConfig.CODE_MODEL
    
    url = DeepSeekConfig.get_full_url()
    headers = DeepSeekConfig.get_headers()
    
    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": system
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": temperature,
        # No max_tokens specified to allow full responses
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=120)
        response.raise_for_status()
        
        data = response.json()
        return data["choices"][0]["message"]["content"]
    
    except requests.RequestException as e:
        raise requests.RequestException(f"API request failed: {str(e)}")
    except (KeyError, IndexError) as e:
        raise ValueError(f"Unexpected API response format: {str(e)}")
