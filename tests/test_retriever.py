from rag.retriever import Retriever

retriever = Retriever()

results = retriever.retrieve(
    "What is Agentic AI?"
)

print("=" * 60)

for i, result in enumerate(results, start=1):

    print(f"\nResult {i}")

    print("-" * 60)

    print(f"Score : {result['score']:.4f}")

    print(f"Page  : {result['page']}")

    print()

    print(result["text"][:500])

print("=" * 60)