import json
import os

DB_FILE = "applied_jobs.json"

def save_jobs(jobs):
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, "w") as f:
            json.dump([], f)

    with open(DB_FILE, "r") as f:
        data = json.load(f)

    data.extend(jobs)

    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=2)