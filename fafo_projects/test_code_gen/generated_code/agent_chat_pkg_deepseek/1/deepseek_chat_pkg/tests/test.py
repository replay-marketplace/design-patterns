"""Tests for DeepSeek Chat package."""

import os
import pytest
import requests
from unittest.mock import patch, MagicMock
from deepseek_chat import simple_chat


class TestSimpleChat:
    """Test cases for simple_chat function."""
    
    def test_simple_chat_success(self, requests_mock):
        """Test successful API call."""
        # Mock API response
        mock_response = {
            "choices": [
                {
                    "message": {
                        "content": "def factorial(n):\n    if n <= 1:\n        return 1\n    return n * factorial(n-1)"
                    }
                }
            ]
        }
        
        requests_mock.post(
            "https://api.deepseek.com/v1/chat/completions",
            json=mock_response,
            status_code=200
        )
        
        # Test with explicit API key
        result = simple_chat("Write a factorial function", api_key="test-key")
        
        assert "factorial" in result
        assert "def" in result
    
    def test_simple_chat_with_env_api_key(self, requests_mock, monkeypatch):
        """Test API call with environment variable API key."""
        # Set environment variable
        monkeypatch.setenv("DEEPSEEK_API_KEY", "env-test-key")
        
        # Mock API response
        mock_response = {
            "choices": [
                {
                    "message": {
                        "content": "print('Hello, World!')"
                    }
                }
            ]
        }
        
        requests_mock.post(
            "https://api.deepseek.com/v1/chat/completions",
            json=mock_response,
            status_code=200
        )
        
        result = simple_chat("Write a hello world program")
        
        assert "Hello" in result
    
    def test_simple_chat_no_api_key(self, monkeypatch):
        """Test that ValueError is raised when no API key is provided."""
        # Remove API key from environment
        monkeypatch.delenv("DEEPSEEK_API_KEY", raising=False)
        
        with pytest.raises(ValueError, match="API key not provided"):
            simple_chat("Test prompt")
    
    def test_simple_chat_api_error(self, requests_mock, monkeypatch):
        """Test handling of API errors."""
        monkeypatch.setenv("DEEPSEEK_API_KEY", "test-key")
        
        # Mock API error
        requests_mock.post(
            "https://api.deepseek.com/v1/chat/completions",
            status_code=401,
            json={"error": "Unauthorized"}
        )
        
        with pytest.raises(requests.exceptions.RequestException):
            simple_chat("Test prompt")
    
    def test_simple_chat_unexpected_response_format(self, requests_mock, monkeypatch):
        """Test handling of unexpected API response format."""
        monkeypatch.setenv("DEEPSEEK_API_KEY", "test-key")
        
        # Mock unexpected response
        requests_mock.post(
            "https://api.deepseek.com/v1/chat/completions",
            json={"unexpected": "format"},
            status_code=200
        )
        
        with pytest.raises(ValueError, match="Unexpected API response format"):
            simple_chat("Test prompt")
    
    def test_simple_chat_custom_model(self, requests_mock, monkeypatch):
        """Test API call with custom model."""
        monkeypatch.setenv("DEEPSEEK_API_KEY", "test-key")
        
        mock_response = {
            "choices": [
                {
                    "message": {
                        "content": "Custom model response"
                    }
                }
            ]
        }
        
        requests_mock.post(
            "https://api.deepseek.com/v1/chat/completions",
            json=mock_response,
            status_code=200
        )
        
        result = simple_chat("Test prompt", model="custom-model")
        
        assert "Custom model response" in result
        
        # Verify the request was made with correct model
        assert requests_mock.last_request.json()["model"] == "custom-model"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
