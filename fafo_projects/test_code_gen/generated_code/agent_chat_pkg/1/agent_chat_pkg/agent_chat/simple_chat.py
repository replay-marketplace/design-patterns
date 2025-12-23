"""
simple_chat function.
"""

import os
from anthropic import Anthropic


def simple_chat(prompt: str) -> str:
    """
    Send a prompt to Claude and return the response.
    
    Args:
        prompt: The prompt to send to the AI
    
    Returns:
        str: The AI's response
    
    Raises:
        ValueError: If ANTHROPIC_API_KEY is not set
        Exception: If the API call fails
    """
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY environment variable is not set")
    
    client = Anthropic(api_key=api_key)
    
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    return message.content[0].text
