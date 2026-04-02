import requests
from bs4 import BeautifulSoup
import time

HEADERS = {"User-Agent": "Mozilla/5.0"}

def google_jobs_search(query):
    url = f"https://www.google.com/search?q={query}&num=20"
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []

    for g in soup.select("div.tF2Cxc"):
        try:
            title = g.select_one("h3").text
            link = g.select_one("a")["href"]
            desc = g.select_one(".VwiC3b")
            description = desc.text if desc else ""

            jobs.append({
                "title": title,
                "company": "Unknown",
                "link": link,
                "description": description
            })
        except:
            continue

    return jobs


def fetch_all_jobs():
    queries = [
        "site:linkedin.com/jobs machine learning fresher",
        "site:naukri.com machine learning fresher",
        "site:glassdoor.com machine learning fresher",
        "site:indeed.com machine learning fresher",
        "site:wellfound.com machine learning intern"
    ]

    all_jobs = []

    for q in queries:
        print(f"🔍 Searching: {q}")
        all_jobs += google_jobs_search(q)
        time.sleep(2)

    return all_jobs