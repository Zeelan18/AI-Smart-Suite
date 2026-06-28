import streamlit as st
from models.sentiment import analyze_sentiment
from utils.session import init_session

init_session()

if not st.session_state.get("logged_in", False):
    st.warning("Please login first.")
    st.stop()

st.title("😊 Sentiment Analysis")
st.caption("Powered by Gemini AI • AI Smart Suite")

text = st.text_area("Enter text", height=200)

if st.button("Analyze Sentiment"):

    if text.strip():

        with st.spinner("Analyzing..."):

            result = analyze_sentiment(text)

        st.success("Analysis Complete")

        st.markdown(result)

        st.session_state.analytics["Sentiment"] = (
            st.session_state.analytics.get("Sentiment", 0) + 1
        )

    else:
        st.warning("Please enter some text.")