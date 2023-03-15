import streamlit as st

if st.session_state.role == "Recruiter":
    job = st.selectbox("Select which job to show applications for",(st.session_state.job_title))
    if job is not None:
        applicants = []
        for i in range(len(st.session_state.name)):
            if st.session_state.resume_job[i] == job:
                applicants.append(st.session_state.name[i])
        applicant = st.selectbox("Select which applicant to show a profile for",(applicants))
        if applicant is not None:
            for i in range(len(st.session_state.name)):
                if st.session_state.name[i] == applicant:
                    st.write("Name")
                    st.info(st.session_state.name[i])
                    st.write("Education")
                    st.info(st.session_state.education[i])
                    st.write("Skills")
                    st.info(st.session_state.skills[i])
                    st.write("Contact Information")
                    st.info(st.session_state.contact[i])
                    st.markdown("""***""")
else:
    st.write("Sorry, applicants don't have access to this page. Please change your role on the home page if you want to use this feature.")