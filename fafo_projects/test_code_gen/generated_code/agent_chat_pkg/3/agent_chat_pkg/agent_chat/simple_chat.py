"""Simple chat function using Anthropic AI"""

import os
from anthropic import Anthropic

MODEL = "claude-sonnet-4-5-20250929"
MAX_TOKENS = 16000


def simple_chat(prompt: str) -> str:
    """
    Send a prompt to Claude and return the response.
    
    Args:
        prompt: The user prompt to send to the AI
        
    Returns:
        The AI's response as a string
        
    Raises:
        ValueError: If prompt is empty
        Exception: If API call fails
    """
    if not prompt or not prompt.strip():
        raise ValueError("Prompt cannot be empty")
    
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY environment variable not set")
    
    client = Anthropic(api_key=api_key)
    
    try:
        message = client.messages.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        return message.content[0].text
    except Exception as e:
        raise Exception(f"Error calling Anthropic API: {str(e)}")
