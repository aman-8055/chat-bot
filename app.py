import streamlit as st
from transformers import pipeline

def generate_response(input_text):
    # Load the pre-trained Hugging Face model
    chatbot_model = pipeline("text-generation", model="microsoft/DialoGPT-medium")

    # Generate a response from the chatbot model
    response = chatbot_model(input_text)[0]['generated_text']
    return response

def chat():
    st.title("Ka Chatbot")
    st.write("Welcome! I'm Ka, your friendly chatbot. How can I assist you today?")

    while True:
        user_input = st.text_input("User:")
        if user_input.lower() in ["exit", "quit"]:
            st.write("Ka: Goodbye! Have a great day!")
            break

        response = generate_response(user_input)
        st.write("Ka:", response)

chat()
