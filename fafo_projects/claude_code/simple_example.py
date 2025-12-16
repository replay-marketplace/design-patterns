"""
Simplest possible example of using Claude SDK Client.
"""

import os
from anthropic import Anthropic

# Initialize the Claude SDK client
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# Send a simple message
message = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=100,
    messages=[
        {"role": "user", "content": "Hello, Claude!"}
    ]
)

# Print the response
print(message.content[0].text)



