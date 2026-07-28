"""
FastAPI Application

Exposes the RAG chatbot through a REST API.
"""

from fastapi import FastAPI, HTTPException

from api.schemas import (
    ChatRequest,
    ChatResponse,
)

from rag.graph import graph


app = FastAPI(
    title="Agentic AI RAG Chatbot",
    description="RAG-powered chatbot using LangGraph, Gemini, and Pinecone.",
    version="1.0.0",
)


@app.get("/")
def home():
    """
    Health check endpoint.
    """

    return {
        "status": "healthy",
        "message": "Agentic AI RAG Chatbot API is running."
    }


@app.post(
    "/chat",
    response_model=ChatResponse,
)
def chat(request: ChatRequest):
    """
    Ask a question to the chatbot.
    """

    try:

        result = graph.invoke(
            {
                "question": request.question
            }
        )

        return ChatResponse(
            question=result["question"],
            answer=result["answer"],
            contexts=result["documents"],
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )