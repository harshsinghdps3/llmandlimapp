from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as gai

# Configure the Gemini API with the key from environment variables
gai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro model and get responses
model = gai.GenerativeModel("gemini-2.5-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    """
    Sends a question to the Gemini model and returns the streaming response.
    """
    response = chat.send_message(question, stream=True)
    return response

# Initialize our Streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Input field and submit button
input_text = st.text_input("Input:", key="input")
submit_button = st.button("Ask the question")

# If the submit button is clicked and there's input
if submit_button and input_text:
    response = get_gemini_response(input_text)
    
    # Add user query to session chat history
    st.session_state['chat_history'].append(("You", input_text))
    
    st.subheader("The Response is")
    # Display the streaming response and add bot's response to history
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

# Display the chat history
st.subheader("The Chat history is")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")