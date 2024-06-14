import requests
import json
import pytest

def delete_job(job_id):
    url = "https://studio.tune.app/tune.Studio/DeleteFinetuneJob"


    payload = {
        "auth": {
            "organization": "37e5cceb-321d-411d-8781-5598bce6a366"
        },
        "id": job_id
    }

    headers = {
        "X-Tune-Key": "sk-tune-fd92y15aRzFKxMRXvCwULY34YizLRXyk0rK",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    pretty_json = json.loads(response.text)
    print(json.dumps(pretty_json, indent=2))
