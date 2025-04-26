import streamlit as st
from config import LOCAL_MODE
from modules import resume_analyzer, job_matcher, interview_coach, skill_planner

st.set_page_config(page_title="AI Career Coach", layout="wide")

st.title("🚀 AI Career Coach Agent")

# Sidebar Navigation
page = st.sidebar.selectbox(
    "Choose a module",
    ("Resume Analyzer", "Job Matcher", "Interview Coach", "Skill Planner")
)

if page == "Resume Analyzer":
    resume_analyzer.run()
elif page == "Job Matcher":
    job_matcher.run()
elif page == "Interview Coach":
    interview_coach.run()
elif page == "Skill Planner":
    skill_planner.run()
