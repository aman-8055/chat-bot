import streamlit as st
from transformers import AutoTokenizer, AutoModelForQuestionAnswering

# Load pre-trained model and tokenizer
model_name = "distilbert-base-uncased-distilled-squad"  # Replace with your desired model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)

# Streamlit app code
def answer_question(context, question):
    inputs = tokenizer.encode_plus(question, context, add_special_tokens=True, return_tensors="pt")
    input_ids = inputs["input_ids"].tolist()[0]

    # Get the start and end logits for the answer
    with torch.no_grad():
        start_logits, end_logits = model(**inputs).logits

    start_index = torch.argmax(start_logits, dim=1).item()
    end_index = torch.argmax(end_logits, dim=1).item()

    # Convert the token IDs back to text
    answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(input_ids[start_index:end_index+1]))

    return answer

def main():
    st.title("Question Answering Chatbot")
    context = st.text_area("Context:", "Enter the context here...")
    question = st.text_input("Question:", "Enter your question here...")

    if st.button("Answer"):
        if context and question:
            answer = answer_question(context, question)
            st.write("Answer:", answer)
        else:
            st.write("Please enter both context and question.")

if __name__ == "__main__":
    main()
