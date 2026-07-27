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

    google_api_key: str
    pinecone_api_key: str

    pinecone_index_name: str

    chat_model: str
    embedding_model: str

    top_k: int


settings = Settings(
    google_api_key=getenv("GOOGLE_API_KEY", ""),

    pinecone_api_key=getenv("PINECONE_API_KEY", ""),

    pinecone_index_name=getenv(
        "PINECONE_INDEX_NAME",
        "agentic-ai-rag",
    ),

    chat_model=getenv(
        "CHAT_MODEL",
        "gemini-2.5-flash",
    ),

    embedding_model=getenv(
        "EMBEDDING_MODEL",
        "gemini-embedding-2-preview",
    ),

    top_k=int(getenv("TOP_K", "4")),
)