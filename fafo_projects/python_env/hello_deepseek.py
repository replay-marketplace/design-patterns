#!/usr/bin/env python3
from deepseek import DeepSeekAPI
import os
import sys

# Get API key from command line argument or environment
api_key = sys.argv[1] if len(sys.argv) > 1 else os.getenv("DEEPSEEK_API_KEY")
if not api_key:
    print("Error: DEEPSEEK_API_KEY not found")
    print("Usage: python3 hello_deepseek.py [API_KEY]")
    print("Or set: export DEEPSEEK_API_KEY='your-key-here'")
    exit(1)

# Initialize client and say hi
client = DeepSeekAPI(api_key=api_key)
print("Saying hi to DeepSeek agent...")
#response = client.chat_completion(prompt="Hi!")


response = client.chat_completion(prompt="How would you implement Deepseek on Tenstorrent Galaxy")


# Print response
print("\nDeepSeek response:")
print(response)

