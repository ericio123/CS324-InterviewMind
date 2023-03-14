import streamlit as st

if st.session_state.pdf == 1:
    st.info(st.session_state.name)
    st.info(st.session_state.education)
    st.info(st.session_state.skills)
    st.info(st.session_state.contact)