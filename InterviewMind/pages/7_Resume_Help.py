import streamlit as st
import openai
import pdfplumber

openai.api_key = "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"

def extract_text(file):
    text = []
    with pdfplumber.open(file) as pdf:
        pages = pdf.pages
        for p in pages:
            text.append(p.extract_text())
    return text

if st.session_state.role == "Applicant":
    task = st.radio("Select how you want to add a job posting",("Create a resume","Improve my resume"))
    if task=="Create a resume":
        name = st.text_input("What's your name?")
        education = st.text_input("What's your education background?")
        work = st.text_input("What work experience do you have?")
        skills = st.text_input("What technical skills are you proficient in?")
        contact = st.text_input("What's your contact information?")
        additional = st.text_input("What additional information do you want to add?")
        if st.button("Build a resume for me"):
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt= f"Give me a resume using the following information about me. My name is: {name}. My education background is: {education}. My work experience is: {work}. I'm proficient with: {skills}. My contact information is: {contact}. Additional information about me is: {additional}. Make the resume appealing to job recruiters but do not make up any information about me.",
                temperature=0.5,
                max_tokens=1000,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
            )
            output = response['choices'][0]['text']
            st.write("Here's a custom-built resume for you!")
            st.info(output)
    else:
        uploaded_file = st.file_uploader('Choose the resume .pdf that you want to improve', type="pdf")
        if uploaded_file is not None:
            text = extract_text(uploaded_file)
            text = ''.join(text)
            advice = st.text_input("What do you want improved about your resume?")
            if st.button("Improve my resume for me"):
                response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt= f"Improve the following resume: {text}. Use the following advice to improve the resume: {advice}. Improve the writing quality and grammar of the resume and make it more appealing to recruiters." ,
                    temperature=0.5,
                    max_tokens=1000,
                    top_p=1.0,
                    frequency_penalty=0.0,
                    presence_penalty=0.0
                )
                output = response['choices'][0]['text']
                st.write("Here's an improved resume for you!")
                st.info(output)
else:
    st.write("Sorry, recruiters don't have access to this page. Please change your role on the home page if you want to use this feature.")