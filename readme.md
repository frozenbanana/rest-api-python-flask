# REST API
This is a simple REST API. It is my solution to "Rest API task" from jobpal.

# How to use
1. Download zip
2. Unzip and move to directory
3. Create a virtual environment  `python3 -m venv .`
4. Install necessary packages `pip install -r reqirements.txt`
5. Initialize dummy database database `python init_db.py`
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
#### List all job offers, with pagination
Send a GET request to `localhost:5000/jobs/page/<PAGE_NUMBER>`  to get corresponding page. 

#### Retrieve locations and categories with most of jobs, ordered by # of job offers. 
Send a GET request to `localhost:5000/locations`