# REST API
This is a simple REST API. It is my solution to "Rest API task" from jobpal. The API
handles request to a job offer database. Supported operations are:

- Insert a new job offer
- Update an existing job offer
- List all job offers
- List all job offers with pagination
- Retrieve locations and categories with most jobs
- Delete a job

# How to use
1. Download zip
2. Unzip and move to directory
3. Create a virtual environment and active it `python3 -m venv . && source bin/active`
4. Install necessary packages `pip install -r reqirements.txt`
5. Initialize dummy database `python init_db.py`
6. Start app `python app.py`

### Using API
It is recommended to use an API testing tool like Postman.

#### Insert a new job offer: 

Send a POST request to `localhost:5000/jobs` with the following json:
~~~
{
	"title": "test_title",
	"description": "test_description",
	"company": "test_company",
	"location": "test_location",
	"category": "test_category"
}
~~~
#### Update an existing job offer
Send a PUT request to `localhost:5000/jobs/<ID_NUMBER>` with the following json:
~~~
{
	"title": "updated_test",
	"description": "updated_description",
	"company": "updated_company",
	"location": "updated_location",
	"category": "updated_category"
}
~~~
#### List all job offers
Send a GET request to `localhost:5000/jobs`  to get all jobs. 

#### List all job offers, with pagination
Send a GET request to `localhost:5000/jobs/page/<PAGE_NUMBER>` to get corresponding page number. 

#### Retrieve locations and categories with most of jobs, ordered by # of job offers. 
Send a GET request to `localhost:5000/locations` to get locations.

#### Delete a job
Send a DELETE request to `localhost:5000/jobs/<ID_NUMBER>` to delete job with corresponding ID number.