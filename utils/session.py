import streamlit as st


def init_session():
    """Initialize all session state variables."""

    defaults = {
        "logged_in": False,
        "username": "",
        "chat_history": [],
        "analytics": {
            "Chat": 0,
            "Summary": 0,
            "Sentiment": 0,
            "Resume": 0,
        },
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value