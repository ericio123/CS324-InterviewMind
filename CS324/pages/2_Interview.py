import streamlit as st

st.info(st.session_state.role)
if st.session_state.role == "Recruiter":
    st.info("interview")
else:
    st.write("Sorry, applicants don't have access to this page. Please change your role on the home page if you want to use this feature.")