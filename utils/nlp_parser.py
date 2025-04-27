import spacy
from utils.skills_master_list import SKILLS_MASTER_LIST

# Load English model
nlp = spacy.load("en_core_web_sm")

def extract_resume_sections(text):
    doc = nlp(text)

    detected_skills = set()
    education = []
    certifications = []
    experience_phrases = []

    skill_keywords = [skill.lower() for skill in SKILLS_MASTER_LIST]

    degree_keywords = ["bachelor", "master", "phd", "b.sc", "m.sc", "b.tech", "m.tech"]
    cert_keywords = ["certified", "certification", "aws", "gcp", "azure"]

    for sent in doc.sents:
        sent_lower = sent.text.lower()

        # Skill detection
        for keyword in skill_keywords:
            if keyword in sent_lower:
                detected_skills.add(keyword)

        # Education detection
        for degree in degree_keywords:
            if degree in sent_lower:
                education.append(sent.text.strip())

        # Certification detection
        for cert in cert_keywords:
            if cert in sent_lower and "certification" in sent_lower:
                certifications.append(sent.text.strip())

        # Experience phrase (impact verbs)
        if any(verb in sent_lower for verb in ["developed", "led", "managed", "optimized", "created", "improved", "designed"]):
            experience_phrases.append(sent.text.strip())

    return {
        "skills": sorted(list(detected_skills)),
        "education": list(set(education)),
        "certifications": list(set(certifications)),
        "experience": list(set(experience_phrases))
    }
