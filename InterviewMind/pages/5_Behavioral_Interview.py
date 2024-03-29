import streamlit as st
import openai
# st.session_state.bh_interviews={}
openai.api_key = "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"

def generate_questions(title, name, desc=None):
    for i in range(len(st.session_state.name)):
        if st.session_state.name[i] == name:
            prompt = f"Generate 5 behavioral interview questions for a {title} position. Use the work history of the candidate to help generate the question. Work history: {st.session_state.work[i]}. Only write questions in output separated by a newline."
            completions = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=100,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
            )
            message = completions.choices[0].text.strip()
    return message.split("\n")

def app():
    # Set up Streamlit app
    st.title("Behavioral Interview Test")
    role = st.selectbox("Select role:", st.session_state.job_title)
    st.write(f"You selected: {role}")
    submitted=None

    name = st.text_input("Write your name below and press Enter to start the test.")

    if name == "":
    # Do nothing until Enter is pressed
        pass
    elif name not in st.session_state.name:
        st.info("You don't have access to the interview for the selected role.")
    else:

        # if st.button("Start Test"):
        with st.form("test"):
            # Generate interview questions using OpenAI API
            # print(type(st.session_state.bh_interviews))
            questions = generate_questions(role, name)
            st.write("Please answer the following questions:")
            question_index = 0
            answers = {}
            
            # Loop through interview questions
            for question in questions:
                st.write(f"Q{question}")
                answer = st.text_area("Your Answer:",key=-question_index)
                # if answer:
                answers[question_index] = {"Question": question, "Answer": answer}
                question_index += 1
            
            submitted = st.form_submit_button("Submit Test")

            if submitted:
                st.session_state.bh_interviews[name]=answers
                st.write("Answers submitted successfully.")
                st.write(answers)

    # if submitted:
    # # Show "Submit Test" button after all questions have been answered
    #     if question_index == len(questions):
    #         if st.button("Submit Test"):
    #             # Save answers to database or file for later use
    #             st.session_state.bh_interviews.append(answers)
    #             st.write("Answers submitted successfully.")
    #             st.write(answers)
                    

# Run Streamlit app
if __name__ == "__main__":
    if st.session_state.role == "Applicant":
        app()
    else:
        st.write("Sorry, recruiters don't have access to this page. Please change your role on the home page if you want to use this feature.")