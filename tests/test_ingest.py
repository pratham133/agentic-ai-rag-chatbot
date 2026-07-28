from ingest.ingest import DocumentIngestor

ingestor = DocumentIngestor(
    "data/Ebook-Agentic-AI.pdf"
)

chunks = ingestor.ingest()

print(f"Total Chunks : {len(chunks)}")

print("-" * 50)

print("Metadata")

print(chunks[0].metadata)

print("-" * 50)

print("Content")

print(chunks[0].page_content[:500])