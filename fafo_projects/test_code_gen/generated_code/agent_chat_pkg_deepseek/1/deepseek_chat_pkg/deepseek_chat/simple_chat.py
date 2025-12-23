"""Simple chat function for DeepSeek API."""

import os
import requests
from typing import Optional


def simple_chat(prompt: str, api_key: Optional[str] = None, model: str = "deepseek-coder") -> str:
    """
    Send a prompt to DeepSeek API and return the response.
    
    This function is configured for code generation tasks.
    
    Args:
        prompt (str): The prompt to send to the DeepSeek API
        api_key (str, optional): DeepSeek API key. If not provided, reads from DEEPSEEK_API_KEY env variable
        model (str, optional): Model to use. Defaults to "deepseek-coder"
    
    Returns:
        str: The response from the DeepSeek API
    
    Raises:
        ValueError: If API key is not provided and not found in environment
        requests.exceptions.RequestException: If API request fails
    
    Example:
        >>> response = simple_chat("Write a Python function to calculate factorial")
        >>> print(response)
    """
    # Get API key from parameter or environment
    if api_key is None:
        api_key = os.environ.get("DEEPSEEK_API_KEY")
    
    if not api_key:
        raise ValueError(
            "DeepSeek API key not provided. "
            "Please set DEEPSEEK_API_KEY environment variable or pass api_key parameter."
        )
    
    # DeepSeek API endpoint
    url = "https://api.deepseek.com/v1/chat/completions"
    
    # Prepare headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    # Prepare payload with system message for code generation
    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": "You are an expert code generation assistant. Provide clear, efficient, and well-documented code solutions."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.7,
        "max_tokens": 2048
    }
    
    try:
        # Make API request
        response = requests.post(url, json=payload, headers=headers, timeout=30)
        response.raise_for_status()
        
        # Parse response
        result = response.json()
        
        # Extract message content
        if "choices" in result and len(result["choices"]) > 0:
            return result["choices"][0]["message"]["content"]
        else:
            raise ValueError("Unexpected API response format")
    
    except requests.exceptions.RequestException as e:
        raise requests.exceptions.RequestException(
            f"Failed to communicate with DeepSeek API: {str(e)}"
        ) from e
