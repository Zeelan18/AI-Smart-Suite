import streamlit as st
import pandas as pd
import plotly.express as px
from utils.session import init_session

# -----------------------
# Initialize Session
# -----------------------
init_session()

if not st.session_state.logged_in:
    st.warning("Please Login First")
    st.stop()

st.title("📊 Usage Analytics")
st.caption("Powered by Gemini AI • AI Smart Suite")

st.write("Track the usage of each AI module.")

analytics = st.session_state.analytics

# Convert to DataFrame
df = pd.DataFrame({
    "Module": analytics.keys(),
    "Usage": analytics.values()
})

# Metrics
col1, col2 = st.columns(2)

with col1:
    st.metric("Total Requests", int(df["Usage"].sum()))

with col2:
    st.metric("Modules Used", int((df["Usage"] > 0).sum()))

st.divider()

# Bar Chart
st.subheader("📈 Module Usage")

fig = px.bar(
    df,
    x="Module",
    y="Usage",
    text="Usage",
    title="AI Module Usage"
)

st.plotly_chart(fig, use_container_width=True)

# Pie Chart
st.subheader("🥧 Usage Distribution")

fig2 = px.pie(
    df,
    names="Module",
    values="Usage",
    hole=0.5
)

st.plotly_chart(fig2, use_container_width=True)

st.divider()

st.subheader("📋 Usage Table")

st.dataframe(df, use_container_width=True)

if st.button("🔄 Reset Analytics"):
    st.session_state.analytics = {
        "Chat": 0,
        "Summary": 0,
        "Sentiment": 0,
        "Resume": 0,
    }
    st.success("Analytics Reset Successfully!")
    st.rerun()