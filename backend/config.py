import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Groq API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Check if API key exists
if not GROQ_API_KEY:
    raise ValueError("❌ GROQ_API_KEY not found. Please check your .env file.")