"""Agent chat functions using DeepSeek LLM."""

import os
from deepseek import DeepSeekAPI
from typing import Tuple


def _count_words(text: str) -> int:
    """
    Count the number of words in a text string.

    Args:
        text: The text to count words in.

    Returns:
        int: The number of words in the text.
    """
    if not text:
        return 0
    return len(text.split())


def simple_chat(prompt: str) -> str:
    """
    Send a prompt to DeepSeek API and return the response.

    Args:
        prompt: The user prompt to send to the API.

    Returns:
        str: The response text from the DeepSeek API.

    Raises:
        ValueError: If API key is not set or prompt is invalid.
        Exception: If API request fails.

    Example:
        >>> response = simple_chat("Hello, how are you?")
        >>> print(response)
    """
    if not prompt or not isinstance(prompt, str):
        raise ValueError("Prompt must be a non-empty string")

    # Get API key from environment
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        raise ValueError(
            "DEEPSEEK_API_KEY environment variable is not set. "
            "Please set it with your DeepSeek API key."
        )

    try:
        # Initialize DeepSeek client
        client = DeepSeekAPI(api_key=api_key)
        
        # Send chat completion request
        response = client.chat_completion(
            prompt=prompt,
            model="deepseek-chat",
            temperature=0.7
        )
        
        return response

    except Exception as e:
        raise Exception(f"API request failed: {str(e)}")


def chat_agent_code_json(prompt: str) -> Tuple[str, int, int]:
    """
    Send a prompt to DeepSeek API configured for JSON code generation.
    Sets up agent to respond only with JSON code, sets temperature to low,
    no max token length for coding.

    Args:
        prompt: The user prompt to send to the API.

    Returns:
        Tuple[str, int, int]: A tuple containing:
            - JSON string: The JSON response from the API
            - input_prompt_word_count: Number of words in the input prompt
            - output_prompt_word_count: Number of words in the output JSON response

    Raises:
        ValueError: If API key is not set or prompt is invalid.
        Exception: If API request fails.

    Example:
        >>> json_str, input_count, output_count = chat_agent_code_json("Generate a JSON object with name and age")
        >>> print(json_str)
    """
    if not prompt or not isinstance(prompt, str):
        raise ValueError("Prompt must be a non-empty string")

    # Count input prompt words
    input_prompt_word_count = _count_words(prompt)

    # Get API key from environment
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        raise ValueError(
            "DEEPSEEK_API_KEY environment variable is not set. "
            "Please set it with your DeepSeek API key."
        )

    # System message to enforce JSON-only responses
    system_message = (
        "You are a code generation assistant. "
        "You must respond ONLY with valid JSON code. "
        "Do not include any explanations, markdown code blocks, or text outside the JSON structure. "
        "Your entire response must be parseable as JSON."
    )

    # Enhance user prompt to request JSON
    json_prompt = f"{prompt}\n\nRespond with valid JSON only. No markdown, no explanations."

    try:
        # Initialize DeepSeek client
        client = DeepSeekAPI(api_key=api_key)
        
        # Send chat completion request with system message
        # Combine system message and user prompt
        full_prompt = f"{system_message}\n\nUser: {json_prompt}"
        
        response = client.chat_completion(
            prompt=full_prompt,
            model="deepseek-coder",
            temperature=0.1  # Low temperature for deterministic code generation
        )

        # Clean up response if it contains markdown code blocks
        content = response.strip()
        if content.startswith("```json"):
            content = content[7:]
        elif content.startswith("```"):
            content = content[3:]

        if content.endswith("```"):
            content = content[:-3]

        json_string = content.strip()

        # Count output words
        output_prompt_word_count = _count_words(json_string)

        return json_string, input_prompt_word_count, output_prompt_word_count

    except Exception as e:
        raise Exception(f"API request failed: {str(e)}")

