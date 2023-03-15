import streamlit as st
import openai
import pdfplumber

def extract_text(file):
    text = []
    with pdfplumber.open(file) as pdf:
        pages = pdf.pages
        for p in pages:
            text.append(p.extract_text())
    return text

if st.session_state.role == "Applicant":
    uploaded_file = st.file_uploader('Choose your .pdf file', type="pdf")
    if uploaded_file is not None:
        text = extract_text(uploaded_file)
        text = ''.join(text)
        st.info(text)
        st.session_state.pdf = 1
        openai.api_key = "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"
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="Answer with the name of this person based on their resume: " + text,
            temperature=0.5,
            max_tokens=150,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        output = response['choices'][0]['text']
        st.info(output)
        st.session_state.name = output
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="Answer with the college, major, and GPA of this person based on their resume: " + text,
            temperature=0.5,
            max_tokens=150,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        output = response['choices'][0]['text']
        st.info(output)
        st.session_state.education = output
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="Answer with the work history of this person based on their resume: " + text,
            temperature=0.5,
            max_tokens=150,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        output = response['choices'][0]['text']
        st.info(output)
        st.session_state.work = output
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="Answer with the technical skills of this person based on their resume: " + text,
            temperature=0.5,
            max_tokens=150,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        output = response['choices'][0]['text']
        st.info(output)
        st.session_state.skills = output
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="Answer with the contact information of this person based on their resume: " + text,
            temperature=0.5,
            max_tokens=150,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        output = response['choices'][0]['text']
        st.info(output)
        st.session_state.contact = output
else:
    st.write("Sorry, recruiters don't have access to this page. Please change your role on the home page if you want to use this feature.")