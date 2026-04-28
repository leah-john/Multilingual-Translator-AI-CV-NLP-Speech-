import edge_tts
import asyncio

def text_to_speech(text, lang):
    filename = "audio/output.mp3"

    voice_map = {
        "en": "en-US-JennyNeural",
        "fr": "fr-FR-DeniseNeural",
        "es": "es-ES-ElviraNeural",
        "hi": "hi-IN-SwaraNeural"
    }

    voice = voice_map.get(lang, "en-US-JennyNeural")

    async def generate():
        communicate = edge_tts.Communicate(text, voice=voice)
        await communicate.save(filename)

    asyncio.run(generate())

    return filename