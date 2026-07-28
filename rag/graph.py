"""
LangGraph Workflow

Defines the complete RAG workflow using LangGraph.
"""

from langgraph.graph import StateGraph, START, END

from rag.graph_state import GraphState
from rag.retriever import Retriever
from rag.prompt_builder import PromptBuilder
from rag.generator import ResponseGenerator


# -------------------------------------------------
# Initialize Components
# -------------------------------------------------

retriever = Retriever()
prompt_builder = PromptBuilder()
generator = ResponseGenerator()


# -------------------------------------------------
# Node 1 - Retrieve Documents
# -------------------------------------------------

def retrieve_node(state: GraphState):
    """
    Retrieve relevant documents from Pinecone.
    """

    print("\n==============================")
    print("RETRIEVE NODE")
    print("==============================")
    print("Question:", state["question"])

    documents = retriever.retrieve(
        state["question"]
    )

    print("\nRetrieved Documents Type:")
    print(type(documents))

    print("\nRetrieved Documents:")
    print(documents)

    print("==============================\n")

    return {
        "documents": documents
    }


# -------------------------------------------------
# Node 2 - Build Prompt
# -------------------------------------------------

def prompt_node(state: GraphState):
    """
    Create the grounded prompt.
    """

    print("\n==============================")
    print("PROMPT NODE")
    print("==============================")

    print("Documents Type:")
    print(type(state["documents"]))

    print("\nDocuments:")
    print(state["documents"])

    print("==============================\n")

    prompt = prompt_builder.build(
        question=state["question"],
        context=state["documents"],
    )

    return {
        "prompt": prompt
    }


# -------------------------------------------------
# Node 3 - Generate Answer
# -------------------------------------------------

def generate_node(state: GraphState):
    """
    Generate the final answer using Gemini.
    """

    print("\n==============================")
    print("GENERATION NODE")
    print("==============================")

    answer = generator.generate(
        state["prompt"]
    )

    print("Generation Complete.")

    print("==============================\n")

    return {
        "answer": answer
    }


# -------------------------------------------------
# Build Workflow
# -------------------------------------------------

workflow = StateGraph(GraphState)

workflow.add_node(
    "retrieve",
    retrieve_node,
)

workflow.add_node(
    "prompt",
    prompt_node,
)

workflow.add_node(
    "generate",
    generate_node,
)

workflow.add_edge(
    START,
    "retrieve",
)

workflow.add_edge(
    "retrieve",
    "prompt",
)

workflow.add_edge(
    "prompt",
    "generate",
)

workflow.add_edge(
    "generate",
    END,
)


# -------------------------------------------------
# Compile Graph
# -------------------------------------------------

graph = workflow.compile()