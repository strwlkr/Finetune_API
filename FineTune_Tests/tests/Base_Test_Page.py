import pytest
from Create_job import create_job
from List_jobs import list_jobs
from Get_jobs import get_job
from Terminate_job import terminate_job
from Retrain_jobs import retrain_job
from Delete_job import delete_job

## Create a job
# Iterate through the list of jobs_to_be_created filled with unique job names and call the create_job function for each
jobs_to_be_created = ["Test-11"]
for job_name in jobs_to_be_created:
    create_job(job_name)

## Get Job
#To get Job details with Job ID
job_ids= ["hryagmmh"]
for job_id in job_ids:
    get_job(job_id)

## List Jobs
# To fetch the list of active,provisioned,terminated and killed jobs by their IDs and segregating them
# active,provisioning,terminated,killed are list of active,provisioned,terminated and killed jobs which are then converted into string type
active,provisioning,terminated,killed = list_jobs()
active_ids = str(active)
provisioning_ids = str(provisioning)
terminated_ids = str(terminated)
killed_ids = str(killed)
print("Active Ids: "+active_ids)
print("Provisioning Ids: "+provisioning_ids)
print("Terminated Ids: "+terminated_ids)
print("Killed Ids: "+killed_ids)

## Terminate Jobs
# To terminate jobs which are active and provisioned

#Uncomment the below lines only when needed
#for id in active_ids:
#    terminate_job(id)

## Retrain Jobs
# Retrain jobs from list of terminated jobs

#Uncomment the below lines only when needed
#for id in terminated_ids:
#    retrain_job(id)

## Delete Jobs
# Delete jobs from list of terminated jobs

#Uncomment the below lines only when needed
#for id in terminated_ids:
#    delete_job(id)

