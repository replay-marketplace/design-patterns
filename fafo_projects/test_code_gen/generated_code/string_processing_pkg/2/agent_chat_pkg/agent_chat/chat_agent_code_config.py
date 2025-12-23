"""
chat_agent_code_config function - Control randomness with low temperature and no max token limit.
"""

import os
from anthropic import Anthropic


def chat_agent_code_config(prompt: str, system: str) -> str:
    """
    Send a prompt to Anthropic AI with custom system message and low temperature.
    Configured for code generation with low randomness and high token limit.
    
    Args:
        prompt (str): The prompt to send to the AI.
        system (str): The system message to set the AI's behavior.
    
    Returns:
        str: The AI's response.
    
    Raises:
        ValueError: If ANTHROPIC_API_KEY is not set.
        Exception: If the API call fails.
    """
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY environment variable is not set")
    
    client = Anthropic(api_key=api_key)
    
    try:
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=8192,  # High token limit for code generation
            temperature=0.0,  # Low temperature for deterministic output
            system=system,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        return message.content[0].text
    except Exception as e:
        raise Exception(f"Error calling Anthropic API: {str(e)}")
