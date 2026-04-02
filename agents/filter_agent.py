from tools.ollama_client import ask_ollama

def filter_jobs(jobs, resume_text):
    filtered = []

    for job in jobs:
        prompt = f"""
        Resume:
        {resume_text}

        Job Title: {job['title']}
        Description: {job['description']}

        Is this suitable for a fresher ML engineer?

        Return format:
        YES/NO
        Reason
        Score (0-100)
        """

        response = ask_ollama(prompt)

        if "YES" in response.upper():
            job["analysis"] = response
            filtered.append(job)

    return filtered