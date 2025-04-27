def infer_skills_from_jd(jd_text):
    jd_text_lower = jd_text.lower()
    inferred_skills = set()

    # Cloud Providers
    if "aws" in jd_text_lower or "amazon web services" in jd_text_lower:
        inferred_skills.update(["aws", "ec2", "s3", "lambda", "terraform"])
    elif "gcp" in jd_text_lower or "google cloud" in jd_text_lower:
        inferred_skills.update(["gcp", "bigquery", "gke", "cloud functions"])
    elif "azure" in jd_text_lower or "microsoft azure" in jd_text_lower:
        inferred_skills.update(["azure", "cosmos db", "aks", "azure functions"])

    # Operating Systems
    if "linux" in jd_text_lower or "operating system" in jd_text_lower:
        inferred_skills.update(["linux", "bash", "shell scripting"])

    # Distributed Systems
    if "distributed system" in jd_text_lower or "microservices" in jd_text_lower:
        inferred_skills.update(["distributed systems", "microservices", "docker", "kubernetes", "rest api", "graphql"])

    # Databases
    if "database" in jd_text_lower or "data structures" in jd_text_lower:
        inferred_skills.update(["mysql", "postgresql", "mongodb", "redis", "elasticsearch"])

    # Security
    if "security" in jd_text_lower or "data protection" in jd_text_lower or "customer trust" in jd_text_lower:
        inferred_skills.update(["iam", "oauth2", "security compliance"])

    # Monitoring
    if "monitoring" in jd_text_lower or "on-call" in jd_text_lower or "availability" in jd_text_lower:
        inferred_skills.update(["prometheus", "grafana", "datadog", "pagerduty", "incident management", "sre best practices"])

    # Machine Learning (basic)
    if "machine learning" in jd_text_lower or "artificial intelligence" in jd_text_lower:
        inferred_skills.update(["tensorflow", "pytorch", "scikit-learn"])

    # Large Language Models (only if LLMs are specifically mentioned)
    if "large language models" in jd_text_lower or "llms" in jd_text_lower or "generative ai" in jd_text_lower:
        inferred_skills.update(["huggingface", "llama2", "llama3"])

    return list(inferred_skills)
