import streamlit as st
from utils.session import init_session
from utils.styles import load_css

st.set_page_config(
    page_title="AI Smart Suite",
    page_icon="🤖",
    layout="wide"
)

load_css()
init_session()

if not st.session_state.logged_in:

    st.markdown("<div class='main-title'>🤖 AI Smart Suite</div>", unsafe_allow_html=True)

    st.markdown("<div class='subtitle'>One Platform • Multiple AI Solutions</div>", unsafe_allow_html=True)

    st.write("")

    col1,col2,col3=st.columns([1,2,1])

    with col2:

        st.write("### 🔐 Login")

        username=st.text_input("Username")

        password=st.text_input("Password",type="password")

        if st.button("Login"):

            if username and password:

                st.session_state.logged_in=True

                st.session_state.username=username

                st.rerun()

            else:

                st.error("Please enter username and password.")

else:

    st.success(f"Welcome {st.session_state.username}")

    st.info("Choose an AI module from the sidebar.")