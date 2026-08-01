"""
Modern Streamlit Chat UI

Agentic AI RAG Chatbot
"""

import requests
import streamlit as st

# =====================================================
# Configuration
# =====================================================

API_URL = st.secrets.get(
    "API_URL",
    "https://agentic-ai-rag-chatbot-vz1l.onrender.com/chat",
)

st.set_page_config(
    page_title="Agentic AI RAG",
    page_icon="🤖",
    layout="wide",
)

# =====================================================
# Custom CSS
# =====================================================

st.markdown(
    """
<style>

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
    max-width:1100px;
}

h1{
    font-weight:800;
}

div[data-testid="stChatMessage"]{
    border-radius:18px;
    padding:15px;
    margin-bottom:12px;
    border:1px solid rgba(200,200,200,.20);
}

div[data-testid="stExpander"]{
    border-radius:14px;
    border:1px solid rgba(200,200,200,.20);
}

div[data-testid="metric-container"]{
    border-radius:14px;
    padding:12px;
}

section[data-testid="stSidebar"]{
    border-right:1px solid rgba(255,255,255,.08);
}

</style>
""",
    unsafe_allow_html=True,
)

# =====================================================
# Session State
# =====================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

# =====================================================
# Sidebar
# =====================================================

with st.sidebar:

    st.title("🤖 Agentic AI RAG")

    st.caption("Enterprise Retrieval-Augmented AI Assistant")

    st.divider()

    st.subheader("📌 About")

    st.write(
        """
This chatbot answers questions **strictly from the uploaded Agentic AI eBook**
using a Retrieval-Augmented Generation (RAG) pipeline.

Responses are generated only after retrieving relevant context from Pinecone.
"""
    )

    st.divider()

    st.subheader("⚙️ AI Stack")

    st.markdown(
        """
🧠 **LLM:** Gemini Flash Latest

🔍 **Vector Database:** Pinecone

📑 **Embeddings:** Gemini Embeddings

🔗 **Workflow:** LangGraph

⚡ **Backend:** FastAPI

🎨 **Frontend:** Streamlit
"""
    )

    st.divider()

    st.subheader("📊 Project Stats")

    col1, col2 = st.columns(2)

    col1.metric("Top Chunks", "4")
    col2.metric("Source", "PDF")

    st.metric("Knowledge Base", "Agentic AI eBook")

    st.success("✅ Pinecone Connected")
    st.success("✅ Gemini Connected")
    st.success("✅ LangGraph Active")
    st.success("✅ FastAPI Running")

    st.divider()

    if st.button("🗑 Clear Chat"):
        st.session_state.messages.clear()
        st.rerun()

    st.divider()

    st.caption(
        "Built with ❤️ using Streamlit, FastAPI, LangGraph, Gemini and Pinecone."
    )

# =====================================================
# Main Page
# =====================================================

st.title("🤖 Agentic AI RAG Chatbot")

st.markdown(
    """
### Intelligent Question Answering over your PDF Knowledge Base

Ask natural language questions and receive grounded answers generated using:

- 🧠 Gemini Flash
- 🔍 Pinecone Semantic Search
- 🔗 LangGraph Workflow
- ⚡ FastAPI Backend
"""
)

st.divider()

# =====================================================
# Display Previous Messages
# =====================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        if message["role"] == "assistant" and "contexts" in message:

            with st.expander("📚 Retrieved Sources"):

                for doc in message["contexts"]:

                    st.markdown(
                        f"""
**📄 Page {doc['page']}**

Similarity Score: **{doc['score']:.3f}**
"""
                    )

                    st.write(doc["text"])

                    st.divider()

# =====================================================
# Chat Input
# =====================================================

question = st.chat_input("Ask anything about Agentic AI...")

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner(
            "🔍 Searching Pinecone...\n\n🧠 Asking Gemini...\n\n✨ Generating grounded response..."
        ):

            try:

                response = requests.post(
                    API_URL,
                    json={"question": question},
                    timeout=60,
                )

                if response.status_code != 200:

                    try:
                        error = response.json().get("detail", "Unknown Error")
                    except Exception:
                        error = response.text

                    st.error(error)

                else:

                    data = response.json()

                    st.markdown(data["answer"])

                    with st.expander("📚 Retrieved Sources"):

                        for doc in data["contexts"]:

                            st.markdown(
                                f"""
**📄 Page {doc['page']}**

Similarity Score: **{doc['score']:.3f}**
"""
                            )

                            st.write(doc["text"])

                            st.divider()

                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": data["answer"],
                            "contexts": data["contexts"],
                        }
                    )

            except requests.exceptions.RequestException as e:

                st.error(
                    f"❌ Unable to connect to the backend.\n\n{e}"
                )

# =====================================================
# Footer
# =====================================================

st.divider()

st.caption(
    "© 2026 • Agentic AI RAG Chatbot • Built for the AI Engineer Intern Assignment using LangGraph, Pinecone, Gemini and FastAPI."
)