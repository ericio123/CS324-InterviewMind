import streamlit as st

if st.session_state.role == "Recruiter":
    st.info("interview")
else:
    st.write("Sorry, applicants don't have access to this page. Please change your role on the home page if you want to use this feature.")