# test_nvidia.py

from langchain_nvidia_ai_endpoints import ChatNVIDIA
from app.config import LLM_MODEL, NVIDIA_API_KEY

llm = ChatNVIDIA(
    model="meta/llama-3.2-3b-instruct",
    api_key=NVIDIA_API_KEY,
)

print("Sending request...")

response = llm.invoke("Hello")

print(response)