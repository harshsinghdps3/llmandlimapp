

from dotenv import load_dotenv
load_dotenv()

import os
import streamlit as st
import google.generativeai as gai

# ──────────────────  API-Key Validation  ──────────────────
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("⚠️  GOOGLE_API_KEY missing! .env file mein key add karo phir reload karo.")
    st.stop()

gai.configure(api_key=api_key)

# ──────────────────  Per-Session Gemini Chat  ─────────────
if "gemini_chat" not in st.session_state:
    model = gai.GenerativeModel("gemini-2.5-pro")           # Configurable later
    st.session_state.gemini_chat = model.start_chat(history=[])

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []                      # For UI display only

chat = st.session_state.gemini_chat                         # Shortcut

# ──────────────────  Safe Gemini Call  ──────────────────
def get_gemini_response(prompt: str) -> str:
    """
        Sends the user prompt to Gemini, displays streaming chunks in real-time,
        and finally returns as a single string. Handles API failures gracefully.
    """
    try:
        stream = chat.send_message(prompt, stream=True)
        chunks = []
        for chunk in stream:          # Real-time token stream
            st.write(chunk.text)      # Immediate feedback to user
            chunks.append(chunk.text)
        return "".join(chunks)
    except Exception as err:
        st.error(f"Gemini API error {err}")
        return "Sorry, a technical issue occurred."

# ──────────────────  Streamlit Page Setup  ─────────────────
st.set_page_config(page_title="Gemini Q&A Demo", page_icon="💬", layout="wide")
st.title("💎 Gemini LLM Application")

# ────────────────── User Input (chat-style widget) ────────────────────
user_prompt = st.chat_input("Type your question here…")

# ────────────────── Main Interaction Logic  ─────────────
if user_prompt:
    st.session_state.chat_history.append(("You", user_prompt))  # Store user msg

    with st.spinner("Gemini is thinking…"):                   # UX spinner
        bot_reply = get_gemini_response(user_prompt)

    # Consolidated single bot entry 
    st.session_state.chat_history.append(("Bot", bot_reply))

# ──────────────────  Chat History Rendering  ─────────
st.subheader("📜 Chat History")
for role, msg in st.session_state.chat_history:
    avatar = "🧑" if role == "You" else "🤖"
    st.write(f"{avatar} **{role}**: {msg}")
