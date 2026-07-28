"""
Pydantic Schemas

Defines request and response models
for the FastAPI application.
"""

from pydantic import BaseModel


class ChatRequest(BaseModel):
    """
    Incoming chat request.
    """

    question: str


class Context(BaseModel):
    """
    Retrieved document chunk.
    """

    text: str
    page: int
    score: float


class ChatResponse(BaseModel):
    """
    Chat response.
    """

    question: str
    answer: str
    contexts: list[Context]