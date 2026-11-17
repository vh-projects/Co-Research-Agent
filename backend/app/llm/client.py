# # app/llm/client

from langchain_groq import ChatGroq
from app.config import GROQ_API_KEY


class LLMClient:
    def __init__(self):
        self.client = ChatGroq(
            model="qwen/qwen3.8-27b",
            # model="openai/gpt-oss-20b",
            api_key=GROQ_API_KEY,
            temperature=0.2,

            reasoning_effort="none",
            # reasoning_effort="low", # openai
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

    def structured(self, model):
        return self.client.with_structured_output(
            model,
            method="json_schema",
            strict=True,
        )


llm = LLMClient()
