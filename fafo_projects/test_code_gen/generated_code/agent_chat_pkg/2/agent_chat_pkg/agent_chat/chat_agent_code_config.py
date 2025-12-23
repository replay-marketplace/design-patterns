"""
chat_agent_code_config function.
"""

import os
from anthropic import Anthropic


def chat_agent_code_config(prompt: str, system: str) -> str:
    """
    Send a prompt with custom system message and low temperature.
    Control randomness with low temperature and no max token limit.
    
    Args:
        prompt: The prompt to send to Claude
        system: The system message to configure Claude's behavior
    
    Returns:
        str: The response from Claude
    """
    client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
    
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=16000,
        temperature=0.0,
        system=system,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    return message.content[0].text
