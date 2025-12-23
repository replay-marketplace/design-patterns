"""
Test file for the agent_chat package.
"""

import os
from agent_chat import simple_chat, chat_agent_code_config, chat_agent_code_json


def test_simple_chat():
    """Test simple_chat function."""
    print("Testing simple_chat...")
    
    # Check if API key is set
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("  Skipped: ANTHROPIC_API_KEY not set")
        return
    
    try:
        response = simple_chat("Say 'Hello, World!' and nothing else.")
        print(f"  Response: {response[:100]}...")
        assert isinstance(response, str)
        assert len(response) > 0
        print("  ✓ Passed")
    except Exception as e:
        print(f"  ✗ Failed: {e}")


def test_chat_agent_code_config():
    """Test chat_agent_code_config function."""
    print("Testing chat_agent_code_config...")
    
    # Check if API key is set
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("  Skipped: ANTHROPIC_API_KEY not set")
        return
    
    try:
        response = chat_agent_code_config(
            prompt="Write a Python function that adds two numbers.",
            system="You are a helpful coding assistant."
        )
        print(f"  Response: {response[:100]}...")
        assert isinstance(response, str)
        assert len(response) > 0
        print("  ✓ Passed")
    except Exception as e:
        print(f"  ✗ Failed: {e}")


def test_chat_agent_code_json():
    """Test chat_agent_code_json function."""
    print("Testing chat_agent_code_json...")
    
    # Check if API key is set
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("  Skipped: ANTHROPIC_API_KEY not set")
        return
    
    try:
        response = chat_agent_code_json(
            prompt="Create a JSON object with name and age fields.",
            agent_type="python"
        )
        print(f"  Response: {response[:100]}...")
        assert isinstance(response, str)
        assert len(response) > 0
        print("  ✓ Passed")
    except Exception as e:
        print(f"  ✗ Failed: {e}")


if __name__ == "__main__":
    print("Running tests...\n")
    print("Note: Set ANTHROPIC_API_KEY environment variable to run API tests.\n")
    
    test_simple_chat()
    test_chat_agent_code_config()
    test_chat_agent_code_json()
    
    print("\nAll tests completed!")
