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

if st.session_state.role == "Recruiter":

    task = st.radio("Select how you want to add a job posting",("Upload Job Description","Create Job Description"))

    if task=="Upload Job Description":

        uploaded_file = st.file_uploader('Choose your .pdf file here containing the job description', type="pdf")
        if uploaded_file is not None:
            text = extract_text(uploaded_file)
            text = ''.join(text)
            st.info(text)
            st.session_state.pdf = 1
            openai.api_key = "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"
            
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt="Give me the title of the job with the following job description: " + text,
                temperature=0.5,
                max_tokens=15,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
            )
            output = response['choices'][0]['text']

            st.session_state.job_title.append(output)
            st.session_state.job_descriptions.append(text)

    else:
        job_title = st.text_input("Job Title")

        job_spec = st.text_input("Any Job Specifics")

        if st.button("Add Job Description"):

            response = openai.Completion.create(
                model="text-davinci-003",
                prompt= f"Give a detailed job description with sections including minimum qualifications and preferred qualities for the job posting with the following job title: {job_title} and with the following job specifics: {job_spec}. Answer keeping in mind the job title and job specifics, if given.",
                temperature=0.5,
                max_tokens=250,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
            )
            output = response['choices'][0]['text']
            st.write(output)

            st.session_state.job_title.append(job_title)
            st.session_state.job_descriptions.append(output)
else:
    st.write("Sorry, applicants don't have access to this page. Please change your role on the home page if you want to use this feature.")