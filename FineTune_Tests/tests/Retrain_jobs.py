import requests
import json
import pytest

def retrain_job(job_id):
    url = "https://studio.tune.app/tune.Studio/RetrainFinetuneJob"

    payload = {
        "auth": {
            "organization": "37e5cceb-321d-411d-8781-5598bce6a366"
        },
        "job": {
            "id": job_id,
            #"name": "Big-Fireworks",
            "baseModel": "llama2-07b-base",
            "datasets": [
                {
                    "path": "HuggingFaceH4/instruction-dataset",
                    "type": "alpaca"
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
            "status": "TERMINATED"
        }
    }
    headers = {
        "X-Tune-Key": "sk-tune-fd92y15aRzFKxMRXvCwULY34YizLRXyk0rK",
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    pretty_json = json.loads(response.text)
    print(json.dumps(pretty_json, indent=2))





