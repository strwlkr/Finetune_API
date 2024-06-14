# Finetune_API
Perform FineTune API operations
This project contains API tests for managing Finetune jobs, including creating, getting, listing, retraining, terminating, and deleting jobs. The tests are organized into separate modules, each focusing on a specific functionality.

1. Project Structure
  Base_Test_Page.py: Contains methods for creating, getting, listing, retraining, terminating, and deleting Finetune jobs. It serves as the central module where all methods are defined and invoked.
  Create_job.py: Contains methods for creating new Finetune jobs.
  Delete_job.py: Contains methods for deleting existing Finetune jobs.
  Retrain_jobs.py: Contains methods for retraining existing Finetune jobs.
  Terminate_job.py: Contains methods for terminating ongoing Finetune jobs.
  List_jobs.py: Contains methods for listing all Finetune jobs.
  Get_jobs.py: Contains methods for getting details of a specific Finetune job.

2. Pre requisites
  Python 3.10.1 installed on your system.
  
  PyCharm IDE installed.
  
  requests library for handling API requests. You can install it using pip:
  pip install requests

3. Setting Up the Project: 
  Clone the repository:
  git clone https://github.com/strwlkr/Finetune_API
  cd api-tests

  a.Open the project in PyCharm:
  Open PyCharm.
  Click on File > Open and select the project directory.

4. Running the Tests
  1. Base_Test_Page
  a. This page contains all the main methods for interacting with the Finetune jobs API.
  b. The jobs_to_be_created list can be filled up with unique job names to be created for test
  c. The job_idslist is fetched with existing job ids which can be used to fetch job details
  d. The list_job() function is automatically invoked everytime the Base_Test_Page is run and the job ids are updated in 4 separate lists(active,provisioned,terminated and killed) based on the latest status
  e. The terminate_job(id),retrain_job(id),delete_job(id) functions can be run from the list of terminated and killed ids.


