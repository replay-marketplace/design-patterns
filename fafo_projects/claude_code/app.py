import asyncio
from claude_code_sdk import query, ClaudeCodeOptions, AssistantMessage, TextBlock

async def main():
    # Configure options - specify your model here
    options = ClaudeCodeOptions(
        model="claude-sonnet-4-5",  # Change model here (e.g., "claude-opus-4", "claude-sonnet-4-5")
        system_prompt="You are an expert Python developer. Generate clean, well-documented code.",
        max_turns=3,  # Limit turns to prevent runaway loops
    )

    prompt = "Write a Python function that calculates the nth Fibonacci number using memoization"

    print("Generating code...\n")
    
    async for message in query(prompt=prompt, options=options):
        if isinstance(message, AssistantMessage):
            for block in message.content:
                if isinstance(block, TextBlock):
                    print(block.text)

asyncio.run(main())