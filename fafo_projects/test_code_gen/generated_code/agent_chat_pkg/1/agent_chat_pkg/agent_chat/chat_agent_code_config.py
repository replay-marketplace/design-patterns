"""
chat_agent_code_config function.
"""

import os
from anthropic import Anthropic


def chat_agent_code_config(prompt: str, system: str) -> str:
    """
    Send a prompt to Claude with custom system message and low temperature.
    Controls randomness with low temperature and no max token limit.
    
    Args:
        prompt: The prompt to send to the AI
        system: The system message to configure the AI's behavior
    
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
        max_tokens=8192,
        temperature=0.0,
        system=system,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    return message.content[0].text
