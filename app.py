import streamlit as st
from transformers import pipeline

def generate_response(input_text, chat_history):
    chatbot_model = pipeline("text-generation", model="microsoft/DialoGPT-medium")
    chat_history.append(input_text)
    response = chatbot_model(chat_history)
    generated_text = response[0]['generated_text']
    return generated_text

def chat():
    st.title("Ka Chatbot")
    st.write("Welcome! I'm Ka, your friendly chatbot. How can I assist you today?")

    chat_history = []

    while True:
        user_input = st.text_input("User:")
        if user_input.lower() in ["exit", "quit"]:
            st.write("Ka: Goodbye! Have a great day!")
            break

        response = generate_response(user_input, chat_history)
        chat_history.append(user_input)
        st.write("Ka:", response)

chat()
