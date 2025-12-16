"""
Simple chat function - Send prompt, return response.
"""

import os
from anthropic import Anthropic


def simple_chat(prompt: str) -> str:
    """
    Send a prompt to the LLM agent and return the response.

    Args:
        prompt: The text prompt to send to the agent.

    Returns:
        The text response from the agent.

    Example:
        >>> response = simple_chat("What is Python?")
        >>> print(response)
        'Python is a programming language...'
    """
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY environment variable is not set")

    client = Anthropic(api_key=api_key)

    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.content[0].text

