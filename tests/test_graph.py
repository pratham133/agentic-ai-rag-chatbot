"""
Test LangGraph Workflow
"""

from rag.graph import graph


state = {
    "question": "What is Agentic AI?"
}

result = graph.invoke(state)

print("=" * 60)
print("QUESTION\n")
print(result["question"])

print("\n" + "=" * 60)
print("ANSWER\n")
print(result["answer"])
print("=" * 60)