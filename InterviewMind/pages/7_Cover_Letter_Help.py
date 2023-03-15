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
    job = st.selectbox("Select the job that you want a cover letter for",(st.session_state.job_title))
    if job is not None:
        for i in range(len(st.session_state.job_title)):
            if st.session_state.job_title[i] == job:
                uploaded_file = st.file_uploader('Choose your resume .pdf file', type="pdf")
                if uploaded_file is not None:
                    text = extract_text(uploaded_file)
                    text = ''.join(text)
                    response = openai.Completion.create(
                                    model="text-davinci-003",
                                    prompt= f"Write a cover letter for a job with the following title: {st.session_state.job_title[i]} and with the following job description: {st.session_state.job_descriptions[i]}. Answer using details from my resume: {text}.",
                                    temperature=0.5,
                                    max_tokens=500,
                                    top_p=1.0,
                                    frequency_penalty=0.0,
                                    presence_penalty=0.0
                                )
                    output = response['choices'][0]['text']
                    st.write("Here's a custom cover letter for you!")
                    st.info(output)
else:
    st.write("Sorry, recruiters don't have access to this page. Please change your role on the home page if you want to use this feature.")