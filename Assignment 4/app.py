import os
from dotenv import load_dotenv
import streamlit as st
from groq import Groq

# Load environment variables
load_dotenv()

# Fetch API key
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    st.error("GROQ_API_KEY not found in .env file")
    st.stop()

# Initialize Groq client
client = Groq(api_key=api_key)

MODEL_NAME = "llama-3.1-8b-instant"

# Streamlit page config
st.set_page_config(page_title="Groq Q&A Chatbot", page_icon="🤖")

st.title("🤖 Question–Answering Chatbot")
st.caption("Powered by Groq + LLaMA")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful question-answering chatbot."}
    ]

# Display chat history
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Ask a question...")

if user_input:
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    # Call Groq API
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=st.session_state.messages,
        temperature=0.3
    )

    bot_reply = response.choices[0].message.content

    # Display bot message
    with st.chat_message("assistant"):
        st.markdown(bot_reply)

    st.session_state.messages.append(
        {"role": "assistant", "content": bot_reply}
    )