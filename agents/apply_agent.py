def prepare_application(job, cover_letter):
    return {
        "company": job.get("company", "Unknown"),
        "role": job["title"],
        "link": job["link"],
        "cover_letter": cover_letter,
        "status": "READY_TO_APPLY"
    }