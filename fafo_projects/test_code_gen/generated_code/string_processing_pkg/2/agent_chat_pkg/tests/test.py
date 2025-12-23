"""
Test file for the agent_chat package.
"""

import os
from dotenv import load_dotenv
from agent_chat import simple_chat, chat_agent_code_config, chat_agent_code_json

# Load environment variables
load_dotenv()

def test_simple_chat():
    """Test simple_chat function."""
    print("Testing simple_chat...")
    try:
        response = simple_chat("Say 'Hello, World!' and nothing else.")
        print(f"Response: {response}")
        assert isinstance(response, str)
        assert len(response) > 0
        print("✓ simple_chat test passed")
    except Exception as e:
        print(f"✗ simple_chat test failed: {e}")
        raise


def test_chat_agent_code_config():
    """Test chat_agent_code_config function."""
    print("\nTesting chat_agent_code_config...")
    try:
        response = chat_agent_code_config(
            "Write a simple Python function that adds two numbers.",
            "You are a helpful Python coding assistant."
        )
        print(f"Response: {response[:200]}...")
        assert isinstance(response, str)
        assert len(response) > 0
        print("✓ chat_agent_code_config test passed")
    except Exception as e:
        print(f"✗ chat_agent_code_config test failed: {e}")
        raise


def test_chat_agent_code_json():
    """Test chat_agent_code_json function."""
    print("\nTesting chat_agent_code_json...")
    try:
        response = chat_agent_code_json(
            "Generate a JSON object with fields: name, age, city",
            "data_generator"
        )
        print(f"Response: {response}")
        assert isinstance(response, str)
        assert len(response) > 0
        # Check if response contains JSON-like structure
        assert '{' in response or '[' in response
        print("✓ chat_agent_code_json test passed")
    except Exception as e:
        print(f"✗ chat_agent_code_json test failed: {e}")
        raise


if __name__ == "__main__":
    print("Running tests...\n")
    print("Note: These tests require ANTHROPIC_API_KEY environment variable to be set.\n")
    
    if not os.getenv("ANTHROPIC_API_KEY"):
        print("Warning: ANTHROPIC_API_KEY not found in environment variables.")
        print("Please set it in a .env file or as an environment variable.")
        print("Skipping tests...")
    else:
        test_simple_chat()
        test_chat_agent_code_config()
        test_chat_agent_code_json()
        
        print("\nAll tests passed!")
