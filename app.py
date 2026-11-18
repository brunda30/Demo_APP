import streamlit as st
from groq import Groq
st.set_page_config(page_title = "Placement practice", layout = "centered")
st.title("AI Placement Assistant")
st.caption("Practice and prepare for your Interviews")
try:
  client = Groq(api_key = st.secrets["GROQ_API_KEY"])
except (KeyError, FileNotFound):
  st.error("API key is missing.Add it in Advanced settings")
  st.stop()
