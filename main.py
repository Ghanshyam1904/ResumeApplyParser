from agents.resume_agent import parse_resume
from agents.job_search_agent import search_jobs
from agents.filter_agent import filter_jobs
from agents.cover_letter_agent import generate_cover_letter
from agents.apply_agent import prepare_application
from agents.notification_agent import notify
from database.db import save_jobs
from utils.helpers import remove_duplicates

def run():
    print("📄 Parsing Resume...")
    resume = parse_resume("resume.pdf")

    print("🔍 Fetching Jobs...")
    jobs = search_jobs()

    jobs = remove_duplicates(jobs)

    print("🧠 Filtering Jobs...")
    filtered = filter_jobs(jobs, resume)

    applications = []
    report = "\n=== JOB REPORT ===\n\n"

    for job in filtered:
        print(f"Processing: {job['title']}")

        cover_letter = generate_cover_letter(job, resume)

        app = prepare_application(job, cover_letter)
        applications.append(app)

        report += f"""
Company: {app['company']}
Role: {app['role']}
Link: {app['link']}
Status: {app['status']}

Cover Letter:
{app['cover_letter']}
---------------------
"""

    save_jobs(applications)
    notify(report)

    print("✅ Done!")

if __name__ == "__main__":
    run()