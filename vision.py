from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
from PIL import Image
import google.generativeai as gai

gai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = gai.GenerativeModel('gemini-2.5-pro')

def get_gemini_response(question, image):
    try:
        if question != "":
            response = model.generate_content([question, image])
        else:
            response = model.generate_content(["Describe this image", image])

        if response.parts:
            return response.text
        else:
            return "I'm sorry, I couldn't generate a response."
    except Exception as e:
        return f"An error occurred: {e}"

st.set_page_config(page_title="Gemini Vision Q&A", layout="wide")

st.header("Interactive Image Q&A with Gemini")

# Get a text input from the user for the question.
input_text = st.text_input("Ask a question about the image:", placeholder="Enter your question here")

# Let the user upload an image file.
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# If an image file is uploaded, open and display the image.
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # When the "Get Answer" button is clicked, generate a response using the provided question and image.
    if st.button("Get Answer"):
        # Call the function to get the response from Gemini.
        response = get_gemini_response(input_text, image)
        st.subheader("Answer:")
        st.write(response)