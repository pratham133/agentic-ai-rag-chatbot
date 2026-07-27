"""
Pinecone Vector Store

Creates the Pinecone index, uploads document embeddings,
and performs semantic similarity search.
"""

from pinecone import (
    Pinecone,
    ServerlessSpec
)

from config.settings import settings
from vectorstore.embeddings import EmbeddingService


class PineconeVectorStore:
    """Handles all Pinecone operations."""

    def __init__(self):
        """Initialize Pinecone."""

        self.pc = Pinecone(
            api_key=settings.pinecone_api_key
        )

        self.embedding_service = EmbeddingService()

        self.index_name = settings.pinecone_index_name

        self.dimension = 3072

        self.create_index_if_not_exists()

        self.index = self.pc.Index(
            self.index_name
        )


    def create_index_if_not_exists(self):
        """
        Create Pinecone index if it doesn't exist.
        """

        existing_indexes = [
            index["name"]
            for index in self.pc.list_indexes()
        ]

        if self.index_name not in existing_indexes:

            self.pc.create_index(
                name=self.index_name,
                dimension=self.dimension,
                metric="cosine",
                spec=ServerlessSpec(
                    cloud="aws",
                    region="us-east-1"
                ),
            )

            print(
                f"Created index: {self.index_name}"
            )

        else:

            print(
                f"Using existing index: {self.index_name}"
            )


    def upload_documents(self, documents):
        """
        Upload document chunks in batches.
        """

        vectors = []

        for i, document in enumerate(documents):

            embedding = self.embedding_service.embed_query(
                document.page_content
            )

            vectors.append(
                {
                    "id": str(i),
                    "values": embedding,
                    "metadata": {
                        "text": document.page_content,
                        "page": document.metadata.get(
                            "page",
                            -1
                        ),
                    },
                }
            )


        batch_size = 20

        for start in range(
            0,
            len(vectors),
            batch_size
        ):

            batch = vectors[
                start:start + batch_size
            ]

            self.index.upsert(
                vectors=batch
            )

            print(
                f"Uploaded batch {start // batch_size + 1}"
            )


        print(
            f"\nUploaded {len(vectors)} vectors successfully."
        )


    def similarity_search(
        self,
        query,
        top_k=4,
    ):
        """
        Perform semantic search.
        """

        query_embedding = (
            self.embedding_service.embed_query(
                query
            )
        )


        results = self.index.query(
            vector=query_embedding,
            top_k=top_k,
            include_metadata=True,
        )


        return results.matches