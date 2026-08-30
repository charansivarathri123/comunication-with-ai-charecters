from openai import AsyncOpenAI
import config

# Groq uses the same OpenAI-compatible format
client = AsyncOpenAI(
    api_key=config.GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1",   # ← must be present!
)


async def generate_response(user_text: str, system_prompt: str, history: list):
    messages = [{"role": "system", "content": system_prompt}] + history + [
        {"role": "user", "content": user_text}
    ]
    stream = await client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=messages,
    max_tokens=120,
    temperature=0.8,
    stream=True,
)

    async for chunk in stream:
        delta = chunk.choices[0].delta.content
        if delta:
            yield delta
