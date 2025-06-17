import streamlit as st
import openai
import os

# Set your OpenAI API key here or use environment variable
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="ChatGPT Personal Assistant", layout="centered")
st.title("🧠 ChatGPT Personal Assistant")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display conversation history
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

# Chat input
prompt = st.chat_input("Ask me anything...")

if prompt:
    # Add user message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get GPT response
    with st.spinner("Thinking..."):
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=st.session_state.messages,
            temperature=0.7,
        )
        reply = response.choices[0].message.content

    # Display GPT reply
    st.chat_message("assistant").markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
