"""
Retriever Module

Searches Pinecone and returns the
most relevant document chunks.
"""

from config.settings import settings
from vectorstore.pinecone_store import PineconeVectorStore


class Retriever:
    """Semantic Retriever."""

    def __init__(self):
        self.vector_store = PineconeVectorStore()

    def retrieve(self, query: str):
        """
        Retrieve relevant chunks
        from Pinecone.
        """

        matches = self.vector_store.similarity_search(
            query=query,
            top_k=settings.top_k,
        )

        retrieved_documents = []

        for match in matches:

            retrieved_documents.append(
                {
                    "score": match.score,
                    "text": match.metadata["text"],
                    "page": match.metadata["page"],
                }
            )

        return retrieved_documents