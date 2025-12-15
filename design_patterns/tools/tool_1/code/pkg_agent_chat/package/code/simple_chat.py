"""
Simple chat function - Send prompt, return response.
"""

import os
from openai import OpenAI


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
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable is not set")

    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

