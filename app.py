import streamlit as st
from transformers import AutoTokenizer, AutoModelForQuestionAnswering

@st.cache(allow_output_mutation=True)
def load_model():
    model_name = "shivam001/deibotquestion"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForQuestionAnswering.from_pretrained(model_name)
    return tokenizer, model

def answer_question(question, tokenizer, model):
    inputs = tokenizer.encode_plus(question, add_special_tokens=True, return_tensors="pt")
    input_ids = inputs["input_ids"].tolist()[0]

    with torch.no_grad():
        outputs = model(**inputs)

    answer_start = torch.argmax(outputs.start_logits)
    answer_end = torch.argmax(outputs.end_logits) + 1
    answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(input_ids[answer_start:answer_end]))

    return answer

def main():
    st.title("Question Answering Chatbot")
    question = st.text_input("Question:", "Enter your question here...")

    if st.button("Answer"):
        if question:
            tokenizer, model = load_model()
            answer = answer_question(question, tokenizer, model)
            st.write("Answer:", answer)
        else:
            st.write("Please enter a question.")

if __name__ == "__main__":
    main()
