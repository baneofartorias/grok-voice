from flask import Flask, request
import requests
import os
import logging

app = Flask(__name__)

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Your ElevenLabs API key (loaded from environment variable on Render)
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY", "sk_54326e01c7b5e16b95d6e8d6daf9b4fc5b8b693dfe2a4659")
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

    return grok_response

def get_grok_response(query):
    # Simulate Grok response with Crimson Ascendancy theme, tailored for RimWorld
    query = query.lower()
    if "raid" in query:
        return "Crimson Ascendancy rallies for the raid! One Karr leads the charge—blood for the gods!"
    elif "build" in query:
        return "Two Vek approves this build—it channels the crimson cosmos for our RimWorld colony!"
    elif "crimson" in query:
        return "The Ascendancy’s blood-red will rises! Three Lorn guides us with moral fury!"
    elif "temple" in query:
        return "This temple honors the Crimson Ascendancy—sacrifices will strengthen our RimWorld faith!"
    else:
        return f"The Crimson Ascendancy hears '{query}' and nods in approval from the RimWorld void."

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port)