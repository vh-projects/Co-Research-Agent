
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from app.config import LLM_MODEL, NVIDIA_API_KEY, GROQ_API_KEY, REQUEST_TIMEOUT
from langchain_groq import ChatGroq


class LLMClient:
    def __init__(self):
        # self.client = ChatGroq(
        #     model="llama-3.3-70b-versatile",
        #     api_key=GROQ_API_KEY,
        #     temperature=0.2,
        #     max_tokens=2048,
        #     timeout=120,
        # )
        self.client = ChatNVIDIA(
            model=LLM_MODEL,
            api_key=NVIDIA_API_KEY,
            temperature=0.2,
            max_tokens=2048,
            # timeout=REQUEST_TIMEOUT,
        )


    def invoke(self, prompt: str) -> str:
        response = self.client.invoke(prompt)

        content = response.content

        if isinstance(content, str):
            return content.strip()

        if isinstance(content, list):
            parts = []

            for item in content:
                if isinstance(item, str):
                    parts.append(item)
                elif isinstance(item, dict):
                    text = item.get("text")
                    if text:
                        parts.append(text)

            return "\n".join(parts).strip()

        return str(content).strip()
    
    
llm = LLMClient()


