import streamlit as st
from streamlit.components.v1 import html
st.set_page_config(page_title="InterviewMind")

@st.cache_data
def ini():
    st.session_state.role = "Applicant"
    st.session_state.pdf = 0

ini()

with st.sidebar:
    st.markdown("""
    # About 
    InterviewMind is a tool built on GPT-3 to automate the interview workflow. 
    """)

if st.session_state.role == "Applicant":
    index = 0
else:
    index = 1
profile = st.sidebar.radio("Select a profile", ("Applicant", "Recruiter"), index=index)
st.session_state.role = profile