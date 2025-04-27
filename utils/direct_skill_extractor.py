from utils.skills_master_list import SKILLS_MASTER_LIST
from rapidfuzz import fuzz
import re

def clean_text(text):
    # Remove numbers, special chars, and lowercase everything
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text.lower()

def extract_direct_skills(jd_text):
    jd_text_clean = clean_text(jd_text)
    jd_tokens = jd_text_clean.split()
    found_skills = []

    for skill in SKILLS_MASTER_LIST:
        skill_normalized = skill.lower()

        # First direct substring match
        if skill_normalized in jd_text_clean:
            found_skills.append(skill)
        else:
            # Fuzzy match token by token
            for token in jd_tokens:
                # Only match tokens of reasonable size (avoid matching 'r' or 'c')
                if len(token) >= 4 and fuzz.partial_ratio(skill_normalized, token) >= 90:
                    found_skills.append(skill)
                    break

    return list(set(found_skills))
