import os

from dotenv import load_dotenv

load_dotenv()

NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
GROQ_API_KEY= os.getenv("GROQ_API_KEY")

LLM_MODEL = "meta/llama-3.2-3b-instruct"

MAX_SEARCH_RESULTS = 5

# MAX_CONTENT_LENGTH= 1000
REQUEST_TIMEOUT = 120

if not NVIDIA_API_KEY:
    raise ValueError("NVIDIA_API_KEY is missing.")

if not TAVILY_API_KEY:
    raise ValueError("TAVILY_API_KEY is missing.")
