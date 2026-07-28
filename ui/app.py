"""
Streamlit Frontend

Simple ChatGPT-style interface for the RAG chatbot.
"""

import streamlit as st
import requests


# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="Agentic AI RAG Chatbot",
    page_icon="🤖",
    layout="wide",
)


# -------------------------------------------------
# Title
# -------------------------------------------------

st.title("🤖 Agentic AI RAG Chatbot")

st.write(
    "Ask questions about Agentic AI using your uploaded knowledge base."
)


# -------------------------------------------------
# Backend API
# -------------------------------------------------

API_URL = "http://127.0.0.1:8000/chat"


# -------------------------------------------------
# User Input
# -------------------------------------------------

question = st.text_input(
    "Ask your question:"
)


# -------------------------------------------------
# Ask Button
# -------------------------------------------------

if st.button("Ask"):

    if not question.strip():

        st.warning("Please enter a question.")

    else:

        with st.spinner("Thinking..."):

            try:
                response = requests.post(
                    API_URL,
                    json={
                        "question": question
                    }
                )

                # -------------------------------------
                # DEBUG INFORMATION
                # -------------------------------------

                st.subheader("Debug Information")

                st.write("Status Code:")
                st.write(response.status_code)

                data = response.json()

                st.write("API Response:")
                st.json(data)

                # -------------------------------------
                # Only continue if successful
                # -------------------------------------

                if response.status_code != 200:

                    st.error("Backend returned an error.")

                else:

                    st.subheader("Answer")

                    st.write(data["answer"])

                    st.subheader("Retrieved Sources")

                    for doc in data["contexts"]:

                        st.markdown(
                            f"### 📄 Page {doc['page']}"
                        )

                        st.write(doc["text"])

                        st.caption(
                            f"Similarity Score: {doc['score']:.4f}"
                        )

                        st.divider()

            except Exception as e:

                st.error(str(e))