import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="Student Homework Organizer", page_icon="📚")

# Sidebar Navigation
page = st.sidebar.selectbox(
    "Navigation",
    ["Home", "Add Homework", "Homework List", "Study Timer", "Survey", "About"]
)

st.sidebar.title("📚 Homework Organizer")
st.sidebar.write("Manage your homework and stay organized.")

# HOME PAGE
if page == "Home":
    st.title("📚 Student Homework Organizer")

    st.header("Welcome!")
    st.write("This app helps students organize their homework and assignments.")

    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135755.png", width=200)

    st.subheader("Features")
    st.write("""
    - Add homework tasks
    - Track assignment deadlines
    - Organize school subjects
    - Study timer for productivity
    """)

    st.success("Tip: Use the sidebar to navigate through the app!")

# ADD HOMEWORK PAGE
elif page == "Add Homework":
    st.title("➕ Add Homework")

    subject = st.text_input("Subject Name")

    assignment = st.text_area("Homework Description")

    due_date = st.date_input("Due Date", date.today())

    difficulty = st.slider("Difficulty Level", 1, 10)

    priority = st.selectbox(
        "Priority Level",
        ["Low", "Medium", "High"]
    )

    reminder = st.checkbox("Set Study Reminder")

    study_hours = st.number_input("Estimated Study Hours", 1, 10)

    if st.button("Save Homework"):
        st.success("Homework saved successfully!")

    st.progress(0.5)

# HOMEWORK LIST PAGE
elif page == "Homework List":
    st.title("📋 Homework List")

    data = {
        "Subject": ["Math", "Science", "English"],
        "Homework": ["Algebra Worksheet", "Lab Report", "Essay Writing"],
        "Priority": ["High", "Medium", "Low"]
    }

    df = pd.DataFrame(data)

    st.dataframe(df)

    option = st.radio(
        "Filter Priority",
        ["All", "High", "Medium", "Low"]
    )

    st.write("Selected Filter:", option)

# STUDY TIMER PAGE
elif page == "Study Timer":

    st.title("⏳ Study Timer")

    minutes = st.select_slider(
        "Select Study Time",
        options=[15, 30, 45, 60]
    )

    if st.button("Start Timer"):
        st.info(f"Study session started for {minutes} minutes!")

    st.metric("Today's Study Goal", "2 Hours", "+30 mins")

# SURVEY PAGE
elif page == "Survey":

    st.title("📊 Student Study Survey")

    st.write("Help us understand your study habits.")

    name = st.text_input("Your Name")

    grade = st.selectbox(
        "Your Year Level",
        ["1st Year", "2nd Year", "3rd Year", "4th Year"]
    )

    study_time = st.slider(
        "How many hours do you study per day?",
        0,10
    )

    focus = st.radio(
        "When do you focus best?",
        ["Morning","Afternoon","Evening"]
    )

    feedback = st.text_area("Any study tips you want to share?")

    if st.button("Submit Survey"):
        st.success("Thank you for your feedback!")

# ABOUT PAGE
elif page == "About":

    st.title("ℹ About This App")

    st.subheader("App Purpose")
    st.write("""
    The Student Homework Organizer is designed to help students manage their assignments
    and stay organized with their academic responsibilities.
    """)

    st.subheader("Target Users")
    st.write("""
    The target users are students who want a simple system to track homework,
    deadlines, and study schedules.
    """)

    st.subheader("Inputs Collected")
    st.write("""
    The application collects:
    - Subject name
    - Homework description
    - Due date
    - Difficulty level
    - Priority level
    - Estimated study hours
    - Student survey responses
    """)

    st.subheader("Outputs")
    st.write("""
    The app displays:
    - Homework list tables
    - Study timer
    - Success notifications
    - Progress indicators
    """)
