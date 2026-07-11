import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
load_dotenv(Path(__file__).resolve().parents[1] / ".env")

# Allowed origins for CORS (cors-origin-resource-sharing)
ALLOWED_ORIGINS = [
    "http://localhost:3000",
]

# ENV variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
DATABASE_URL = os.getenv("DATABASE_URL", "")