import streamlit as st
from utils import pdf_parser, nlp_parser, smart_ats_score
from utils.direct_skill_extractor import extract_direct_skills

def run():
    st.title("📄 AI Career Coach - Smart Resume Analyzer")

    st.markdown("Upload your **Resume** and paste a **Job Description** to analyze your skill match for ATS optimization.")

    uploaded_resume = st.file_uploader("📂 Upload your Resume (PDF)", type=["pdf"])
    job_description = st.text_area(
        "📝 Paste the Job Description here",
        height=300,
        placeholder="Paste the full job description here...",
    )

    analyze_clicked = st.button("🔍 Analyze Resume and Job Description")

    if analyze_clicked:
        if not uploaded_resume:
            st.warning("⚠️ Please upload your resume before analyzing.")
            return

        if not job_description.strip():
            st.warning("⚠️ Please paste the job description before analyzing.")
            return

        with st.spinner("Analyzing your resume and job description..."):
            # Extract resume text and sections
            resume_text = pdf_parser.extract_text(uploaded_resume)
            parsed_sections = nlp_parser.extract_resume_sections(resume_text)

            # Extract JD direct skills
            direct_skills = extract_direct_skills(job_description)

            # Skill matching
            mandatory_skills, good_to_have_skills, optional_skills = smart_ats_score.categorize_missing_skills(
                parsed_sections["skills"], job_description
            )

            ats_skill_score = smart_ats_score.true_skill_based_score(
                parsed_sections["skills"], mandatory_skills, good_to_have_skills
            )

            # Resume Skills Lower
            resume_skills_lower = [r.lower() for r in parsed_sections["skills"]]

            matched_skills = [skill for skill in direct_skills if skill.lower() in resume_skills_lower]
            missing_skills = [skill for skill in direct_skills if skill.lower() not in resume_skills_lower]

            # Results
            st.success("✅ Analysis Complete!")

            st.subheader("📌 Extracted Resume Skills")
            with st.expander("View Skills from Resume"):
                st.write(parsed_sections["skills"])

            st.subheader("🚀 ATS Compatibility Score")
            st.metric(label="Skill Match Score (%)", value=f"{ats_skill_score * 100:.2f}")

            st.subheader("🔎 Skill Matching Details")
            st.write(f"✅ **Matched Skills:** {matched_skills}")
            st.write(f"❌ **Missing Skills:** {missing_skills}")

            st.subheader("🧩 Skill Gap Analysis")

            with st.expander("🚨 Mandatory Skills (Directly Required by JD)"):
                if mandatory_skills:
                    st.error(mandatory_skills)
                else:
                    st.success("No critical mandatory skills missing!")

            with st.expander("✅ Good to Have Skills (Inferred from JD Context)"):
                if good_to_have_skills:
                    st.info(good_to_have_skills)
                else:
                    st.success("Good coverage on context skills!")

            with st.expander("✨ Optional Bonus Skills (Nice to Show)"):
                if optional_skills:
                    st.info(optional_skills)
                else:
                    st.success("Optional bonuses fully covered!")

            st.subheader("🧠 AI Improvement Tips")
            tips = []
            if mandatory_skills:
                tips.append(f"⚡ Strongly recommend addressing {len(mandatory_skills)} mandatory skills like: {mandatory_skills[:3]}")
            if good_to_have_skills:
                tips.append(f"➕ Boost your profile with good-to-have skills like: {good_to_have_skills[:3]}")

            if not tips:
                tips.append("✅ Your resume aligns very well with the job description!")

            for tip in tips:
                st.write("- " + tip)
