import pytest
import os
from unittest.mock import patch, MagicMock
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agent_chat import simple_chat, chat_agent_code_config, chat_agent_code_json


class TestAgentChat:
    """Test suite for agent chat functions"""

    @patch('agent_chat.simple_chat.requests.post')
    def test_simple_chat(self, mock_post):
        """Test simple_chat function"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'choices': [{'message': {'content': 'Test response'}}]
        }
        mock_post.return_value = mock_response

        with patch.dict(os.environ, {'DEEPSEEK_API_KEY': 'test_key'}):
            result = simple_chat("Hello")
            assert isinstance(result, str)
            mock_post.assert_called_once()

    @patch('agent_chat.chat_agent_code_config.requests.post')
    def test_chat_agent_code_config(self, mock_post):
        """Test chat_agent_code_config function"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'choices': [{'message': {'content': 'def test(): pass'}}]
        }
        mock_post.return_value = mock_response

        with patch.dict(os.environ, {'DEEPSEEK_API_KEY': 'test_key'}):
            result = chat_agent_code_config("Write a function", "You are a code generator")
            assert isinstance(result, str)
            
            # Verify low temperature was used
            call_args = mock_post.call_args
            assert call_args is not None
            json_data = call_args[1]['json']
            assert json_data['temperature'] <= 0.3

    @patch('agent_chat.chat_agent_code_json.requests.post')
    def test_chat_agent_code_json(self, mock_post):
        """Test chat_agent_code_json function"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'choices': [{'message': {'content': '{"code": "test"}'}}]
        }
        mock_post.return_value = mock_response

        with patch.dict(os.environ, {'DEEPSEEK_API_KEY': 'test_key'}):
            result = chat_agent_code_json("Generate JSON", "python")
            assert isinstance(result, str)
            
            # Verify JSON response format was requested
            call_args = mock_post.call_args
            assert call_args is not None
            json_data = call_args[1]['json']
            assert 'response_format' in json_data or 'JSON' in str(json_data.get('messages', []))

    def test_simple_chat_no_api_key(self):
        """Test simple_chat raises error without API key"""
        with patch.dict(os.environ, {}, clear=True):
            with pytest.raises(ValueError, match="DEEPSEEK_API_KEY"):
                simple_chat("Hello")

    @patch('agent_chat.chat_agent_code_json.requests.post')
    def test_chat_agent_code_json_agent_types(self, mock_post):
        """Test different agent types in chat_agent_code_json"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'choices': [{'message': {'content': '{}'}}]
        }
        mock_post.return_value = mock_response

        with patch.dict(os.environ, {'DEEPSEEK_API_KEY': 'test_key'}):
            agent_types = ['python', 'javascript', 'general']
            for agent_type in agent_types:
                result = chat_agent_code_json("Test", agent_type)
                assert isinstance(result, str)
