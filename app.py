"""
LangGraph Workflow

Defines the RAG workflow using LangGraph.
"""

from langgraph.graph import StateGraph, START, END

from rag.graph_state import GraphState

from rag.retriever import Retriever

from rag.prompt_builder import PromptBuilder

from rag.generator import ResponseGenerator

retriever = Retriever()
prompt_builder = PromptBuilder()
generator = ResponseGenerator()

def retrieve_node(state: GraphState):
    """
    Retrieve relevant documents.
    """

    documents = retriever.retrieve(
        state["question"]
    )

    return {
        "documents": documents
    }

def prompt_node(state: GraphState):
    """
    Build the prompt.
    """

    prompt = prompt_builder.build(
        question=state["question"],
        context=state["documents"],
    )

    return {
        "prompt": prompt
    }

def generate_node(state: GraphState):
    """
    Generate the final answer.
    """

    answer = generator.generate(
        state["prompt"]
    )

    return {
        "answer": answer
    }

graph = StateGraph(GraphState)

graph.add_node("retrieve", retrieve_node)
graph.add_node("prompt", prompt_node)
graph.add_node("generate", generate_node)

graph.add_edge(START, "retrieve")
graph.add_edge("retrieve", "prompt")
graph.add_edge("prompt", "generate")
graph.add_edge("generate", END)

rag_graph = graph.compile()