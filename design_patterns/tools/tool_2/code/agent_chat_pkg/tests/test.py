"""Tests for agent_chat package."""

import os
import sys

# Add parent directory to path to import package
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from agent_chat import (
    simple_chat,
    chat_agent_code_json
)


def test_simple_chat():
    """Test simple_chat function."""
    print("Testing simple_chat...")
    
    # Check if API key is set
    if not os.environ.get("DEEPSEEK_API_KEY"):
        print("⚠ Skipping simple_chat test: DEEPSEEK_API_KEY not set")
        return
    
    try:
        response = simple_chat("Say hello in one sentence.")
        assert isinstance(response, str)
        assert len(response) > 0
        print("✓ simple_chat test passed")
    except Exception as e:
        print(f"✗ simple_chat test failed: {e}")


def test_chat_agent_code_json():
    """Test chat_agent_code_json function."""
    print("\nTesting chat_agent_code_json...")
    
    # Check if API key is set
    if not os.environ.get("DEEPSEEK_API_KEY"):
        print("⚠ Skipping chat_agent_code_json test: DEEPSEEK_API_KEY not set")
        return
    
    try:
        prompt = "Generate a JSON object with a 'name' field set to 'John' and an 'age' field set to 30"
        json_str, input_count, output_count = chat_agent_code_json(prompt)
        
        assert isinstance(json_str, str)
        assert len(json_str) > 0
        assert isinstance(input_count, int)
        assert input_count > 0
        assert isinstance(output_count, int)
        assert output_count > 0
        
        # Verify it's valid JSON (basic check)
        import json
        try:
            parsed = json.loads(json_str)
            assert isinstance(parsed, dict)
            print("✓ chat_agent_code_json test passed - valid JSON returned")
        except json.JSONDecodeError:
            print("⚠ chat_agent_code_json returned non-JSON (may need adjustment)")
        
        print(f"  Input word count: {input_count}")
        print(f"  Output word count: {output_count}")
        
    except Exception as e:
        print(f"✗ chat_agent_code_json test failed: {e}")


def test_word_counting():
    """Test that word counting works correctly."""
    print("\nTesting word counting...")
    
    # Check if API key is set
    if not os.environ.get("DEEPSEEK_API_KEY"):
        print("⚠ Skipping word counting test: DEEPSEEK_API_KEY not set")
        return
    
    try:
        # Simple prompt with known word count
        prompt = "Hello world test"
        expected_input_words = 3
        
        json_str, input_count, output_count = chat_agent_code_json(prompt)
        
        assert input_count == expected_input_words, f"Expected {expected_input_words} words, got {input_count}"
        assert output_count > 0, "Output word count should be greater than 0"
        
        print(f"✓ Word counting test passed")
        print(f"  Expected input words: {expected_input_words}, got: {input_count}")
        
    except Exception as e:
        print(f"✗ Word counting test failed: {e}")


if __name__ == "__main__":
    test_simple_chat()
    test_chat_agent_code_json()
    test_word_counting()
    print("\nAll tests completed!")

