from sklearn.metrics.pairwise import cosine_similarity
import re

def calculate_similarity(embedding1, embedding2):
    return cosine_similarity([embedding1], [embedding2])[0][0]

def find_missing_keywords(resume_text, job_description):
    resume_words = set(re.findall(r'\b\w+\b', resume_text.lower()))
    jd_words = set(re.findall(r'\b\w+\b', job_description.lower()))
    missing = jd_words - resume_words
    return list(missing)[:20]  # show top 20 missing keywords
