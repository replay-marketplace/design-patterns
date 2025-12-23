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


# System prompts for different agent types
SYSTEM_PROMPTS = {
    "python": "You are an expert Python code generator. Generate clean, efficient, and well-documented Python code. Always follow PEP 8 style guidelines.",
    "javascript": "You are an expert JavaScript code generator. Generate modern, clean JavaScript/TypeScript code following best practices.",
    "java": "You are an expert Java code generator. Generate clean, object-oriented Java code following Java conventions.",
    "cpp": "You are an expert C++ code generator. Generate efficient, modern C++ code following best practices.",
    "general": "You are an expert code generator. Generate clean, efficient, and well-documented code in the requested programming language.",
    "json": "You are a code generator that responds ONLY with valid JSON. Never include explanations, markdown formatting, or any text outside the JSON structure.",
}


def get_system_prompt(agent_type: str) -> str:
    """Get system prompt based on agent type"""
    return SYSTEM_PROMPTS.get(agent_type.lower(), SYSTEM_PROMPTS["general"])
