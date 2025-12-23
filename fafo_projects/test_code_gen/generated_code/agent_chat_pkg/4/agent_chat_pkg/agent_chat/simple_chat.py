"""Simple chat function for DeepSeek API"""

import requests
from typing import Optional
from .config import DeepSeekConfig


def simple_chat(prompt: str, model: Optional[str] = None) -> str:
    """
    Send a prompt to DeepSeek API and return the response.
    
    Args:
        prompt: The user prompt to send
        model: Optional model name (defaults to deepseek-coder for code generation)
    
    Returns:
        str: The response from the API
    
    Raises:
        ValueError: If API key is not set
        requests.RequestException: If API request fails
    """
    model = model or DeepSeekConfig.CODE_MODEL
    
    url = DeepSeekConfig.get_full_url()
    headers = DeepSeekConfig.get_headers()
    
    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=60)
        response.raise_for_status()
        
        data = response.json()
        return data["choices"][0]["message"]["content"]
    
    except requests.RequestException as e:
        raise requests.RequestException(f"API request failed: {str(e)}")
    except (KeyError, IndexError) as e:
        raise ValueError(f"Unexpected API response format: {str(e)}")
