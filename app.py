import streamlit as st
from groq import Groq

st.set_page_config(page_title = "Placement Practice", layout="centered")
st.title("AI Placement Assistant")
st.caption("Practice and Prepare for your Interviews")

try:
    client = Groq(api_key = st.secrets["GROQ_API_KEY"])
except (KeyError, FileNotFoundError):
    st.error("API Key is missing. Add it in Advanced settings")
    st.stop()
    role = st.selectbox('Job Title',['Machine Learning Engineer','Data Analyst','Prompt Engineer','DevOps Engineer','other'])
  
