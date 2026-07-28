from vectorstore.embeddings import EmbeddingService

embedding_service = EmbeddingService()

vector = embedding_service.embed_query(
    "What is Agentic AI?"
)

print("=" * 60)
print("Embedding Length:", len(vector))
print("=" * 60)

print(vector[:10])