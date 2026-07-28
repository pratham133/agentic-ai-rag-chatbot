# 🤖 Agentic AI RAG Chatbot

A production-style Retrieval-Augmented Generation (RAG) chatbot built using **LangGraph**, **Pinecone**, **Google Gemini**, **FastAPI**, and **Streamlit**.

The chatbot answers questions **strictly from the provided Agentic AI eBook** by retrieving relevant knowledge from a vector database before generating responses with Gemini.

---

## ✨ Features

- 📄 PDF Knowledge Base
- ✂️ Intelligent Text Chunking
- 🧠 Gemini Embeddings
- 🔍 Pinecone Vector Search
- 🔗 LangGraph Workflow
- 🤖 Gemini Flash LLM
- ⚡ FastAPI REST API
- 🎨 Modern Streamlit Chat UI
- 📚 Retrieved Context Sources
- 📈 Similarity Confidence Scores
- 💬 Multi-turn Chat Interface

---

## 🏗 Project Architecture

```text
                   PDF
                    │
                    ▼
          Text Extraction
                    │
                    ▼
             Text Chunking
                    │
                    ▼
        Gemini Embeddings
                    │
                    ▼
        Pinecone Vector DB
                    │
                    ▼
             User Question
                    │
                    ▼
         Query Embedding
                    │
                    ▼
       Semantic Retrieval
                    │
                    ▼
      Retrieved Context Chunks
                    │
                    ▼
          LangGraph Workflow
                    │
                    ▼
            Gemini Flash LLM
                    │
                    ▼
            Grounded Answer
                    │
                    ▼
       FastAPI → Streamlit UI
```

---

## 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| LangGraph | RAG Workflow |
| Google Gemini | LLM |
| Gemini Embeddings | Text Embeddings |
| Pinecone | Vector Database |
| FastAPI | Backend API |
| Streamlit | Frontend UI |
| LangChain | LLM Integration |
| PyPDF | PDF Processing |
