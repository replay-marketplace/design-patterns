"""Configuration module for DeepSeek API"""

import os
from typing import Optional


class DeepSeekConfig:
    """Configuration for DeepSeek API"""
    
    API_BASE_URL = "https://api.deepseek.com/v1"
    CHAT_ENDPOINT = "/chat/completions"
    DEFAULT_MODEL = "deepseek-chat"
    CODE_MODEL = "deepseek-coder"
    
    @staticmethod
    def get_api_key() -> str:
        """Get API key from environment variable"""
        api_key = os.getenv("DEEPSEEK_API_KEY")
        if not api_key:
            raise ValueError(
                "DEEPSEEK_API_KEY environment variable is not set. "
                "Please set it with your DeepSeek API key."
            )
        return api_key
    
    @staticmethod
    def get_headers() -> dict:
        """Get headers for API requests"""
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {DeepSeekConfig.get_api_key()}"
        }
    
    @staticmethod
    def get_full_url(endpoint: Optional[str] = None) -> str:
        """Get full API URL"""
        endpoint = endpoint or DeepSeekConfig.CHAT_ENDPOINT
        return f"{DeepSeekConfig.API_BASE_URL}{endpoint}"
