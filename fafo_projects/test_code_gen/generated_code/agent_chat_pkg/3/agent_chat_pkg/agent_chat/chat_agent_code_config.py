"""Chat agent with configurable system message and low temperature"""

import os
from anthropic import Anthropic

MODEL = "claude-sonnet-4-5-20250929"
# No max_tokens limit as per requirements


def chat_agent_code_config(prompt: str, system: str) -> str:
    """
    Send a prompt with a custom system message and low temperature.
    Controls randomness with low temperature and no max token limit.
    
    Args:
        prompt: The user prompt to send to the AI
        system: The system message to configure the AI's behavior
        
    Returns:
        The AI's response as a string
        
    Raises:
        ValueError: If prompt or system is empty
        Exception: If API call fails
    """
    if not prompt or not prompt.strip():
        raise ValueError("Prompt cannot be empty")
    
    if not system or not system.strip():
        raise ValueError("System message cannot be empty")
    
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY environment variable not set")
    
    client = Anthropic(api_key=api_key)
    
    try:
        message = client.messages.create(
            model=MODEL,
            max_tokens=16000,  # Using 16k as specified in description
            temperature=0.2,  # Low temperature for more deterministic output
            system=system,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        return message.content[0].text
    except Exception as e:
        raise Exception(f"Error calling Anthropic API: {str(e)}")
