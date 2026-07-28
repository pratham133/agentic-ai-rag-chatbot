"""
Graph State

Defines the shared state that flows between LangGraph nodes.
"""

from typing import TypedDict


class GraphState(TypedDict):
    """
    Shared state for the RAG workflow.
    """

    question: str
    documents: list[dict]
    prompt: str
    answer: str
    score: float