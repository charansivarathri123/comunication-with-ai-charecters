import config

print("OpenAI key loaded:", config.OPENAI_API_KEY is not None)
print("Groq key loaded:", config.GROQ_API_KEY is not None)
print("ElevenLabs key loaded:", config.ELEVENLABS_API_KEY is not None)
print("Voice ID loaded:", config.ELEVENLABS_VOICE_ID)

