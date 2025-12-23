"""Tests for DeepSeek Chat package."""

import pytest
import os
from unittest.mock import Mock, patch, MagicMock
import requests

from deepseek_chat import simple_chat
from deepseek_chat.deepseek_client import DeepSeekClient
from deepseek_chat.config import Config


class TestSimpleChat:
    """Test cases for simple_chat function."""
    
    def test_simple_chat_with_api_key(self, requests_mock):
        """Test simple_chat with explicit API key."""
        mock_response = {
            "choices": [
                {
                    "message": {
                        "content": "Here's a factorial function:\n\ndef factorial(n):\n    if n <= 1:\n        return 1\n    return n * factorial(n-1)"
                    }
                }
            ]
        }
        
        requests_mock.post(
            "https://api.deepseek.com/v1/chat/completions",
            json=mock_response
        )
        
        response = simple_chat(
            "Write a factorial function",
            api_key="test_api_key"
        )
        
        assert "factorial" in response.lower()
        assert "def" in response
    
    def test_simple_chat_with_env_api_key(self, requests_mock, monkeypatch):
        """Test simple_chat with API key from environment."""
        monkeypatch.setenv("DEEPSEEK_API_KEY", "env_api_key")
        
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
            json=mock_response
        )
        
        response = simple_chat("Write hello world")
        
        assert "Hello" in response
    
    def test_simple_chat_no_api_key(self):
        """Test simple_chat raises error when no API key provided."""
        with patch.dict(os.environ, {}, clear=True):
            with pytest.raises(ValueError, match="API key is required"):
                simple_chat("test prompt")
    
    def test_simple_chat_empty_prompt(self):
        """Test simple_chat raises error for empty prompt."""
        with pytest.raises(ValueError, match="Prompt must be a non-empty string"):
            simple_chat("", api_key="test_key")
    
    def test_simple_chat_invalid_prompt_type(self):
        """Test simple_chat raises error for non-string prompt."""
        with pytest.raises(ValueError, match="Prompt must be a non-empty string"):
            simple_chat(123, api_key="test_key")


class TestDeepSeekClient:
    """Test cases for DeepSeekClient class."""
    
    def test_client_initialization(self):
        """Test client initialization."""
        client = DeepSeekClient(api_key="test_key")
        
        assert client.api_key == "test_key"
        assert client.base_url == "https://api.deepseek.com/v1"
        assert "Bearer test_key" in client.headers["Authorization"]
    
    def test_client_custom_base_url(self):
        """Test client with custom base URL."""
        client = DeepSeekClient(
            api_key="test_key",
            base_url="https://custom.api.com/v1/"
        )
        
        assert client.base_url == "https://custom.api.com/v1"
    
    def test_chat_success(self, requests_mock):
        """Test successful chat completion."""
        mock_response = {
            "choices": [
                {
                    "message": {
                        "content": "This is a test response"
                    }
                }
            ]
        }
        
        requests_mock.post(
            "https://api.deepseek.com/v1/chat/completions",
            json=mock_response
        )
        
        client = DeepSeekClient(api_key="test_key")
        response = client.chat(
            messages=[{"role": "user", "content": "test"}]
        )
        
        assert response == "This is a test response"
    
    def test_chat_api_error(self, requests_mock):
        """Test chat with API error."""
        requests_mock.post(
            "https://api.deepseek.com/v1/chat/completions",
            status_code=500,
            text="Internal Server Error"
        )
        
        client = DeepSeekClient(api_key="test_key")
        
        with pytest.raises(Exception, match="API request failed"):
            client.chat(messages=[{"role": "user", "content": "test"}])
    
    def test_chat_unexpected_response_format(self, requests_mock):
        """Test chat with unexpected response format."""
        requests_mock.post(
            "https://api.deepseek.com/v1/chat/completions",
            json={"unexpected": "format"}
        )
        
        client = DeepSeekClient(api_key="test_key")
        
        with pytest.raises(Exception, match="Unexpected API response format|No response generated"):
            client.chat(messages=[{"role": "user", "content": "test"}])
    
    def test_chat_with_custom_parameters(self, requests_mock):
        """Test chat with custom parameters."""
        mock_response = {
            "choices": [
                {
                    "message": {
                        "content": "Custom response"
                    }
                }
            ]
        }
        
        requests_mock.post(
            "https://api.deepseek.com/v1/chat/completions",
            json=mock_response
        )
        
        client = DeepSeekClient(api_key="test_key")
        response = client.chat(
            messages=[{"role": "user", "content": "test"}],
            model="custom-model",
            temperature=0.5,
            max_tokens=1024,
            stop=["\n\n"]
        )
        
        assert response == "Custom response"
        
        # Verify request payload
        request_json = requests_mock.last_request.json()
        assert request_json["model"] == "custom-model"
        assert request_json["temperature"] == 0.5
        assert request_json["max_tokens"] == 1024
        assert request_json["stop"] == ["\n\n"]


class TestConfig:
    """Test cases for Config class."""
    
    def test_get_api_key_from_env(self, monkeypatch):
        """Test getting API key from environment."""
        monkeypatch.setenv("DEEPSEEK_API_KEY", "test_env_key")
        
        api_key = Config.get_api_key()
        assert api_key == "test_env_key"
    
    def test_get_api_key_not_set(self, monkeypatch):
        """Test getting API key when not set."""
        monkeypatch.delenv("DEEPSEEK_API_KEY", raising=False)
        
        api_key = Config.get_api_key()
        assert api_key is None
    
    def test_get_base_url_default(self, monkeypatch):
        """Test getting default base URL."""
        monkeypatch.delenv("DEEPSEEK_BASE_URL", raising=False)
        
        base_url = Config.get_base_url()
        assert base_url == "https://api.deepseek.com/v1"
    
    def test_get_base_url_custom(self, monkeypatch):
        """Test getting custom base URL from environment."""
        monkeypatch.setenv("DEEPSEEK_BASE_URL", "https://custom.api.com")
        
        base_url = Config.get_base_url()
        assert base_url == "https://custom.api.com"


@pytest.fixture
def requests_mock():
    """Fixture for mocking requests."""
    with patch('requests.post') as mock_post:
        mock_response = Mock()
        mock_response.raise_for_status = Mock()
        mock_response.json = Mock()
        mock_post.return_value = mock_response
        yield mock_post
