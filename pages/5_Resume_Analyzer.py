import streamlit as st
from utils.session import init_session
from models.resume import extract_text, analyze_resume

init_session()

if not st.session_state.logged_in:
    st.warning("Please Login First")
    st.stop()

st.title("📄 AI Resume Analyzer")
st.caption("Powered by Gemini AI • AI Smart Suite")
st.write("Upload your Resume (PDF)")

uploaded_file = st.file_uploader(
    "Choose Resume",
    type=["pdf"]
)

if uploaded_file:

    st.success("Resume Uploaded Successfully")

    if st.button("Analyze Resume"):

        with st.spinner("Analyzing Resume..."):

            resume_text = extract_text(uploaded_file)

            result = analyze_resume(resume_text)

        st.success("Analysis Completed")

        st.markdown(result)

        st.session_state.analytics["Resume"] += 1