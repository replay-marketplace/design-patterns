"""DeepSeek API client implementation."""

import requests
from typing import List, Dict, Any, Optional


class DeepSeekClient:
    """Client for interacting with the DeepSeek API."""
    
    def __init__(self, api_key: str, base_url: str = "https://api.deepseek.com/v1"):
        """Initialize the DeepSeek client.
        
        Args:
            api_key: The API key for authentication
            base_url: The base URL for the API (default: https://api.deepseek.com/v1)
        """
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    
    def chat(
        self,
        messages: List[Dict[str, str]],
        model: str = "deepseek-coder",
        temperature: float = 0.7,
        max_tokens: int = 2048,
        top_p: float = 1.0,
        frequency_penalty: float = 0.0,
        presence_penalty: float = 0.0,
        stop: Optional[List[str]] = None
    ) -> str:
        """Send a chat completion request to the DeepSeek API.
        
        Args:
            messages: List of message dictionaries with 'role' and 'content' keys
            model: The model to use for generation
            temperature: Sampling temperature (0.0 to 2.0)
            max_tokens: Maximum number of tokens to generate
            top_p: Nucleus sampling parameter
            frequency_penalty: Frequency penalty parameter
            presence_penalty: Presence penalty parameter
            stop: List of stop sequences
        
        Returns:
            str: The generated response text
        
        Raises:
            Exception: If the API request fails
        """
        endpoint = f"{self.base_url}/chat/completions"
        
        payload = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "top_p": top_p,
            "frequency_penalty": frequency_penalty,
            "presence_penalty": presence_penalty
        }
        
        if stop:
            payload["stop"] = stop
        
        try:
            response = requests.post(
                endpoint,
                headers=self.headers,
                json=payload,
                timeout=60
            )
            response.raise_for_status()
            
            data = response.json()
            
            if "choices" in data and len(data["choices"]) > 0:
                return data["choices"][0]["message"]["content"]
            else:
                raise Exception("No response generated from API")
                
        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {str(e)}")
        except (KeyError, IndexError) as e:
            raise Exception(f"Unexpected API response format: {str(e)}")
