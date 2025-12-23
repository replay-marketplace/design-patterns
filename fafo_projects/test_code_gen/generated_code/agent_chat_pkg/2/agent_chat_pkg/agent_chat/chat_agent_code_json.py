"""
chat_agent_code_json function.
"""

import os
from anthropic import Anthropic


AGENT_SYSTEMS = {
    "json_generator": "You are a JSON code generation assistant. Always respond with valid JSON only. Your responses must be valid JSON objects.",
    "code_generator": "You are a code generation assistant. Always respond with valid JSON only. Your responses must be valid JSON objects containing code.",
    "data_processor": "You are a data processing assistant. Always respond with valid JSON only. Your responses must be valid JSON objects.",
    "default": "You are a helpful assistant. Always respond with valid JSON only. Your responses must be valid JSON objects."
}


def chat_agent_code_json(prompt: str, agent_type: str) -> str:
    """
    Send a prompt and get a JSON-only response.
    Picks system message based on agent_type.
    
    Args:
        prompt: The prompt to send to Claude
        agent_type: The type of agent (determines system message)
    
    Returns:
        str: The JSON response from Claude
    """
    client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
    
    # Get system message based on agent_type, default to "default" if not found
    system_message = AGENT_SYSTEMS.get(agent_type, AGENT_SYSTEMS["default"])
    
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=16000,
        temperature=0.0,
        system=system_message,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    return message.content[0].text
