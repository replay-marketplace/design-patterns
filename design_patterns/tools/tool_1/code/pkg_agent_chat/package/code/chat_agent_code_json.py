"""
Chat agent code JSON function - Responds only with JSON code; picks system based on agent_type.
"""

import os
import json
from openai import OpenAI


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
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable is not set")

    client = OpenAI(api_key=api_key)
    system_message = _get_system_message(agent_type)

    # Try with response_format first, fallback if not supported
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ],
            temperature=0.1,  # Low temperature for deterministic responses
            response_format={"type": "json_object"}  # Force JSON response
        )
    except Exception as e:
        # If response_format is not supported, retry without it
        error_str = str(e)
        if "response_format" in error_str.lower() or "json_object" in error_str.lower():
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.1  # Low temperature for deterministic responses
            )
        else:
            raise

    response_text = response.choices[0].message.content
    
    try:
        return json.loads(response_text)
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse JSON response: {e}. Response was: {response_text}")

