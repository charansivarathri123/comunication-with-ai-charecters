import asyncio
from llm_engine import generate_response
from prompts import build_system_prompt

async def main():
    prompt = build_system_prompt("Steve Jobs", "Apple co-founder, visionary.")
    async for token in generate_response("Hello, who are you?", prompt, []):
        print(token, end="", flush=True)
asyncio.run(main())

import asyncio

# ... existing code ...

async def main():
    # ... existing code ...
    print()  # just add a newline at the end

asyncio.run(main(), debug=False)
