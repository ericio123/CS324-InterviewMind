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
                            for j in range(len(st.session_state.bh_interviews[key])):
                                st.write("Behavioral Question " + str(j+1))
                                question = st.session_state.bh_interviews[key][j]["Question"]
                                st.info(question)
                                st.write("Behavioral Answer " + str(j+1))
                                answer = st.session_state.bh_interviews[key][j]["Answer"]
                                st.info(answer)
                                text += f"Question: {question}. Answer: {answer}. "
                            response = openai.Completion.create(
                                model="text-davinci-003",
                                prompt=f"Given the following five behavioral questions and their answers from a candidate, please provide an overall behavioral profile of the candidate. Your response should be based solely on the information provided in the candidate's answers and should not include any made-up information or assumptions: {text}",
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
                            for j in range(len(st.session_state.tc_interviews[key])):
                                st.write("Technical Question " + str(j+1))
                                question = st.session_state.tc_interviews[key][j]["Question"]
                                st.info(question)
                                st.write("Technical Answer " + str(j+1))
                                answer = st.session_state.tc_interviews[key][j]["Answer"]
                                st.info(answer)
                            response = openai.Completion.create(
                                model="text-davinci-003",
                                prompt=f"Given the following short technical questions and their answers from a candidate, please evaluate the candidate's technical capabilities and provide a rating out of 5 based on the accuracy of their answers for the respective question asked. What can you infer about the candidate's technical capabilities based on their overall rating and their strengths and areas for improvement (in short)? Your response should be based solely on the information provided in the candidate's answers and should not include any made-up information or assumptions.: {st.session_state.tc_interviews[applicant.strip()]}",
                                temperature=0.5,
                                max_tokens=150,
                                top_p=1.0,
                                frequency_penalty=0.0,
                                presence_penalty=0.0
                            )
                            output = response['choices'][0]['text']
                            st.write("Technical summary")
                            st.info(output)
                            st.markdown("""***""")


else:
    st.write("Sorry, applicants don't have access to this page. Please change your role on the home page if you want to use this feature.")