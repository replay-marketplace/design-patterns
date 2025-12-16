"""
Chat agent code config function - Control randomness, low temp, no max token.
"""

import os
from anthropic import Anthropic


def chat_agent_code_config(prompt: str, system: str) -> str:
    """
    Send a prompt with system message to the LLM agent with controlled randomness.
    Uses low temperature for deterministic code generation and no max token limit.

    Args:
        prompt: The text prompt to send to the agent.
        system: The system message that defines the agent's behavior and context.

    Returns:
        The text response from the agent.

    Example:
        >>> system_msg = "You are a helpful coding assistant."
        >>> response = chat_agent_code_config("Write a hello world function", system_msg)
        >>> print(response)
        'def hello_world():\\n    print("Hello, World!")'
    """
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY environment variable is not set")

    client = Anthropic(api_key=api_key)

    response = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=4096,  # Large max_tokens to allow full response
        system=system,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.1,  # Low temperature for deterministic code generation
    )

    return response.content[0].text

