"""
Agent Chat Module

Provides functions for interacting with DeepSeek LLM agent.
"""

import os
from deepseek import DeepSeekAPI


def _count_words(text: str) -> int:
    """Count the number of words in a text string."""
    if not text:
        return 0
    return len(text.split())


def simple_chat(prompt: str) -> str:
    """
    Send a prompt to the LLM agent and return the response.
    
    Args:
        prompt: The user prompt to send to the agent
        
    Returns:
        The response string from the agent
    """
    api_key = os.environ.get('DEEPSEEK_API_KEY')
    if not api_key:
        raise ValueError("DEEPSEEK_API_KEY environment variable is not set")
    
    client = DeepSeekAPI(api_key=api_key)
    response = client.chat_completion(prompt=prompt, stream=False)
    return response


def chat_agent_code_json(prompt: str) -> tuple[str, int, int]:
    """
    Set up agent to respond only with JSON code.
    Sets temperature to low, no max token length for coding.
    
    Args:
        prompt: The user prompt to send to the agent
        
    Returns:
        A tuple containing:
        - JSON string response from the agent
        - Input prompt word count
        - Output prompt word count
    """
    api_key = os.environ.get('DEEPSEEK_API_KEY')
    if not api_key:
        raise ValueError("DEEPSEEK_API_KEY environment variable is not set")
    
    # Count input words
    input_prompt_word_count = _count_words(prompt)
    
    # Set up system prompt to ensure JSON-only responses
    system_prompt = "You are a coding assistant. Respond ONLY with valid JSON code. Do not include any markdown formatting, explanations, or text outside of the JSON structure."
    
    client = DeepSeekAPI(api_key=api_key)
    
    # Configure for JSON code generation:
    # - temperature: 0 (low temperature for coding)
    # - max_tokens: Maximum allowed (8192) for coding tasks
    # - response_format: JSON
    response = client.chat_completion(
        prompt=prompt,
        prompt_sys=system_prompt,
        stream=False,
        temperature=0,
        response_format={"type": "json_object"}
    )
    
    # Count output words
    output_prompt_word_count = _count_words(response)
    
    return response, input_prompt_word_count, output_prompt_word_count

