import requests
import json

def create_job(job_name):
    url = "https://studio.tune.app/tune.Studio/CreateFinetuneJob"

    payload = {
        "auth": {
            "organization": "37e5cceb-321d-411d-8781-5598bce6a366"
        },
        "job": {
            "name": job_name,
            "baseModel": "llama2-07b-base",
            "datasets": [
                {
                    "path": "vicgalle/alpaca-gpt4",
                    "type": "huggingface",
                    "format": "instruct"
                }
            ],
            "resource": {
                "gpu": "nvidia-l4",
                "gpuCount": "1",
                "diskSize": "30Gi",
                "maxRetries": 1
            },
            "featureGates": {},
            "trainingConfig": {},
            "meta": {
                "metadata": {},
                "quantization": "QUANTIZATION_UNSPECIFIED",
                "IsModelMergeJob": True
            },
            "status": "ACTIVE"
        }
    }

    headers = {
        "X-Tune-Key": "sk-tune-fd92y15aRzFKxMRXvCwULY34YizLRXyk0rK",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    pretty_json = json.loads(response.text)
    print(json.dumps(pretty_json, indent=2))