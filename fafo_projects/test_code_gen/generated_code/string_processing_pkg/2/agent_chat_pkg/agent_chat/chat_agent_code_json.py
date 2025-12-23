"""
chat_agent_code_json function - Responds only with JSON code based on agent type.
"""

import os
from anthropic import Anthropic


# System prompts for different agent types
AGENT_SYSTEMS = {
    "code_generator": "You are a code generation assistant. Always respond with valid JSON only. Your responses must be valid JSON objects containing code or structured data.",
    "data_generator": "You are a data generation assistant. Always respond with valid JSON only. Generate structured data in JSON format based on the user's request.",
    "api_designer": "You are an API design assistant. Always respond with valid JSON only. Your responses must be valid JSON objects representing API specifications, endpoints, or schemas.",
    "config_generator": "You are a configuration generation assistant. Always respond with valid JSON only. Generate configuration files and settings in valid JSON format.",
    "default": "You are a helpful assistant. Always respond with valid JSON only. Your responses must be valid JSON objects."
}


def chat_agent_code_json(prompt: str, agent_type: str) -> str:
    """
    Send a prompt to Anthropic AI and receive a JSON-only response.
    The system message is selected based on the agent_type parameter.
    
    Args:
        prompt (str): The prompt to send to the AI.
        agent_type (str): The type of agent to use. Options: 'code_generator', 
                         'data_generator', 'api_designer', 'config_generator', or 'default'.
    
    Returns:
        str: The AI's response in JSON format.
    
    Raises:
        ValueError: If ANTHROPIC_API_KEY is not set or agent_type is invalid.
        Exception: If the API call fails.
    """
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY environment variable is not set")
    
    # Get system message based on agent type
    system_message = AGENT_SYSTEMS.get(agent_type)
    if not system_message:
        # If agent_type not found, use default
        system_message = AGENT_SYSTEMS["default"]
    
    client = Anthropic(api_key=api_key)
    
    try:
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=8192,
            temperature=0.0,  # Low temperature for consistent JSON output
            system=system_message,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        return message.content[0].text
    except Exception as e:
        raise Exception(f"Error calling Anthropic API: {str(e)}")
