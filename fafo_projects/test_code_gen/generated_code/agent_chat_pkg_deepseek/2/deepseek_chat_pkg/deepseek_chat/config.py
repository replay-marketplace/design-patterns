"""Configuration settings for DeepSeek Chat package."""

import os
from typing import Optional


class Config:
    """Configuration class for DeepSeek API settings."""
    
    DEFAULT_MODEL = "deepseek-coder"
    DEFAULT_TEMPERATURE = 0.7
    DEFAULT_MAX_TOKENS = 2048
    DEFAULT_BASE_URL = "https://api.deepseek.com/v1"
    
    @staticmethod
    def get_api_key() -> Optional[str]:
        """Get API key from environment variable.
        
        Returns:
            Optional[str]: The API key if found, None otherwise
        """
        return os.environ.get("DEEPSEEK_API_KEY")
    
    @staticmethod
    def get_base_url() -> str:
        """Get base URL from environment variable or use default.
        
        Returns:
            str: The base URL for the API
        """
        return os.environ.get("DEEPSEEK_BASE_URL", Config.DEFAULT_BASE_URL)
