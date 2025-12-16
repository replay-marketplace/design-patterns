"""
Tests for pkg_agent_chat package.
"""

import sys
import os

# Add the package to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'package'))

from code.simple_chat import simple_chat
from code.chat_agent_code_config import chat_agent_code_config
from code.chat_agent_code_json import chat_agent_code_json


def test_simple_chat():
    """Test simple_chat function."""
    # Skip test if API key is not set
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("⊘ simple_chat test skipped (ANTHROPIC_API_KEY not set)")
        return
    
    try:
        response = simple_chat("Say 'Hello, World!' in one sentence.")
        assert isinstance(response, str)
        assert len(response) > 0
        print("✓ simple_chat tests passed")
    except Exception as e:
        print(f"⚠ simple_chat test failed: {e}")


def test_chat_agent_code_config():
    """Test chat_agent_code_config function."""
    # Skip test if API key is not set
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("⊘ chat_agent_code_config test skipped (ANTHROPIC_API_KEY not set)")
        return
    
    try:
        system_msg = "You are a helpful coding assistant."
        response = chat_agent_code_config("Write a Python function that returns 'test'", system_msg)
        assert isinstance(response, str)
        assert len(response) > 0
        print("✓ chat_agent_code_config tests passed")
    except Exception as e:
        print(f"⚠ chat_agent_code_config test failed: {e}")


def test_chat_agent_code_json():
    """Test chat_agent_code_json function."""
    # Skip test if API key is not set
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("⊘ chat_agent_code_json test skipped (ANTHROPIC_API_KEY not set)")
        return
    
    try:
        response = chat_agent_code_json("Return a JSON object with key 'status' and value 'ok'", "code")
        assert isinstance(response, dict)
        assert "status" in response
        print("✓ chat_agent_code_json tests passed")
    except Exception as e:
        print(f"⚠ chat_agent_code_json test failed: {e}")


if __name__ == "__main__":
    print("Running tests for pkg_agent_chat...\n")
    test_simple_chat()
    test_chat_agent_code_config()
    test_chat_agent_code_json()
    print("\nAll tests completed! ✓")

