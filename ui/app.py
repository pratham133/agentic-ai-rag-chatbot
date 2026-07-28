"""
Streamlit Frontend

Professional UI for the Agentic AI RAG Chatbot.
"""

import requests
import streamlit as st


# ==================================================
# Page Configuration
# ==================================================

st.set_page_config(
    page_title="Agentic AI RAG Chatbot",
    page_icon="🤖",
    layout="wide",
)

# ==================================================
# Sidebar
# ==================================================

with st.sidebar:

    st.title("🤖 Agentic AI RAG")

    st.markdown("---")

    st.markdown("### 📌 About")

    st.write(
        """
This chatbot answers questions using:

- 📄 PDF Knowledge Base
- 🧠 Gemini LLM
- 🔍 Pinecone Vector Search
- 🔗 LangGraph Workflow
- ⚡ FastAPI Backend
- 🎨 Streamlit Frontend
"""
    )

    st.markdown("---")

    st.info(
        "Ask any question related to the uploaded Agentic AI document."
    )

# ==================================================
# Main Page
# ==================================================

st.title("🤖 Agentic AI RAG Chatbot")

st.caption(
    "Powered by Gemini • Pinecone • LangGraph • FastAPI"
)

st.write("")

# ==================================================
# Backend
# ==================================================

API_URL = "http://127.0.0.1:8000/chat"

# ==================================================
# User Question
# ==================================================

question = st.text_input(
    "Ask your question",
    placeholder="Example: What is Agentic AI?"
)

# ==================================================
# Ask Button
# ==================================================

if st.button(
    "Ask",
    use_container_width=True,
):

    if question.strip() == "":

        st.warning("Please enter a question.")

    else:

        with st.spinner("Searching knowledge base..."):

            try:

                response = requests.post(
                    API_URL,
                    json={
                        "question": question
                    }
                )

                if response.status_code != 200:

                    st.error("Backend Error")

                    st.json(response.json())

                else:

                    data = response.json()

                    st.success("Answer generated successfully!")

                    st.markdown("## 💡 Answer")

                    st.write(data["answer"])

                    st.markdown("---")

                    st.markdown("## 📚 Retrieved Sources")

                    for index, doc in enumerate(
                        data["contexts"],
                        start=1,
                    ):

                        with st.expander(
                            f"Document {index} | Page {doc['page']} | Score {doc['score']:.3f}"
                        ):

                            st.write(doc["text"])

            except Exception as e:

                st.error(str(e))