from utils.direct_skill_extractor import extract_direct_skills
from utils.jd_skill_inference import infer_skills_from_jd

LLM_SPECIALIZED_SKILLS = ["huggingface", "llama2", "llama3"]

def categorize_missing_skills(resume_skills, job_description):
    direct_skills = extract_direct_skills(job_description)
    inferred_skills = infer_skills_from_jd(job_description)

    resume_skills_lower = [r.lower() for r in resume_skills]
    jd_text_lower = job_description.lower()

    mandatory_missing = []
    good_to_have_missing = []
    optional_missing = []

    for skill in direct_skills:
        if skill.lower() not in resume_skills_lower:
            mandatory_missing.append(skill)

    for skill in inferred_skills:
        skill_lower = skill.lower()
        if skill_lower not in resume_skills_lower:
            if any(llm_skill in jd_text_lower for llm_skill in LLM_SPECIALIZED_SKILLS):
                if skill_lower in LLM_SPECIALIZED_SKILLS:
                    if skill_lower in direct_skills:
                        mandatory_missing.append(skill)
                    else:
                        good_to_have_missing.append(skill)
                else:
                    good_to_have_missing.append(skill)
            else:
                if skill_lower in LLM_SPECIALIZED_SKILLS:
                    optional_missing.append(skill)
                else:
                    good_to_have_missing.append(skill)

    return mandatory_missing, good_to_have_missing, optional_missing

def true_skill_based_score(resume_skills, mandatory_skills, good_to_have_skills):
    resume_skills_lower = [r.lower() for r in resume_skills]
    
    mandatory_covered = [skill for skill in mandatory_skills if skill.lower() in resume_skills_lower]
    good_to_have_covered = [skill for skill in good_to_have_skills if skill.lower() in resume_skills_lower]

    total_skills_expected = len(mandatory_skills) + len(good_to_have_skills)
    total_skills_covered = len(mandatory_covered) + len(good_to_have_covered)

    if total_skills_expected == 0:
        return 1.0  # If no skills expected, assume perfect match

    score = total_skills_covered / total_skills_expected
    return score
