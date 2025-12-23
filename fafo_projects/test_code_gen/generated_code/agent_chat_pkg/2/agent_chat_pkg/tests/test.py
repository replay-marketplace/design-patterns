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
        print("  ⚠️  ANTHROPIC_API_KEY not set. Skipping test.")
        return
    
    try:
        response = simple_chat("Say 'Hello, World!' and nothing else.")
        print(f"  Response: {response[:100]}...")
        assert isinstance(response, str)
        assert len(response) > 0
        print("  ✓ simple_chat test passed")
    except Exception as e:
        print(f"  ✗ simple_chat test failed: {e}")


def test_chat_agent_code_config():
    """Test chat_agent_code_config function."""
    print("\nTesting chat_agent_code_config...")
    
    # Check if API key is set
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("  ⚠️  ANTHROPIC_API_KEY not set. Skipping test.")
        return
    
    try:
        system_msg = "You are a helpful coding assistant."
        response = chat_agent_code_config(
            "Write a one-line Python function that adds two numbers.",
            system_msg
        )
        print(f"  Response: {response[:100]}...")
        assert isinstance(response, str)
        assert len(response) > 0
        print("  ✓ chat_agent_code_config test passed")
    except Exception as e:
        print(f"  ✗ chat_agent_code_config test failed: {e}")


def test_chat_agent_code_json():
    """Test chat_agent_code_json function."""
    print("\nTesting chat_agent_code_json...")
    
    # Check if API key is set
    if not os.environ.get("ANTHROPIC_API_KEY"):
        print("  ⚠️  ANTHROPIC_API_KEY not set. Skipping test.")
        return
    
    try:
        response = chat_agent_code_json(
            "Create a JSON object with keys 'name' and 'age'.",
            "json_generator"
        )
        print(f"  Response: {response[:100]}...")
        assert isinstance(response, str)
        assert len(response) > 0
        print("  ✓ chat_agent_code_json test passed")
    except Exception as e:
        print(f"  ✗ chat_agent_code_json test failed: {e}")


if __name__ == "__main__":
    print("Running tests...\n")
    print("Note: These tests require ANTHROPIC_API_KEY environment variable to be set.\n")
    
    test_simple_chat()
    test_chat_agent_code_config()
    test_chat_agent_code_json()
    
    print("\nAll tests completed!")
