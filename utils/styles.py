import streamlit as st


def load_css():
    st.markdown("""
    <style>

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 3rem;
        padding-right: 3rem;
    }

    .main-title {
        font-size:42px;
        font-weight:bold;
        color:#2563EB;
        text-align:center;
    }

    .subtitle{
        text-align:center;
        color:gray;
        font-size:18px;
    }

    .feature-card{

        background:#F8FAFC;
        border-radius:15px;
        padding:20px;
        border:1px solid #E2E8F0;
        margin-bottom:15px;

        box-shadow:0 5px 15px rgba(0,0,0,.08);

    }

    .feature-title{

        color:#2563EB;
        font-size:20px;
        font-weight:bold;

    }

    .stButton>button{

        width:100%;
        height:48px;

        border-radius:12px;

        background:#2563EB;

        color:white;

        border:none;

        font-weight:bold;

        font-size:16px;

    }

    .stButton>button:hover{

        background:#1D4ED8;

        color:white;

    }

    div[data-testid="stMetric"]{

        border-radius:12px;

        border:1px solid #E5E7EB;

        padding:15px;

        background:white;

        box-shadow:0 3px 10px rgba(0,0,0,.08);

    }

    </style>
    """, unsafe_allow_html=True)