import requests
import config

def synthesize(text: str, voice_id: str = None) -> bytes:
    voice_id = voice_id or config.ELEVENLABS_VOICE_ID
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}/stream"
    resp = requests.post(
        url,
        headers={"xi-api-key": config.ELEVENLABS_API_KEY},
        json={
            "text": text,
            "model_id": "eleven_multilingual_v2",  # auto-handles Telugu/Hindi/etc.
            "voice_settings": {"stability": 0.6, "similarity_boost": 0.9},
        },
        stream=True,
    )
    return resp.content  # audio bytes → pipe to avatar + WebRTC
