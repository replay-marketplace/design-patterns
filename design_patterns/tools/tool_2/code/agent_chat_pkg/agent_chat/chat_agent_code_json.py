"""Chat agent code JSON function - Sets up agent to respond only with JSON code."""

import os
import requests
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
        requests.RequestException: If API request fails.

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

    # DeepSeek API endpoint
    url = "https://api.deepseek.com/v1/chat/completions"

    # Prepare headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # System message to enforce JSON-only responses
    system_message = (
        "You are a code generation assistant. "
        "You must respond ONLY with valid JSON code. "
        "Do not include any explanations, markdown code blocks, or text outside the JSON structure. "
        "Your entire response must be parseable as JSON."
    )

    # Enhance user prompt to request JSON
    json_prompt = f"{prompt}\n\nRespond with valid JSON only. No markdown, no explanations."

    # Prepare payload with low temperature and no max_tokens limit
    payload = {
        "model": "deepseek-coder",
        "messages": [
            {
                "role": "system",
                "content": system_message
            },
            {
                "role": "user",
                "content": json_prompt
            }
        ],
        "temperature": 0.1  # Low temperature for deterministic code generation
        # No max_tokens specified to allow full response
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=120)
        response.raise_for_status()

        data = response.json()
        content = data["choices"][0]["message"]["content"]

        # Clean up response if it contains markdown code blocks
        content = content.strip()
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

    except requests.RequestException as e:
        raise requests.RequestException(f"API request failed: {str(e)}")
    except (KeyError, IndexError) as e:
        raise ValueError(f"Unexpected API response format: {str(e)}")
