import requests
from config import OLLAMA_URL, MODEL

def ask_ollama(prompt):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )
    
    return response.json()["response"]