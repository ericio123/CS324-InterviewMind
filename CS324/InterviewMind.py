import streamlit as st
import openai
import pdfplumber
from streamlit.components.v1 import html
st.set_page_config(page_title="InterviewMind")

with st.sidebar:
    st.markdown("""
    # About 
    InterviewMind is a tool built on GPT-3 to automate the interview workflow. 
    """)

def extract_text(file):
    text = []
    with pdfplumber.open(file) as pdf:
        pages = pdf.pages
        for p in pages:
            text.append(p.extract_text())
    return text

uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")
if uploaded_file is not None:
    text = extract_text(uploaded_file)
    text = ''.join(text)
    #text.replace('\n', '  \n')
    st.info(text)

_ = '''
input_text = None
if 'output' not in st.session_state:
    st.session_state['output'] = 0

if st.session_state['output'] <=2:
    st.markdown("""
    # Enter a prompt here
    """)
    input_text = st.text_input("Prompt")
    st.session_state['output'] += 1
else:
    st.info("Refresh for another prompt")

if input_text:
    prompt = input_text
    if prompt:
        openai.api_key = "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"
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.5,
            max_tokens=150,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        output = response['choices'][0]['text']
        st.info(output)
'''