import streamlit as st

st.set_page_config(page_title="InterviewMind")

@st.cache_data
def ini():
    st.session_state.role = "Applicant"
    st.session_state.resume_job = []
    st.session_state.name = []
    st.session_state.education = []
    st.session_state.work = []
    st.session_state.skills = []
    st.session_state.contact = []
    st.session_state.job_title = []
    st.session_state.job_descriptions = []
    st.session_state.bh_interviews = {}
    st.session_state.tc_interviews = {}

ini()

st.title("InterviewMind")
st.write("InterviewMind is a tool built on GPT-3 to automate the interview workflow for both applicants and recruiters. For more information check out our blog post at URL. Use the sidebar on the left to select a role and gain access to the relevant pages and features.")

if st.session_state.role == "Applicant":
    index = 0
else:
    index = 1
profile = st.sidebar.radio("Select a profile", ("Applicant", "Recruiter"), index=index)
st.session_state.role = profile