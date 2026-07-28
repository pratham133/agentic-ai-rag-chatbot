"""
Tests for RAG pipeline.
"""

from rag.graph import rag_graph


def test_graph_execution():

    response = rag_graph.invoke(
        {
            "question": "What is artificial intelligence?"
        }
    )


    assert "answer" in response