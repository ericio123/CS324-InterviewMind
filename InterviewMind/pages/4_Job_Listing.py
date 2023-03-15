import streamlit as st

job = st.selectbox("Select which job to show the posting for",(st.session_state.job_title))
if job is not None:
    for i in range(len(st.session_state.job_title)):
        if st.session_state.job_title[i] == job:
            st.write("Job Title")
            st.info(st.session_state.job_title[i])
            st.write("Job Description")
            st.info(st.session_state.job_descriptions[i])
            st.markdown("""***""")