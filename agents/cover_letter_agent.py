from tools.ollama_client import ask_ollama

def generate_cover_letter(job, resume_text):
    prompt = f"""
    Write a short professional cover letter.

    Job: {job['title']}
    Description: {job['description']}

    Resume:
    {resume_text}
    """

    return ask_ollama(prompt)