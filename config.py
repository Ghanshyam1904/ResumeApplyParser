import os
from dotenv import load_dotenv
load_dotenv()

EMAIL = os.getenv("Email")
EMAIL_PASSWORD = os.getenv("EmailPassword")
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen:7b"