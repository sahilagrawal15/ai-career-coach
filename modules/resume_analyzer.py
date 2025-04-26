import streamlit as st
from utils import pdf_parser, embeddings, ats_score

def run():
    st.header("📄 Resume Analyzer & ATS Optimizer")

    uploaded_resume = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])
    job_description = st.text_area("Paste Job Description Here")

    if uploaded_resume and job_description:
        resume_text = pdf_parser.extract_text(uploaded_resume)

        st.subheader("Extracted Resume Text")
        st.write(resume_text)

        resume_embedding = embeddings.generate_embedding(resume_text)
        job_embedding = embeddings.generate_embedding(job_description)

        score = ats_score.calculate_similarity(resume_embedding, job_embedding)

        st.subheader("ATS Compatibility Score")
        st.metric(label="Score (%)", value=f"{score*100:.2f}")

        missing_keywords = ats_score.find_missing_keywords(resume_text, job_description)
        st.subheader("Missing Keywords Suggestions")
        st.write(missing_keywords)
