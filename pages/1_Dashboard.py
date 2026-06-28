import streamlit as st
from utils.session import init_session

init_session()

if not st.session_state.logged_in:
    st.warning("Please Login First")
    st.stop()

st.title("🤖 AI Smart Suite")
st.caption("Powered by Gemini AI • AI Smart Suite")

st.caption("One Platform • Multiple AI Tools")

st.divider()

st.success(f"Welcome, {st.session_state.username} 👋")

st.write("### 🚀 Available AI Modules")

col1,col2=st.columns(2)

with col1:

    st.info("💬 AI Chat Assistant")

    st.info("📝 Text Summarizer")

    st.info("😊 Sentiment Analysis")

with col2:

    st.info("📄 Resume Analyzer")

    st.info("📊 Usage Analytics")

    st.info("🔐 Secure Login")

st.divider()

st.write("## 📈 Today's Usage")

c1,c2,c3,c4=st.columns(4)

with c1:
    st.metric("Chat",st.session_state.analytics["Chat"])

with c2:
    st.metric("Summary",st.session_state.analytics["Summary"])

with c3:
    st.metric("Sentiment",st.session_state.analytics["Sentiment"])

with c4:
    st.metric("Resume",st.session_state.analytics["Resume"])

st.divider()

st.write("### 🎯 Project Highlights")

st.markdown("""
✅ AI Chat Assistant

✅ Text Summarizer

✅ Sentiment Analysis

✅ Resume Analyzer

✅ Usage Analytics

✅ Modern Dashboard

✅ Gemini AI Integration

✅ Streamlit Interface
""")

st.divider()

if st.button("Logout"):
    st.session_state.logged_in=False
    st.session_state.username=""
    st.rerun()