# --- University Management System with Full Features and Attractive UI ---

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from streamlit_lottie import st_lottie
import requests

# --- Utility to load Lottie animations ---
def load_lottie(url):
    r = requests.get(url)
    return r.json() if r.status_code == 200 else None

lottie_login = load_lottie("https://assets3.lottiefiles.com/packages/lf20_jcikwtux.json")

# --- Dummy credentials ---
USERS = {
    "admin": {"password": "admin123", "role": "Admin"},
    "faculty1": {"password": "fac123", "role": "Faculty"},
    "stud001": {"password": "stud123", "role": "Student"},
    "Abdul": {"password": "12345", "role": "Student"}
}

# Session Initialization
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# --- Login Page ---
if not st.session_state.logged_in:
    st.set_page_config(page_title="University Portal", layout="centered")
    st_lottie(lottie_login, height=200)
    st.title("\U0001F512 University Management System")
    user = st.text_input("\U0001F464 Username")
    pwd = st.text_input("\U0001F511 Password", type="password")
    if st.button("\u27A1\uFE0F Login"):
        user_info = USERS.get(user)
        if user_info and user_info["password"] == pwd:
            st.session_state.user = user
            st.session_state.role = user_info["role"]
            st.session_state.logged_in = True
            st.success(f"Welcome, {user_info['role']} {user.capitalize()}!")
        else:
            st.error("Invalid credentials. Try again.")
    st.stop()

# --- After Login ---
role = st.session_state.role
st.set_page_config(page_title=f"{role} Dashboard", layout="wide")
st.sidebar.title(f"\U0001F464 {role} Menu")

# --- Dummy Data ---
students_df = pd.DataFrame({"ID": ["stud001", "stud002"], "Name": ["Ali", "Sara"], "GPA": [3.5, 3.8]})
faculty_df = pd.DataFrame({"ID": ["faculty1", "faculty2"], "Name": ["Dr. Khan", "Ms. Ayesha"], "Dept": ["CS", "IT"]})
attendance_df = pd.DataFrame({"Date": pd.date_range(end=datetime.today(), periods=7).strftime('%Y-%m-%d'),
                              "Attendance": [90, 88, 92, 85, 87, 91, 89]}).set_index("Date")
finance_df = pd.DataFrame({"Month": ["Jan", "Feb", "Mar"], "Fees": [100000, 120000, 110000]}).set_index("Month")
courses_df = pd.DataFrame({"Course ID": ["CS101", "IT202"], "Title": ["Intro to CS", "Web Dev"], "Credits": [3, 4]})
assignments_df = pd.DataFrame({"Course": ["CS101", "IT202"], "Assignment": ["HW1", "Project"], "Due": ["2025-06-25", "2025-06-30"]})
notices = ["Mid Term Exams from July 1", "Submit Assignments by June 30"]

# --- Sidebar Navigation ---
menus = {
    "Admin": ["Dashboard", "Manage Students", "Manage Faculty", "Courses", "Attendance", "Finance", "Notices", "Logout"],
    "Faculty": ["Dashboard", "My Classes", "Assignments", "Attendance", "Exams", "Notices", "Logout"],
    "Student": ["Dashboard", "My Profile", "Courses", "Assignments", "My Attendance", "My Results", "Notices", "Logout"]
}
choice = st.sidebar.selectbox("\U0001F4DA Select Module", menus[role])

# --- Modules ---

if choice == "Dashboard":
    st.title(f"\U0001F4CA {role} Dashboard")
    cols = st.columns(3)
    cols[0].metric("\U0001F393 Students", len(students_df))
    cols[1].metric("\U0001F3EB Faculty", len(faculty_df))
    cols[2].metric("\U0001F4B0 Fees Collected", finance_df["Fees"].sum())
    st.subheader("Attendance Trend")
    st.line_chart(attendance_df)
    st.subheader("Fee Collection")
    st.bar_chart(finance_df)

elif choice == "Manage Students" and role == "Admin":
    st.title("\U0001F4CB Manage Students")
    st.dataframe(students_df)

elif choice == "Manage Faculty" and role == "Admin":
    st.title("\U0001F3EB Manage Faculty")
    st.dataframe(faculty_df)

elif choice == "Courses":
    st.title("\U0001F4D6 Course Management")
    st.dataframe(courses_df)

elif choice == "My Profile" and role == "Student":
    st.title("\U0001F464 My Profile")
    me = students_df[students_df["ID"] == st.session_state.user]
    st.table(me)

elif choice == "Assignments":
    st.title("\U0001F4DD Assignments")
    st.table(assignments_df)
    if role == "Faculty":
        st.file_uploader("Upload New Assignment", type=["pdf", "docx"])

elif choice == "My Classes" and role == "Faculty":
    st.title("\U0001F4DA My Classes")
    st.write("\u26A0 Under development")

elif choice in ["Attendance", "My Attendance"]:
    st.title("\U0001F4C5 Attendance Records")
    st.line_chart(attendance_df)

elif choice == "Finance" and role == "Admin":
    st.title("\U0001F4B5 Finance")
    st.bar_chart(finance_df)

elif choice in ["Exams", "My Results"]:
    st.title("\U0001F4DA Exam Results")
    res = pd.DataFrame({"Subject": ["Math", "Physics"], "Grade": ["A", "B+"]})
    st.table(res)

elif choice == "Notices":
    st.title("\U0001F4E2 Notices & Announcements")
    for note in notices:
        st.info(note)
    if role in ["Admin", "Faculty"]:
        new_notice = st.text_area("Add New Notice")
        if st.button("Post"):
            notices.append(new_notice)
            st.success("Notice added!")

elif choice == "Logout":
    st.session_state.clear()
    st.experimental_rerun()

else:
    st.warning("\u26A0 Feature coming soon.")

# Footer
st.markdown("---")
st.markdown("\u2728 *University Management System built with Streamlit*")
