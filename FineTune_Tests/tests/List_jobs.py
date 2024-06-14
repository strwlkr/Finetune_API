import requests

def list_jobs():
    url = "https://studio.tune.app/tune.Studio/ListFinetuneJobs"

    payload = {"auth": {
            "organization": "37e5cceb-321d-411d-8781-5598bce6a366"
        }}

    headers = {
        "X-Tune-Key": "sk-tune-fd92y15aRzFKxMRXvCwULY34YizLRXyk0rK",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    jobs = response.json()
    # Check if 'jobs' is a list or a dictionary containing a list of jobs
    if isinstance(jobs, dict):
        jobs = jobs.get('jobs', [])

    # Filter and print all jobs with status
    print("List of jobs with ids/names and status:")
    for job in jobs:
        print(job.get('id')+"/("+job.get('name')+")"+": "+job.get('status'))

    active_ids=[]
    provisioning_ids = []
    terminated_ids = []
    killed_ids = []
    for job in jobs:
        if job.get('status')=="ACTIVE":
            active_ids.append(job.get('id'))
        elif job.get('status')=="PROVISIONING":
            provisioning_ids.append(job.get('id'))
        elif job.get('status')=="TERMINATED":
            terminated_ids.append(job.get('id'))
        elif job.get('status')=="KILLED":
            killed_ids.append(job.get('id'))

    return active_ids,provisioning_ids,terminated_ids,killed_ids