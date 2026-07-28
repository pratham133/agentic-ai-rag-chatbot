from rag.pipeline import RAGPipeline


rag = RAGPipeline()

question = "What is Agentic AI?"

print("=" * 60)
print("QUESTION")
print()
print(question)
print()

result = rag.ask(question)

print("=" * 60)
print("QUESTION\n")
print(question)

print("\n" + "=" * 60)
print("ANSWER\n")
print(result["answer"])

print("\n" + "=" * 60)
print("RETRIEVED CONTEXT\n")

for i, chunk in enumerate(result["contexts"], start=1):
    print(f"\nChunk {i}:")
    print(chunk[:300])
    print("-" * 60)