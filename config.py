from dotenv import load_dotenv
load_dotenv()  # load the .env file
import os
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
ELEVENLABS_VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID")
SIMLI_API_KEY = os.getenv("SIMLI_API_KEY")