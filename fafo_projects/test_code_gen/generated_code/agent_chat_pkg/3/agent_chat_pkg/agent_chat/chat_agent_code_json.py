"""Chat agent that responds only with JSON code"""

import os
from anthropic import Anthropic

MODEL = "claude-sonnet-4-5-20250929"
MAX_TOKENS = 16000

# System messages for different agent types
SYSTEM_MESSAGES = {
    "python": "You are a Python code generation assistant. Always respond with valid JSON only. Your responses must be valid JSON objects that can be parsed. Do not include any explanatory text outside the JSON structure.",
    "javascript": "You are a JavaScript code generation assistant. Always respond with valid JSON only. Your responses must be valid JSON objects that can be parsed. Do not include any explanatory text outside the JSON structure.",
    "data": "You are a data analysis assistant. Always respond with valid JSON only. Your responses must be valid JSON objects that can be parsed. Do not include any explanatory text outside the JSON structure.",
    "general": "You are a code generation assistant. Always respond with valid JSON only. Your responses must be valid JSON objects that can be parsed. Do not include any explanatory text outside the JSON structure.",
}


def chat_agent_code_json(prompt: str, agent_type: str) -> str:
    """
    Send a prompt and receive a JSON-only response.
    Picks system message based on agent_type.
    
    Args:
        prompt: The user prompt to send to the AI
        agent_type: The type of agent (e.g., 'python', 'javascript', 'data', 'general')
        
    Returns:
        The AI's response as a JSON string
        
    Raises:
        ValueError: If prompt is empty or agent_type is invalid
        Exception: If API call fails
    """
    if not prompt or not prompt.strip():
        raise ValueError("Prompt cannot be empty")
    
    if not agent_type or not agent_type.strip():
        raise ValueError("Agent type cannot be empty")
    
    # Get system message based on agent_type, default to 'general' if not found
    system_message = SYSTEM_MESSAGES.get(agent_type.lower(), SYSTEM_MESSAGES["general"])
    
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY environment variable not set")
    
    client = Anthropic(api_key=api_key)
    
    try:
        message = client.messages.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            temperature=0.3,  # Low temperature for consistent JSON output
            system=system_message,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        response_text = message.content[0].text.strip()
        
        # Clean up response to ensure it's pure JSON
        # Remove markdown code blocks if present
        if response_text.startswith("```"):
            lines = response_text.split("\n")
            # Remove first line (```json or ```)
            lines = lines[1:]
            # Remove last line (```)
            if lines and lines[-1].strip() == "```":
                lines = lines[:-1]
            response_text = "\n".join(lines).strip()
        
        return response_text
    except Exception as e:
        raise Exception(f"Error calling Anthropic API: {str(e)}")
