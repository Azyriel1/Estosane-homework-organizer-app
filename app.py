import streamlit as st
import pandas as pd
from datetime import date
import time

st.set_page_config(page_title="Student Homework Organizer", page_icon="📚")

# ------------------------
# Initialize session state
# ------------------------
if "homework_list" not in st.session_state:
    st.session_state.homework_list = []

if "edit_index" not in st.session_state:
    st.session_state.edit_index = None  # Track which homework is being edited

# ------------------------
# Sidebar Navigation
# ------------------------
page = st.sidebar.selectbox(
    "Navigation",
    ["Home", "Add/Edit Homework", "Homework List", "Study Timer", "Survey", "About"]
)

st.sidebar.title("📚 Homework Organizer")
st.sidebar.write("Manage your homework and stay organized.")

# ------------------------
# HOME PAGE
# ------------------------
if page == "Home":
    st.title("📚 Student Homework Organizer")
    st.header("Welcome!")
    st.write("This app helps students organize their homework and assignments.")
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135755.png", width=200)
    st.subheader("Features")
    st.write("""
    - Add, edit, and delete homework tasks
    - Track assignment deadlines
    - Organize school subjects
    - Study timer for productivity
    """)
    st.success("Tip: Use the sidebar to navigate through the app!")

# ------------------------
# ADD/EDIT HOMEWORK PAGE
# ------------------------
elif page == "Add/Edit Homework":
    st.title("➕ Add or Edit Homework")

    if st.session_state.edit_index is not None:
        hw = st.session_state.homework_list[st.session_state.edit_index]
        subject = st.text_input("Subject Name", value=hw["Subject"])
        assignment = st.text_area("Homework Description", value=hw["Description"])
        due_date = st.date_input("Due Date", value=pd.to_datetime(hw["Due Date"]))
        difficulty = st.slider("Difficulty Level", 1, 10, value=hw["Difficulty"])
        priority = st.selectbox(
            "Priority Level", ["Low", "Medium", "High"], index=["Low", "Medium", "High"].index(hw["Priority"])
        )
        study_hours = st.number_input("Estimated Study Hours", 1, 10, value=hw["Study Hours"])
    else:
        subject = st.text_input("Subject Name")
        assignment = st.text_area("Homework Description")
        due_date = st.date_input("Due Date", date.today())
        difficulty = st.slider("Difficulty Level", 1, 10)
        priority = st.selectbox("Priority Level", ["Low", "Medium", "High"])
        study_hours = st.number_input("Estimated Study Hours", 1, 10)

    if st.button("Save Homework"):
        if subject.strip() == "" or assignment.strip() == "":
            st.warning("Please enter both Subject and Homework Description.")
        else:
            new_homework = {
                "Subject": subject,
                "Description": assignment,
                "Due Date": due_date.strftime("%Y-%m-%d"),
                "Difficulty": difficulty,
                "Priority": priority,
                "Study Hours": study_hours
            }

            if st.session_state.edit_index is not None:
                st.session_state.homework_list[st.session_state.edit_index] = new_homework
                st.session_state.edit_index = None
                st.success("✅ Homework updated successfully!")
            else:
                st.session_state.homework_list.append(new_homework)
                st.success("✅ Homework added successfully!")

# ------------------------
# HOMEWORK LIST PAGE
# ------------------------
elif page == "Homework List":
    st.title("📋 Homework List")

    if st.session_state.homework_list:
        df = pd.DataFrame(st.session_state.homework_list)
        st.dataframe(df)

        # Choose homework to edit
        edit_choice = st.selectbox(
            "Select homework to edit", 
            options=[f"{i}: {hw['Subject']} - {hw['Description']}" for i, hw in enumerate(st.session_state.homework_list)],
            key="edit_select"
        )

        if st.button("Edit Selected Homework"):
            st.session_state.edit_index = int(edit_choice.split(":")[0])
            st.success("Now go to Add/Edit Homework page to update this entry.")

        # Choose homework to delete
        delete_choice = st.selectbox(
            "Select homework to delete",
            options=[f"{i}: {hw['Subject']} - {hw['Description']}" for i, hw in enumerate(st.session_state.homework_list)],
            key="delete_select"
        )

        if st.button("Delete Selected Homework"):
            index_to_delete = int(delete_choice.split(":")[0])
            st.session_state.homework_list.pop(index_to_delete)
            st.success("✅ Homework deleted successfully!")
            st.experimental_rerun()
    else:
        st.info("No homework added yet. Go to 'Add/Edit Homework' to add new tasks.")

# ------------------------
# STUDY TIMER PAGE
# ------------------------
elif page == "Study Timer":
    st.title("⏳ Study Timer")
    minutes = st.select_slider("Select Study Time (minutes)", options=[15, 30, 45, 60])
    start_button = st.button("Start Timer")
    timer_placeholder = st.empty()

    if start_button:
        total_seconds = minutes * 60
        for i in range(total_seconds, -1, -1):
            mins, secs = divmod(i, 60)
            timer_placeholder.markdown(f"**Time Left: {mins:02d}:{secs:02d}**")
            time.sleep(1)
        st.success("⏰ Time's up! Great job studying!")

# ------------------------
# SURVEY PAGE
# ------------------------
elif page == "Survey":
    st.title("📊 Student Study Survey")
    st.write("Help us understand your study habits.")

    name = st.text_input("Your Name")
    grade = st.selectbox("Your Year Level", ["1st Year", "2nd Year", "3rd Year", "4th Year"])
    study_time = st.slider("How many hours do you study per day?", 0, 10)
    focus = st.radio("When do you focus best?", ["Morning", "Afternoon", "Evening"])
    feedback = st.text_area("Any study tips you want to share?")

    if st.button("Submit Survey"):
        st.success("Thank you for your feedback!")

# ------------------------
# ABOUT PAGE
# ------------------------
elif page == "About":
    st.title("ℹ About This App")

    st.write("""
    The Student Homework Organizer is a simple application developed using Streamlit that helps students manage 
    their homework and academic responsibilities in an organized way. 
    
    The app is designed for students who want an easy tool to track their assignments, deadlines, and study tasks. 
    
    Users can input information such as the subject name, homework description, due date, priority level, difficulty level, and estimated study hours. 
    
    The application then displays helpful outputs including organized homework lists, study timer notifications, 
    tables, and status messages to guide students in managing their schoolwork efficiently.
    """)
