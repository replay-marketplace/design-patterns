import anthropic
import json
from typing import List, Dict


def coder(prompt: str) -> str:
    """
    Uses Anthropic Claude claude-opus-4-5-20251101 to generate code based on a prompt.
    
    Args:
        prompt: A string describing what code to generate.
        
    Returns:
        A JSON string containing a list of file objects with 'path' and 'contents' keys.
    """
    client = anthropic.Anthropic()
    
    system_prompt = """You are a code generation assistant. You must respond ONLY with valid JSON.
Your response must be a JSON array of objects, where each object has:
- "path": the file path (e.g., "main.py")
- "contents": the file contents as a string

Example response format:
[
  {"path": "main.py", "contents": "print('hello world')"},
  {"path": "README.md", "contents": "# Project\n\nDescription here."}
]

Do not include any markdown code blocks, explanations, or text outside the JSON array.
Your entire response must be parseable as JSON."""

    user_message = f"""Generate code for the following request:

{prompt}

Respond with a JSON array containing file objects with 'path' and 'contents' keys.
Always include at least:
1. A main code file (e.g., main.py)
2. A README_tests.md file with testing instructions

Respond with valid JSON only."""

    message = client.messages.create(
        model="claude-opus-4-5-20251101",
        max_tokens=4096,
        messages=[
            {
                "role": "user",
                "content": user_message
            }
        ],
        system=system_prompt
    )
    
    response_text = message.content[0].text
    
    # Validate that the response is valid JSON
    try:
        parsed = json.loads(response_text)
        # Ensure it's a list
        if not isinstance(parsed, list):
            parsed = [parsed]
        # Validate structure
        for item in parsed:
            if not isinstance(item, dict) or 'path' not in item or 'contents' not in item:
                raise ValueError("Invalid structure: each item must have 'path' and 'contents'")
        return json.dumps(parsed, indent=2)
    except json.JSONDecodeError as e:
        # If response isn't valid JSON, wrap it in a proper structure
        return json.dumps([
            {"path": "main.py", "contents": response_text},
            {"path": "README_tests.md", "contents": "# Tests\n\nRun the generated code to test."}
        ], indent=2)
