import streamlit as st

if st.session_state.role == "Recruiter":
    if st.session_state.pdf == 1:
        for i in range(len(st.session_state.name)):
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