import streamlit as st
from transformers import pipeline

def generate_response(input_text):
    chatbot_model = pipeline("text-generation", model="microsoft/DialoGPT-medium")
    response = chatbot_model(input_text)[0]['generated_text']
    return response

def chat():
    st.title("Ka Chatbot")
    st.write("Welcome! I'm Ka, your friendly chatbot. How can I assist you today?")

    input_counter = 0  # Counter to generate unique keys

    while True:
        user_input = st.text_input(f"User-{input_counter}:")  # Append counter to the key
        if user_input.lower() in ["exit", "quit"]:
            st.write("Ka: Goodbye! Have a great day!")
            break

        response = generate_response(user_input)
        st.write("Ka:", response)

        input_counter += 1  # Increment the counter

chat()
