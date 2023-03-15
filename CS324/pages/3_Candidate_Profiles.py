import streamlit as st

if st.session_state.role == "Recruiter":
    if st.session_state.pdf == 1:
        st.info(st.session_state.name)
        st.info(st.session_state.education)
        st.info(st.session_state.skills)
        st.info(st.session_state.contact)
else:
    st.write("Sorry, applicants don't have access to this page. Please change your role on the home page if you want to use this feature.")