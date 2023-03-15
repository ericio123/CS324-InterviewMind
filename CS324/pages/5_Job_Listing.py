import streamlit as st

for i in range(len(st.session_state.job_title)):
    st.write("Job Title")
    st.info(st.session_state.job_title[i])
    st.write("Job Description")
    st.info(st.session_state.job_descriptions[i])
    st.markdown("""***""")