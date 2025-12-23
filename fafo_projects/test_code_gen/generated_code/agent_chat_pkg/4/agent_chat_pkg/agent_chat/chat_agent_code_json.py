"""Chat agent that responds only with JSON code"""

import requests
from typing import Optional
from .config import DeepSeekConfig, get_system_prompt


def chat_agent_code_json(
    prompt: str,
    agent_type: str,
    model: Optional[str] = None,
    temperature: float = 0.1
) -> str:
    """
    Send a prompt and receive a JSON-only response.
    System message is automatically selected based on agent_type.
    
    Args:
        prompt: The user prompt to send
        agent_type: Type of agent (python, javascript, java, cpp, general, json)
                   Determines the system prompt used
        model: Optional model name (defaults to deepseek-coder)
        temperature: Temperature for response randomness (default: 0.1 for very deterministic)
    
    Returns:
        str: JSON response from the API
    
    Raises:
        ValueError: If API key is not set or invalid parameters
        requests.RequestException: If API request fails
    """
    if not prompt or not isinstance(prompt, str):
        raise ValueError("Prompt must be a non-empty string")
    
    if not agent_type or not isinstance(agent_type, str):
        raise ValueError("Agent type must be a non-empty string")
    
    if not 0 <= temperature <= 2:
        raise ValueError("Temperature must be between 0 and 2")
    
    model = model or DeepSeekConfig.CODE_MODEL
    
    # Get base system prompt for agent type
    base_system = get_system_prompt(agent_type)
    
    # Enhance system prompt to enforce JSON-only responses
    json_system = (
        f"{base_system}\n\n"
        "CRITICAL: You must respond ONLY with valid JSON. "
        "Do not include any explanations, markdown code blocks, or text outside the JSON structure. "
        "Your entire response must be parseable as JSON."
    )
    
    url = DeepSeekConfig.get_full_url()
    headers = DeepSeekConfig.get_headers()
    
    # Enhance user prompt to request JSON
    json_prompt = f"{prompt}\n\nRespond with valid JSON only. No markdown, no explanations."
    
    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": json_system
            },
            {
                "role": "user",
                "content": json_prompt
            }
        ],
        "temperature": temperature,
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
        
        return content.strip()
    
    except requests.RequestException as e:
        raise requests.RequestException(f"API request failed: {str(e)}")
    except (KeyError, IndexError) as e:
        raise ValueError(f"Unexpected API response format: {str(e)}")
