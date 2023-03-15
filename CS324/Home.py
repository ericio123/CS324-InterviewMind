import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="InterviewMind")

@st.cache_data
def ini():
    st.session_state.role = "Applicant"
    st.session_state.pdf = 0
    st.session_state.name = []
    st.session_state.education = []
    st.session_state.work = []
    st.session_state.skills = []
    st.session_state.contact = []
    st.session_state.job_title = []
    st.session_state.job_descriptions = []

ini()

with st.sidebar:
    st.markdown("""
    # About 
    InterviewMind is a tool built on GPT-3 to automate the interview workflow. 
    """)

st.title("InterviewMind")
st.write("InterviewMind is a tool built on GPT-3 to automate the interview workflow. For more information check out our blog post at URL.")

if st.session_state.role == "Applicant":
    index = 0
else:
    index = 1
profile = st.sidebar.radio("Select a profile", ("Applicant", "Recruiter"), index=index)
st.session_state.role = profile