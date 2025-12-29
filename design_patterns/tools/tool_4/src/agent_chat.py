"""Agent chat functions using DeepSeek LLM."""

import os
from deepseek import DeepSeekAPI
from typing import Tuple
from anthropic import Anthropic


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


def simple_chat_anthropic(prompt: str) -> str:
    """
    Send a prompt to Anthropic API and return the response.

    Args:
        prompt: The user prompt to send to the API.

    Returns:
        str: The response text from the Anthropic API.

    Raises:
        ValueError: If API key is not set or prompt is invalid.
        Exception: If API request fails.

    Example:
        >>> response = simple_chat_anthropic("Hello, how are you?")
        >>> print(response)
    """
    if not prompt or not isinstance(prompt, str):
        raise ValueError("Prompt must be a non-empty string")

    # Get API key from environment
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError(
            "ANTHROPIC_API_KEY environment variable is not set. "
            "Please set it with your Anthropic API key."
        )

    try:
        # Initialize Anthropic client
        client = Anthropic(api_key=api_key)
        
        # Send chat completion request
        message = client.messages.create(
            model="claude-opus-4-5-20251101",
            max_tokens=1024,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        # Extract text content from response
        response_text = message.content[0].text
        return response_text

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
    print("[DEBUG] chat_agent_code_json: Function called")
    print(f"[DEBUG] chat_agent_code_json: Input prompt length: {len(prompt) if prompt else 0} chars")
    
    if not prompt or not isinstance(prompt, str):
        print("[DEBUG] chat_agent_code_json: ERROR - Invalid prompt")
        raise ValueError("Prompt must be a non-empty string")

    # Count input prompt words
    input_prompt_word_count = _count_words(prompt)
    print(f"[DEBUG] chat_agent_code_json: Input prompt word count: {input_prompt_word_count}")

    # Get API key from environment
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        print("[DEBUG] chat_agent_code_json: ERROR - DEEPSEEK_API_KEY not set")
        raise ValueError(
            "DEEPSEEK_API_KEY environment variable is not set. "
            "Please set it with your DeepSeek API key."
        )
    print(f"[DEBUG] chat_agent_code_json: API key found (length: {len(api_key)} chars)")

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
        print("[DEBUG] chat_agent_code_json: Initializing DeepSeek client...")
        # Initialize DeepSeek client
        client = DeepSeekAPI(api_key=api_key)
        print("[DEBUG] chat_agent_code_json: Client initialized successfully")
        
        # Send chat completion request with system message
        # Combine system message and user prompt
        full_prompt = f"{system_message}\n\nUser: {json_prompt}"
        print(f"[DEBUG] chat_agent_code_json: Full prompt length: {len(full_prompt)} chars")
        print(f"[DEBUG] chat_agent_code_json: Sending request to API (model: deepseek-coder, temperature: 0.1)...")
        
        response = client.chat_completion(
            prompt=full_prompt,
            model="deepseek-coder",
            temperature=0.1  # Low temperature for deterministic code generation
        )

        print(f"[DEBUG] chat_agent_code_json: Received response (type: {type(response)}, length: {len(str(response)) if response else 0} chars)")
        print(f"[DEBUG] chat_agent_code_json: Raw response preview (first 200 chars): {str(response)[:200] if response else 'None'}")

        # Clean up response if it contains markdown code blocks
        content = response.strip()
        print(f"[DEBUG] chat_agent_code_json: After strip, content length: {len(content)} chars")
        
        if content.startswith("```json"):
            print("[DEBUG] chat_agent_code_json: Removing ```json prefix")
            content = content[7:]
        elif content.startswith("```"):
            print("[DEBUG] chat_agent_code_json: Removing ``` prefix")
            content = content[3:]

        if content.endswith("```"):
            print("[DEBUG] chat_agent_code_json: Removing ``` suffix")
            content = content[:-3]

        json_string = content.strip()
        print(f"[DEBUG] chat_agent_code_json: Final JSON string length: {len(json_string)} chars")
        print(f"[DEBUG] chat_agent_code_json: Final JSON string preview (first 200 chars): {json_string[:200]}")

        # Count output words
        output_prompt_word_count = _count_words(json_string)
        print(f"[DEBUG] chat_agent_code_json: Output word count: {output_prompt_word_count}")
        print(f"[DEBUG] chat_agent_code_json: Returning result")
        print(f"[RESPONSE] chat_agent_code_json: Full response string:\n{json_string}")

        return json_string, input_prompt_word_count, output_prompt_word_count

    except Exception as e:
        print(f"[DEBUG] chat_agent_code_json: EXCEPTION occurred: {type(e).__name__}: {str(e)}")
        raise Exception(f"API request failed: {str(e)}")


def chat_agent_code_json_anthropic(prompt: str) -> Tuple[str, int, int]:
    """
    Send a prompt to Anthropic API configured for JSON code generation.
    Sets up agent to respond only with JSON code, sets temperature to low,
    higher max token length for coding.

    Args:
        prompt: The user prompt to send to the API.

    Returns:
        Tuple[str, int, int]: A tuple containing:
            - JSON string: The JSON response from the API
            - input_prompt_word_count: Number of words in the input prompt
            - output_prompt_word_count: Number of words in the output JSON response

    Raises:
        ValueError: If API key is not set or prompt is invalid.
        Exception: If API request failed.

    Example:
        >>> json_str, input_count, output_count = chat_agent_code_json_anthropic("Generate a JSON object with name and age")
        >>> print(json_str)
    """
    if not prompt or not isinstance(prompt, str):
        raise ValueError("Prompt must be a non-empty string")

    # Count input prompt words
    input_prompt_word_count = _count_words(prompt)

    # Get API key from environment
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError(
            "ANTHROPIC_API_KEY environment variable is not set. "
            "Please set it with your Anthropic API key."
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
        # Initialize Anthropic client
        client = Anthropic(api_key=api_key)
        
        # Send chat completion request with system message
        message = client.messages.create(
            model="claude-opus-4-5-20251101",
            max_tokens=16000,  # Higher max tokens for code generation
            temperature=0.1,  # Low temperature for deterministic code generation
            system=system_message,
            messages=[
                {"role": "user", "content": json_prompt}
            ]
        )
        
        # Extract text content from response
        response_text = message.content[0].text

        # Clean up response if it contains markdown code blocks
        content = response_text.strip()
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

