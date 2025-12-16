"""
Chat agent code JSON function - Responds only with JSON code; picks system based on agent_type.
"""

import os
import json
import re
from anthropic import Anthropic


def _get_system_message(agent_type: str) -> str:
    """
    Get system message based on agent_type.

    Args:
        agent_type: The type of agent (e.g., 'code', 'data', 'analysis').

    Returns:
        The system message for the specified agent type.
    """
    system_messages = {
        "code": "You are a code generation assistant. Always respond with valid JSON only. Your responses must be valid JSON objects.",
        "data": "You are a data processing assistant. Always respond with valid JSON only. Your responses must be valid JSON objects.",
        "analysis": "You are a code analysis assistant. Always respond with valid JSON only. Your responses must be valid JSON objects.",
        "default": "You are a helpful assistant. Always respond with valid JSON only. Your responses must be valid JSON objects."
    }
    return system_messages.get(agent_type.lower(), system_messages["default"])


def _strip_markdown_code_fences(text: str) -> str:
    """
    Strip markdown code fences (```json ... ``` or ``` ... ```) from text.
    
    Args:
        text: The text that may contain markdown code fences.
        
    Returns:
        The text with markdown code fences removed.
    """
    # Remove markdown code fences (```json, ```, etc.)
    text = re.sub(r'^```(?:json)?\s*\n', '', text, flags=re.MULTILINE)
    text = re.sub(r'\n```\s*$', '', text, flags=re.MULTILINE)
    return text.strip()


def chat_agent_code_json(prompt: str, agent_type: str = "code") -> dict:
    """
    Send a prompt to the LLM agent and return JSON response.
    Picks system message based on agent_type.

    Args:
        prompt: The text prompt to send to the agent.
        agent_type: The type of agent ('code', 'data', 'analysis', or 'default').

    Returns:
        A dictionary parsed from the JSON response.

    Example:
        >>> response = chat_agent_code_json("Generate a function signature", "code")
        >>> print(response)
        {'function': 'def example():', 'description': '...'}
    """
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY environment variable is not set")

    client = Anthropic(api_key=api_key)
    system_message = _get_system_message(agent_type)

    response = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=4096,
        system=system_message,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.1,  # Low temperature for deterministic responses
    )

    response_text = response.content[0].text
    
    # Strip markdown code fences if present
    response_text = _strip_markdown_code_fences(response_text)
    
    try:
        return json.loads(response_text)
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse JSON response: {e}. Response was: {response_text}")

