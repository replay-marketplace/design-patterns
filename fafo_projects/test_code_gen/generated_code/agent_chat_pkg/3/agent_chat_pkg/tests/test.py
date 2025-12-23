import pytest
import os
from agent_chat import simple_chat, chat_agent_code_config, chat_agent_code_json
import json

# Note: These tests require ANTHROPIC_API_KEY environment variable to be set
# For CI/CD, you may want to mock the Anthropic client

def test_simple_chat():
    """Test simple_chat function"""
    if not os.getenv('ANTHROPIC_API_KEY'):
        pytest.skip("ANTHROPIC_API_KEY not set")
    
    response = simple_chat("Say 'test passed' and nothing else.")
    assert isinstance(response, str)
    assert len(response) > 0

def test_chat_agent_code_config():
    """Test chat_agent_code_config function"""
    if not os.getenv('ANTHROPIC_API_KEY'):
        pytest.skip("ANTHROPIC_API_KEY not set")
    
    system = "You are a helpful coding assistant."
    prompt = "Write a simple Python function that adds two numbers."
    response = chat_agent_code_config(prompt, system)
    assert isinstance(response, str)
    assert len(response) > 0

def test_chat_agent_code_json():
    """Test chat_agent_code_json function"""
    if not os.getenv('ANTHROPIC_API_KEY'):
        pytest.skip("ANTHROPIC_API_KEY not set")
    
    prompt = "Generate a simple JSON object with a 'status' field set to 'ok'."
    response = chat_agent_code_json(prompt, "python")
    assert isinstance(response, str)
    # Verify it's valid JSON
    try:
        json.loads(response)
    except json.JSONDecodeError:
        pytest.fail("Response is not valid JSON")

def test_chat_agent_code_json_different_agent_types():
    """Test chat_agent_code_json with different agent types"""
    if not os.getenv('ANTHROPIC_API_KEY'):
        pytest.skip("ANTHROPIC_API_KEY not set")
    
    agent_types = ["python", "javascript", "data"]
    prompt = "Generate a JSON object with a 'message' field."
    
    for agent_type in agent_types:
        response = chat_agent_code_json(prompt, agent_type)
        assert isinstance(response, str)
        # Verify it's valid JSON
        try:
            json.loads(response)
        except json.JSONDecodeError:
            pytest.fail(f"Response for agent_type '{agent_type}' is not valid JSON")

def test_simple_chat_empty_prompt():
    """Test simple_chat with empty prompt"""
    if not os.getenv('ANTHROPIC_API_KEY'):
        pytest.skip("ANTHROPIC_API_KEY not set")
    
    with pytest.raises(ValueError):
        simple_chat("")

def test_chat_agent_code_config_empty_system():
    """Test chat_agent_code_config with empty system message"""
    if not os.getenv('ANTHROPIC_API_KEY'):
        pytest.skip("ANTHROPIC_API_KEY not set")
    
    with pytest.raises(ValueError):
        chat_agent_code_config("Test prompt", "")
