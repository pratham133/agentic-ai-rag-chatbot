"""
Application Configuration

Loads environment variables and exposes them
through a strongly typed Settings object.
"""

from dataclasses import dataclass
from os import getenv

from dotenv import load_dotenv


load_dotenv()


@dataclass(frozen=True)
class Settings:
    """Application configuration."""

    openai_api_key: str
    pinecone_api_key: str

    pinecone_index_name: str

    chat_model: str
    embedding_model: str

    top_k: int


settings = Settings(
    openai_api_key=getenv("OPENAI_API_KEY", ""),
    pinecone_api_key=getenv("PINECONE_API_KEY", ""),

    pinecone_index_name=getenv(
        "PINECONE_INDEX_NAME",
        "agentic-ai-rag",
    ),

    chat_model=getenv(
        "OPENAI_CHAT_MODEL",
        "gpt-4.1-mini",
    ),

    embedding_model=getenv(
        "OPENAI_EMBEDDING_MODEL",
        "text-embedding-3-small",
    ),

    top_k=int(getenv("TOP_K", "4")),
)