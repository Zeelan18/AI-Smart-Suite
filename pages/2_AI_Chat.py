import streamlit as st
from models.chat_model import get_response
from utils.session import init_session

init_session()

# Login check
if not st.session_state.get("logged_in", False):
    st.warning("Please login first.")
    st.stop()

# Chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("💬 AI Chat Assistant")
st.caption("Powered by Gemini AI • AI Smart Suite")

prompt = st.chat_input("Ask me anything...")

if prompt:

    # User message
    st.session_state.chat_history.append(("You", prompt))

    # AI response
    response = get_response(prompt)

    st.session_state.chat_history.append(("AI", response))

    # Analytics
    if "analytics" in st.session_state:
        st.session_state.analytics["Chat"] += 1

# Display history
for sender, message in st.session_state.chat_history:

    if sender == "You":
        with st.chat_message("user"):
            st.write(message)

    else:
        with st.chat_message("assistant"):
            st.write(message)

# Clear chat
if st.button("🗑 Clear Chat"):
    st.session_state.chat_history = []
    st.rerun()