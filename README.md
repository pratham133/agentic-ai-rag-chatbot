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
---

# 📂 Project Structure

```text
agentic-ai-rag-chatbot/
│
├── api/                 # FastAPI backend
├── config/              # Environment configuration
├── data/                # PDF knowledge base
├── ingest/              # PDF ingestion pipeline
├── rag/                 # LangGraph RAG workflow
├── screenshots/         # README screenshots
├── tests/               # Unit tests
├── ui/                  # Streamlit frontend
├── vectorstore/         # Pinecone integration
│
├── .env.example
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/<your-username>/agentic-ai-rag-chatbot.git

cd agentic-ai-rag-chatbot
```

---

## 2. Create a virtual environment

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY

PINECONE_API_KEY=YOUR_PINECONE_API_KEY

PINECONE_INDEX_NAME=agentic-ai-rag

CHAT_MODEL=gemini-flash-latest

EMBEDDING_MODEL=gemini-embedding-2-preview

TOP_K=4
```

---

# 🚀 Running the Project

## Step 1 — Ingest the PDF

```bash
python ingest/main.py
```

This will:

- Read the PDF
- Chunk the document
- Generate Gemini embeddings
- Store vectors in Pinecone

---

## Step 2 — Start FastAPI

```bash
uvicorn api.main:app --reload
```

FastAPI will run on

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

## Step 3 — Start Streamlit

```bash
streamlit run ui/app.py
```

The application opens at

```
http://localhost:8501
```

---

# 📡 API Endpoint

## POST /chat

Request

```json
{
    "question": "What is Agentic AI?"
}
```

Example Response

```json
{
    "question": "What is Agentic AI?",
    "answer": "...",
    "contexts": [
        {
            "page": 17,
            "score": 0.817,
            "text": "..."
        }
    ]
}
```

The API returns:

- Generated answer
- Retrieved context chunks
- Similarity scores

This satisfies the interview requirement of returning both the answer and supporting evidence.

---

# 📸 Application Screenshots

## 🏠 Home Page

A clean and modern Streamlit interface with project information and chat capabilities.

![Home Page](screenshots/home-page.png)

---

## 💬 Chat Example

The chatbot answers questions using Retrieval-Augmented Generation (RAG), grounding every response in the uploaded Agentic AI eBook.

![Chat Example](screenshots/chat-example.png)

---

## 💭 Multi-turn Conversation (Part 1)

Example of a conversation showing multiple grounded responses from the knowledge base.

![Conversation Part 1](screenshots/conversation-1.png)

---

## 💭 Multi-turn Conversation (Part 2)

Continuation of the conversation with additional questions and retrieved sources.

![Conversation Part 2](screenshots/conversation-2.png)

---

## ⚡ FastAPI Documentation

Interactive Swagger UI generated automatically by FastAPI.

![FastAPI Docs](screenshots/fastapi-docs.png)

---

# 💬 Sample Queries

The following are example questions that can be asked to the chatbot.

- What is Agentic AI?
- Explain Agentic AI in simple language.
- How does Agentic AI work?
- What are the benefits of Agentic AI?
- Summarize the document in five bullet points.
- How is Agentic AI different from traditional AI?

---

# 🏗️ Architecture Explanation

The chatbot follows a Retrieval-Augmented Generation (RAG) architecture.

1. The Agentic AI eBook is ingested and split into smaller text chunks.
2. Gemini Embeddings convert each chunk into vector representations.
3. The vectors are stored in Pinecone for semantic search.
4. When a user asks a question, the query is embedded using the same embedding model.
5. Pinecone retrieves the most relevant document chunks based on vector similarity.
6. LangGraph orchestrates the retrieval and generation workflow.
7. Gemini Flash receives the retrieved context and generates an answer grounded only in the retrieved content.
8. FastAPI exposes the chatbot as a REST API, while Streamlit provides an interactive user interface.

This workflow ensures that responses remain grounded in the uploaded knowledge base rather than relying solely on the LLM's general knowledge.

---

# 🎯 Assignment Deliverables

This project satisfies all requirements of the AI Engineer Internship assignment.

- ✅ PDF ingestion and chunking
- ✅ Gemini text embeddings
- ✅ Pinecone vector database
- ✅ LangGraph RAG workflow
- ✅ Grounded answer generation
- ✅ FastAPI REST API
- ✅ Streamlit chat interface
- ✅ Retrieved context returned with every response
- ✅ Similarity (confidence) scores displayed
- ✅ Sample queries included
- ✅ Architecture explanation provided

---

# 🔮 Future Improvements

Potential enhancements include:

- Conversation memory
- Multi-PDF support
- Source highlighting within responses
- Streaming token-by-token responses
- User authentication
- Docker deployment
- Cloud deployment (AWS, Azure, or GCP)
- Advanced evaluation metrics
- Hybrid keyword + semantic search

---

# 👨‍💻 Author

**Pratham Pasi**

AI Engineer | Python Developer | Building AI, Data Analytics, and Intelligent Applications

GitHub: https://github.com/pratham133

---

# ⭐ Acknowledgements

This project was developed as part of the **AI Engineer Intern Technical Assignment**.

Technologies used:

- Google Gemini
- LangGraph
- Pinecone
- FastAPI
- Streamlit
- LangChain

---

If you found this project helpful, consider giving it a ⭐ on GitHub.

