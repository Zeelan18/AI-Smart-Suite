import streamlit as st
from models.summarizer import summarize_text
from utils.session import init_session

init_session()

if not st.session_state.get("logged_in", False):
    st.warning("Please login first.")
    st.stop()

st.title("📝 AI Text Summarizer")
st.caption("Powered by Gemini AI • AI Smart Suite")

summary_type = st.selectbox(
    "Summary Type",
    ["Short", "Medium", "Detailed"]
)

text = st.text_area(
    "Paste your text here",
    height=250
)

if st.button("Generate Summary"):

    if text.strip():

        with st.spinner("Generating summary..."):

            summary = summarize_text(text, summary_type)

        st.success("Summary Generated")

        st.markdown("### Summary")

        st.write(summary)

        if "analytics" in st.session_state:
            st.session_state.analytics["Summary"] += 1

    else:
        st.warning("Please enter some text.")