from tts import synthesize

audio = synthesize("Hello, this is a test. నమస్కారం, ఇది ఒక పరీక్ష.")
with open("test.mp3", "wb") as f:
    f.write(audio)
print("Done! Check test.mp3")
