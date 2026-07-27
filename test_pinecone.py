from ingest.ingest import DocumentIngestor
from vectorstore.pinecone_store import PineconeVectorStore

ingestor = DocumentIngestor(
    "data/Ebook-Agentic-AI.pdf"
)

documents = ingestor.ingest()

store = PineconeVectorStore()

store.upload_documents(documents)