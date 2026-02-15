import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

class Settings:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    MODEL_NAME = "gemini-2.5-flash"

    # Validation to ensure we don't run without a key
    if not GEMINI_API_KEY:
        raise ValueError("❌ MISSING API KEY! Please check your .env file.")

settings = Settings()