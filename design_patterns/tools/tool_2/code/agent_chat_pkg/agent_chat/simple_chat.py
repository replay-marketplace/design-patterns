"""Simple chat function - Send prompt, return response."""

import os
import requests
from typing import Optional


def simple_chat(prompt: str) -> str:
    """
    Send a prompt to DeepSeek API and return the response.

    Args:
        prompt: The user prompt to send to the API.

    Returns:
        str: The response text from the DeepSeek API.

    Raises:
        ValueError: If API key is not set or prompt is invalid.
        requests.RequestException: If API request fails.

    Example:
        >>> response = simple_chat("Hello, how are you?")
        >>> print(response)
    """
    if not prompt or not isinstance(prompt, str):
        raise ValueError("Prompt must be a non-empty string")

    # Get API key from environment
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        raise ValueError(
            "DEEPSEEK_API_KEY environment variable is not set. "
            "Please set it with your DeepSeek API key."
        )

    # DeepSeek API endpoint
    url = "https://api.deepseek.com/v1/chat/completions"

    # Prepare headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # Prepare payload
    payload = {
        "model": "deepseek-chat",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.7
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
