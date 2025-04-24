from flask import Flask, request
import requests
import os
import logging

app = Flask(__name__)

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Your ElevenLabs API key
ELEVENLABS_API_KEY = "sk_54326e01c7b5e16b95d6e8d6daf9b4fc5b8b693dfe2a4659"
# Path to OBS text file
OBS_TEXT_FILE = "C:\\Users\\baneo\\OneDrive\\Desktop\\grok-text.txt"
# Path to audio file
AUDIO_FILE = "C:\\Users\\baneo\\OneDrive\\Desktop\\temp_audio.mp3"
# Simulated Grok response (no public API yet)
GROK_SIMULATION = True

@app.route('/')
def handle_query():
    query = request.args.get('query', '')
    if not query:
        logger.warning("No query provided")
        return "No query provided"

    # Get Grok response
    grok_response = get_grok_response(query)
    logger.info(f"Grok response: {grok_response}")

    # Update OBS text file
    try:
        with open(OBS_TEXT_FILE, 'w', encoding='utf-8') as f:
            f.write(grok_response)
    except Exception as e:
        logger.error(f"Failed to write to OBS text file: {e}")

    # Generate ElevenLabs voice
    audio_url = generate_elevenlabs_audio(grok_response)

    return grok_response

def get_grok_response(query):
    # Simulate Grok response with Crimson Ascendancy theme
    query = query.lower()
    if "raid" in query:
        return "Crimson Ascendancy rallies for the raid! Blood for the gods!"
    elif "build" in query:
        return "This build channels the crimson cosmos—epic work!"
    elif "crimson" in query:
        return "The Ascendancy’s blood-red will rises!"
    else:
        return f"The Crimson Ascendancy hears '{query}' and nods in approval."

def generate_elevenlabs_audio(text):
    url = "https://api.elevenlabs.io/v1/text-to-speech/Fa4K0TVxiDTazJm4irHI/stream"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "content-type": "application/json"
    }
    payload = {
        "text": text,
        "voice_settings": {"similarity_boost": 0.85, "optimize_streaming_latency": 3}
    }
    try:
        response = requests.post(url, headers=headers, json=payload, stream=True)
        if response.status_code == 200:
            with open(AUDIO_FILE, "wb") as audio_file:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        audio_file.write(chunk)
            logger.info(f"Audio saved to {AUDIO_FILE}")
            return AUDIO_FILE
        else:
            logger.error(f"ElevenLabs API error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        logger.error(f"Failed to generate audio: {e}")
        return None

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)