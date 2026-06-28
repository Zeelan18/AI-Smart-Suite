import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    try:
        api_key = st.secrets["GOOGLE_API_KEY"]
    except Exception:
        api_key = None

if not api_key:
    st.error("""
❌ Google API Key not found.

For Local:
Create a .env file with

GOOGLE_API_KEY=YOUR_API_KEY

For Streamlit Cloud:
Go to

App Settings → Secrets

Add

GOOGLE_API_KEY="YOUR_API_KEY"
""")
    st.stop()

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")