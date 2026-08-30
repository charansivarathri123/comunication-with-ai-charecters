from openai import OpenAI
import config

# Groq's Whisper — same OpenAI-compatible format, free
client = OpenAI(
    api_key=config.GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1",
)


async def transcribe_stream(audio_bytes: bytes, filename: str = "audio.webm") -> str:
    """Transcribes recorded audio to text using Whisper on Groq."""
    result = client.audio.transcriptions.create(
        model="whisper-large-v3",
        file=(filename, audio_bytes, "audio/webm"),
    )
    return result.text
