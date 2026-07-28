"""
Retriever Module

Retrieves relevant chunks from Pinecone.
"""

from vectorstore.pinecone_store import PineconeVectorStore

from config.settings import settings


class Retriever:
    """Retrieves relevant documents."""

    def __init__(self):
        """Initialize vector store."""

        self.vector_store = PineconeVectorStore()

    def retrieve(self, query: str):
        """
        Retrieve top-k similar chunks.
        """

        results = self.vector_store.similarity_search(
            query=query,
            top_k=settings.top_k,
        )

        documents = []

        for match in results:

            documents.append(
                {
                    "text": match.metadata["text"],
                    "page": match.metadata["page"],
                    "score": match.score,
                }
            )

        return documents