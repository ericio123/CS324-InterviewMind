import streamlit as st
import openai

if st.session_state.role == "Recruiter":
    job = st.selectbox("Select which job to show applications for",(st.session_state.job_title))
    if job is not None:
        applicants = []
        for i in range(len(st.session_state.name)):
            if st.session_state.resume_job[i] == job:
                applicants.append(st.session_state.name[i])
        applicant = st.selectbox("Select which applicant to show a profile for",(applicants))
        if applicant is not None:
            for i in range(len(st.session_state.name)):
                if st.session_state.name[i] == applicant:
                    st.write("Name")
                    st.info(st.session_state.name[i])
                    st.write("Education")
                    st.info(st.session_state.education[i])
                    st.write("Skills")
                    st.info(st.session_state.skills[i])
                    st.write("Contact Information")
                    st.info(st.session_state.contact[i])
                    st.markdown("""***""")
                    text = ""
                    for key in st.session_state.bh_interviews.keys():
                        if key.strip() == st.session_state.name[i].strip():
                            for i in range(len(st.session_state.bh_interviews[key])):
                                st.write("Behavioral Question " + str(i+1))
                                question = st.session_state.bh_interviews[key][i]["Question"]
                                st.info(question)
                                st.write("Behavioral Answer " + str(i+1))
                                answer = st.session_state.bh_interviews[key][i]["Question"]
                                st.info(answer)
                                text += f"Question: {question}. Answer: {answer}. "
                    response = openai.Completion.create(
                        model="text-davinci-003",
                        prompt=f"Give a summary of the personality of this job applicant based on their answers to the following behavioral interview questions: {text}",
                        temperature=0.5,
                        max_tokens=150,
                        top_p=1.0,
                        frequency_penalty=0.0,
                        presence_penalty=0.0
                    )
                    output = response['choices'][0]['text']
                    st.write("Behavioral summary")
                    st.info(output)
                    st.markdown("""***""")
                    for key in st.session_state.tc_interviews.keys():
                        if key.strip() == st.session_state.name[i].strip():
                            for i in range(len(st.session_state.tc_interviews[key])):
                                st.write("Technical Question " + str(i+1))
                                question = st.session_state.tc_interviews[key][i]["Question"]
                                st.info(question)
                                st.write("Technical Answer " + str(i+1))
                                answer = st.session_state.tc_interviews[key][i]["Question"]
                                st.info(answer)
else:
    st.write("Sorry, applicants don't have access to this page. Please change your role on the home page if you want to use this feature.")