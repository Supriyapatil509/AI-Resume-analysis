def analyze_resume(text):
    skills = ["python", "java", "sql", "machine learning", "data science"]
    
    found_skills = []
    for skill in skills:
        if skill.lower() in text.lower():
            found_skills.append(skill)

    score = len(found_skills) * 20

    return {
        "skills": found_skills,
        "score": score
    }