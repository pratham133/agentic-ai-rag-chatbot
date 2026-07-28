"""
RAG Pipeline

Provides a simple interface for interacting with the LangGraph workflow.
"""

from rag.graph import RAGGraph


class RAGPipeline:
    """Main RAG interface."""

    def __init__(self):

        self.graph = RAGGraph()

    def ask(self, question: str) -> dict:

        result = self.graph.invoke(question)

        return {
            "answer": result["answer"],
            "contexts": result["contexts"],
        }