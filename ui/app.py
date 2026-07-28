"""
Professional Streamlit Frontend

Agentic AI RAG Chatbot
"""

import requests
import streamlit as st


# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="Agentic AI RAG Chatbot",
    page_icon="🤖",
    layout="wide",
)


# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.title("🤖 Agentic AI RAG")

    st.markdown("---")

    st.subheader("📌 About")

    st.info(
        """
This chatbot uses Retrieval-Augmented Generation (RAG)
to answer questions from your uploaded PDF knowledge base.

### Tech Stack

- 🧠 Gemini
- 🔍 Pinecone
- 🔗 LangGraph
- ⚡ FastAPI
- 🎨 Streamlit

---

### Workflow

PDF

⬇

Pinecone

⬇

Retriever

⬇

LangGraph

⬇

Gemini

⬇

Answer
"""
    )

    st.markdown("---")

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()


# =====================================================
# CHAT HISTORY
# =====================================================

if "messages" not in st.session_state:
    st.session_state.messages = []


# =====================================================
# TITLE
# =====================================================

st.title("🤖 Agentic AI RAG Chatbot")

st.caption(
    "Powered by Gemini • Pinecone • LangGraph • FastAPI"
)


API_URL = "http://127.0.0.1:8000/chat"


# =====================================================
# DISPLAY OLD CHAT
# =====================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# =====================================================
# CHAT INPUT
# =====================================================

question = st.chat_input(
    "Ask anything about Agentic AI..."
)


# =====================================================
# SEND QUESTION
# =====================================================

if question:

    # Show user message

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    with st.chat_message("user"):

        st.markdown(question)

    # Assistant response

    with st.chat_message("assistant"):

        with st.spinner("Searching knowledge base..."):

            try:

                response = requests.post(
                    API_URL,
                    json={
                        "question": question
                    },
                    timeout=60,
                )

                if response.status_code != 200:

                    st.error("Backend Error")

                    st.code(response.text)

                else:

                    data = response.json()

                    answer = data["answer"]

                    st.markdown(answer)

                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": answer,
                        }
                    )

                    st.divider()

                    st.subheader("📚 Retrieved Sources")

                    for doc in data["contexts"]:

                        with st.expander(
                            f"📄 Page {doc['page']} | Score {doc['score']:.3f}"
                        ):

                            st.write(doc["text"])

            except Exception as e:

                st.error(str(e))


# =====================================================
# FOOTER
# =====================================================

st.markdown("---")

st.caption(
    "Built with ❤️ using Streamlit, FastAPI, LangGraph, Gemini and Pinecone."
)