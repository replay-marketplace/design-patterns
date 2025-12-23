"""
Package Agent Chat - A Python package for interacting with DeepSeek LLM agent.

This package provides functions for chat interactions with the DeepSeek API.
"""

from .simple_chat import simple_chat
from .chat_agent_code_json import chat_agent_code_json

__version__ = "0.1.0"
__all__ = [
    "simple_chat",
    "chat_agent_code_json",
]
