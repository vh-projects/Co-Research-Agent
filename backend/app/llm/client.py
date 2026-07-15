# from langchain_nvidia_ai_endpoints import ChatNVIDIA

# from app.config import LLM_MODEL, NVIDIA_API_KEY


# class LLMClient:
#     def __init__(self):
#         self.client = ChatNVIDIA(
#             model=LLM_MODEL,
#             api_key=NVIDIA_API_KEY,
#             temperature=0.2,
#             max_tokens=4096,
#         )

#     def invoke(self, prompt: str) -> str:
#         response = self.client.invoke(prompt)
#         return response.content.strip()


# llm = LLMClient()


from langchain_nvidia_ai_endpoints import ChatNVIDIA

from app.config import LLM_MODEL, NVIDIA_API_KEY


class LLMClient:
    def __init__(self):
        self.client = ChatNVIDIA(
            model=LLM_MODEL,
            api_key=NVIDIA_API_KEY,
            temperature=0.2,
            max_tokens=2048,
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


