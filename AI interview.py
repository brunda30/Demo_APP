import streamlit as st

# Page configuration
st.set_page_config(
    page_title="LLM",
    layout="centered"
)

# Application title
st.title("AI Interview")
st.caption("Practice and Prepare for your placement.")

# Import Groq safely
try:
    from groq import Groq

except ImportError:
    st.error("Groq package is not installed.")
    st.info("Add groq to your requirements.txt file and redeploy.")
    st.stop()

# API configuration
try:
    client = Groq(
        api_key=st.secrets["GROQ_API_KEY"]
    )

except (KeyError, FileNotFoundError):
    st.error("API key is missing. Add it in Streamlit Secrets.")
    st.stop()

# Success message
st.success("Groq API connected successfully!")

st.write("Welcome to your AI Interview Assistant.")

# Job role
role = st.selectbox(
    "Job Title",
    [
        "Machine Learning Engineer",
        "Senior Software Engineering",
        "Data Analysis",
        "Cyber Security",
        "Software Developer",
        "Others"
    ]
)

if role == "Others":
    role = st.text_input("Enter your Job Title", "XXXXXX")

# Model selection
model = st.selectbox(
    "Choose your model",
    [
        "openai/gpt-oss-120b",
        "openai/gpt-oss-20b"
    ]
)

# Experience level
level = st.selectbox(
    "Choose your level",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)

# Activity selection
mode = st.radio(
    "Activity",
    [
        "General Questions",
        "Generate Code Questions",
        "Evaluate Answers",
        "Improve Answers"
    ]
)

# Input fields
question = ""
answer = ""

if mode in ["Evaluate Answers", "Improve Answers"]:
    question = st.text_area("Enter your Question")
    answer = st.text_area("Enter your Answer")

# Generate AI response
if st.button("Generate AI Response", type="primary"):

    if mode in ["Evaluate Answers", "Improve Answers"]:
        if not question.strip() or not answer.strip():
            st.warning("Please enter a valid Question and Answer.")
            st.stop()

    st.write("Selected Job Role:", role)
    st.write("Selected Model:", model)
    st.write("Experience Level:", level)
    st.write("Selected Activity:", mode)

    st.info("Your inputs are ready for AI processing.")



