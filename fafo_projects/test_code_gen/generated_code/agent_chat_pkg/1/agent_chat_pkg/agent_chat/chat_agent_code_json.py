"""
chat_agent_code_json function.
"""

import os
from anthropic import Anthropic


# System prompts for different agent types
SYSTEM_PROMPTS = {
    "python": "You are a Python code generation assistant. Always respond with valid JSON only. Your responses must be valid JSON objects containing code or data structures.",
    "javascript": "You are a JavaScript code generation assistant. Always respond with valid JSON only. Your responses must be valid JSON objects containing code or data structures.",
    "data": "You are a data structuring assistant. Always respond with valid JSON only. Your responses must be valid JSON objects.",
    "default": "You are a code generation assistant. Always respond with valid JSON only. Your responses must be valid JSON objects."
}


def chat_agent_code_json(prompt: str, agent_type: str) -> str:
    """
    Send a prompt to Claude and get a JSON-only response.
    Picks system message based on agent_type.
    
    Args:
        prompt: The prompt to send to the AI
        agent_type: The type of agent (e.g., 'python', 'javascript', 'data', 'default')
    
    Returns:
        str: The AI's JSON response
    
    Raises:
        ValueError: If ANTHROPIC_API_KEY is not set
        Exception: If the API call fails
    """
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY environment variable is not set")
    
    # Select system prompt based on agent_type
    system_prompt = SYSTEM_PROMPTS.get(agent_type.lower(), SYSTEM_PROMPTS["default"])
    
    client = Anthropic(api_key=api_key)
    
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=8192,
        temperature=0.0,
        system=system_prompt,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    return message.content[0].text
