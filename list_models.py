# list_models.py
from openai import OpenAI
import config

client = OpenAI(
    api_key=config.GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1",
)

for m in client.models.list():
    print(m.id)
