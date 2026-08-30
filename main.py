from fastapi import FastAPI, WebSocket
import asyncio, json
from stt import transcribe_stream
from llm_engine import generate_response
from tts import synthesize
from prompts import build_system_prompt

app = FastAPI()

@app.websocket("/session/{persona_id}")
async def session(ws: WebSocket, persona_id: str):
    await ws.accept()
    audio_in = asyncio.Queue()
    transcript_q = asyncio.Queue()
    history = []
    system_prompt = build_system_prompt("Steve Jobs", "Visionary Apple co-founder...")

    # Start STT in background
    stt_task = asyncio.create_task(transcribe_stream(audio_in, transcript_q))

    async def receive_audio():
        async for msg in ws.iter_bytes():
            await audio_in.put(msg)

    asyncio.create_task(receive_audio())

    while True:
        result = await transcript_q.get()
        full_reply = ""
        async for token in generate_response(result["text"], system_prompt, history):
            full_reply += token
        history.append({"role": "user", "content": result["text"]})
        history.append({"role": "assistant", "content": full_reply})
        audio = synthesize(full_reply)
        await ws.send_bytes(audio)          # → LiveKit track / Simli input
