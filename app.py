from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as gai

gai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = gai.GenerativeModel("gemini-2.5-pro")

def get_gemini_response(question):
    try:
        response = model.generate_content(question)
        if response.parts:
            return response.text
        else:
            return "I'm sorry, I couldn't generate a response."
    except Exception as e:
        return f"An error occurred: {e}"

st.set_page_config(page_title="Gemini Q&A", layout="wide")

st.header("Interactive Q&A with Gemini")

input_text = st.text_input("Ask your question:", key="input_question", placeholder="Type your question here...")



if st.button("Get Answer"):
    if input_text:
        st.write(get_gemini_response(input_text))
    else:
        st.warning("Please enter a question.")
