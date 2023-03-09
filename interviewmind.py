import streamlit as st
import openai
from streamlit.components.v1 import html
st.set_page_config(page_title="InterviewMind")


html_temp = """
                <div style="background-color:{};padding:1px">
                
                </div>
                """

with st.sidebar:
    st.markdown("""
    # About 
    InterviewMind is a tool built on GPT-3 to automate the interview workflow. 
    """)


input_text = None
if 'output' not in st.session_state:
    st.session_state['output'] = 0

if st.session_state['output'] <=2:
    st.markdown("""
    # Interview Questions
    """)
    input_text = st.text_input("Prompt")
    st.session_state['output'] = st.session_state['output'] + 1
else:
    st.info("Refresh for another prompt")

hide="""
<style>
footer{
	visibility: hidden;
    position: relative;
}
.viewerBadge_container__1QSob{
    visibility: hidden;
}
#MainMenu{
	visibility: hidden;
}
<style>
"""
st.markdown(hide, unsafe_allow_html=True)

st.markdown(
    """
    <style>
        iframe[width="220"] {
            position: fixed;
            bottom: 60px;
            right: 40px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
if input_text:
    prompt = "prompt"
    if prompt:
        openai.api_key = "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"
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="Create a list of 8 questions for a software engineering job interview",
            temperature=0.5,
            max_tokens=150,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        output = response['choices'][0]['text']
        st.info(output)