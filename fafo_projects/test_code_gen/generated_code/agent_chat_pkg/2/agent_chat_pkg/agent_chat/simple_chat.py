"""
simple_chat function.
"""

import os
from anthropic import Anthropic


def simple_chat(prompt: str) -> str:
    """
    Send a prompt to Claude and return the response.
    
    Args:
        prompt: The prompt to send to Claude
    
    Returns:
        str: The response from Claude
    """
    client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
    
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=16000,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    return message.content[0].text
