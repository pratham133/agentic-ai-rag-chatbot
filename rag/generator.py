"""
Generator Module

Uses Gemini to generate grounded answers.
"""

from langchain_google_genai import ChatGoogleGenerativeAI

from config.settings import settings


class ResponseGenerator:
    """LLM Response Generator."""

    def __init__(self):

        self.llm = ChatGoogleGenerativeAI(
            model=settings.chat_model,
            google_api_key=settings.google_api_key,
            temperature=0,
        )

    def generate(self, prompt: str) -> str:
        """
        Generate the final answer.
        """

        response = self.llm.invoke(prompt)

        if isinstance(response.content, list):
            return response.content[0]["text"]

        return response.content