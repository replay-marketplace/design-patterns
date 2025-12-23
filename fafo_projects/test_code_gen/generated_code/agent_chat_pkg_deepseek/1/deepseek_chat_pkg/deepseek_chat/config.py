"""Configuration settings for DeepSeek Chat package."""

import os

# Default API endpoint
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"

# Default model for code generation
DEFAULT_MODEL = "deepseek-coder"

# Default temperature for code generation
DEFAULT_TEMPERATURE = 0.7

# Default max tokens
DEFAULT_MAX_TOKENS = 2048

# Request timeout in seconds
REQUEST_TIMEOUT = 30

# System prompt for code generation
CODE_GENERATION_SYSTEM_PROMPT = (
    "You are an expert code generation assistant. "
    "Provide clear, efficient, and well-documented code solutions."
)


def get_api_key() -> str:
    """Get API key from environment variable."""
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        raise ValueError(
            "DEEPSEEK_API_KEY environment variable not set. "
            "Please set it with your DeepSeek API key."
        )
    return api_key
