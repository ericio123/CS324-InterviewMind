# import streamlit as st

# # Define the pages for the "Student" profile
# def student_home():
#     st.write("Welcome to the Student Home Page!")

# def student_page1():
#     st.write("This is Student Page 1")

# def student_page2():
#     st.write("This is Student Page 2")

# student_pages = {
#     "Student Home": student_home,
#     "Page 1": student_page1,
#     "Page 2": student_page2
# }

# # Define the pages for the "Recruiter" profile
# def recruiter_home():
#     st.write("Welcome to the Recruiter Home Page!")

# def recruiter_page1():
#     st.write("This is Recruiter Page 1")

# def recruiter_page2():
#     st.write("This is Recruiter Page 2")

# recruiter_pages = {
#     "Recruiter Home": recruiter_home,
#     "Page 1": recruiter_page1,
#     "Page 2": recruiter_page2
# }

# # Define the sidebar
# st.sidebar.title("Profile Selector")
# profile = st.sidebar.radio("", ("Student", "Recruiter"))

# # Display the appropriate set of pages based on the user's selection
# if profile == "Student":
#     st.sidebar.write("Student Pages")
#     page = st.sidebar.radio("", list(student_pages.keys()))
#     student_pages[page]()
# else:
#     st.sidebar.write("Recruiter Pages")
#     page = st.sidebar.radio("", list(recruiter_pages.keys()))
#     recruiter_pages[page]()


import streamlit as st

# Define pages for student and recruiter profiles
def student_profile():
    st.write("Welcome to the student section!")
    st.write("Here are some pages available to students:")

    page_options = ["Page 1", "Page 2", "Page 3"]
    selected_page = st.sidebar.selectbox("Select a page", page_options)
    if selected_page == "Page 1":
        st.write("This is page 1 for students")
    elif selected_page == "Page 2":
        st.write("This is page 2 for students")
    elif selected_page == "Page 3":
        st.write("This is page 3 for students")

def recruiter_profile():
    st.write("Welcome to the recruiter section!")
    st.write("Here are some pages available to recruiters:")

    page_options = ["Page 4", "Page 5", "Page 6"]
    selected_page = st.sidebar.selectbox("Select a page", page_options)
    if selected_page == "Page 4":
        st.write("This is page 1 for recruiters")
    elif selected_page == "Page 5":
        st.write("This is page 2 for recruiters")
    elif selected_page == "Page 6":
        st.write("This is page 3 for recruiters")

# Define the main app
def main():
    st.sidebar.title("Select a profile:")
    profile = st.sidebar.radio("", ("Student", "Recruiter"))
    if profile == "Student":
        student_profile()
    elif profile == "Recruiter":
        recruiter_profile()

# Run the app
if __name__ == "__main__":
    main()
