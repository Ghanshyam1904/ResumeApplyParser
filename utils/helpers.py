def remove_duplicates(jobs):
    seen = set()
    unique = []

    for job in jobs:
        if job["link"] not in seen:
            seen.add(job["link"])
            unique.append(job)

    return unique