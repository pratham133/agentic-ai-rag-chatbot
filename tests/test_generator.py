from rag.generator import ResponseGenerator
from rag.prompt_builder import PromptBuilder
from rag.retriever import Retriever


question = "What is Agentic AI?"


retriever = Retriever()

context = retriever.retrieve(question)


prompt = PromptBuilder.build(
    question,
    context,
)


generator = ResponseGenerator()

answer = generator.generate(prompt)


print("=" * 60)

print("QUESTION\n")

print(question)

print("\n")

print("=" * 60)

print("ANSWER\n")

print(answer)

print("\n")

print("=" * 60)