"""
Prompt Builder

Creates a grounded prompt for Gemini.
"""


class PromptBuilder:
    """Build prompts for RAG."""

    @staticmethod
    def build(question: str, context: list[dict]) -> str:
        """
        Build the final prompt.
        """

        retrieved_context = "\n\n".join(
            chunk["text"]
            for chunk in context
        )

        return f"""
You are an AI assistant that answers questions ONLY using the provided context.

Rules:

1. Use ONLY the information provided below.

2. If the answer is not present in the context, reply exactly:

"I couldn't find that information in the provided document."

3. Never use outside knowledge.

4. Never guess.

5. Keep the answer concise and accurate.



Context:

{retrieved_context}



Question:

{question}



Answer:
"""