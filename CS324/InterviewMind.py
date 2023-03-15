import streamlit as st
from streamlit.components.v1 import html
st.set_page_config(page_title="InterviewMind")

with st.sidebar:
    st.markdown("""
    # About 
    InterviewMind is a tool built on GPT-3 to automate the interview workflow. 
    """)

st.sidebar.title("Select a profile:")
profile = st.sidebar.radio("", ("Applicant", "Recruiter"))
st.session_state.role = profile