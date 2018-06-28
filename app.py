# Make sure there is a crud.sqlite file before running this file
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False)
    description = db.Column(db.String(480), unique=False)
    company = db.Column(db.String(80), unique=False)
    location = db.Column(db.String(80), unique=False)
    category = db.Column(db.String(80), unique=False)

    def __init__(self, title, description, company, location, category):
        self.title = title
        self.description = description
        self.company = company
        self.location = location
        self.category = category


class JobSchema(ma.Schema):
    class Meta:
        # Field to expose
        fields = ('id', 'title', 'description', 'company', 'location', 'category')


job_schema = JobSchema()
jobs_schema = JobSchema(many=True)


# endpoint to show all jobs
@app.route("/jobs", methods=["GET"])
def get_jobs():
    all_jobs = Job.query.all()
    result = jobs_schema.dump(all_jobs)

    return jsonify(result.data)


# endpoint to get job by id
@app.route("/jobs/<id>", methods=["GET"])
def job_detail(id):
    job = Job.query.get(id)
    return job_schema.jsonify(job)


# endpoint to show jobs paginated
@app.route("/jobs/page/<int:page_num>", methods=["GET"])
def get_jobs_page(page_num):
    jobs = Job.query.paginate(per_page=5, page=page_num, error_out=True)
    return jobs_schema.jsonify(jobs.items)


# endpoint to show locations ordered by number of job offers
@app.route("/locations", methods=["GET"])
def get_location():
    locations = {}

    jobs = db.engine.execute("SELECT location, GROUP_CONCAT(DISTINCT category) AS categories,"
                             "COUNT(id) FROM JOB GROUP BY location ORDER BY COUNT(id) DESC")

    for row in jobs:
        categories = row['categories'].split(",")
        categories.sort()
        locations[row['location']] = categories

    return jsonify(locations)


# endpoint to create new job
@app.route("/jobs", methods=["POST"])
def create_job():
    title = request.json['title']
    description = request.json['description']
    company = request.json['company']
    location = request.json['location']
    category = request.json['category']

    new_job = Job(title, description, company, location, category)

    db.session.add(new_job)
    db.session.commit()

    return job_schema.jsonify(new_job)


# endpoint to update job
@app.route("/jobs/<id>", methods=["PUT"])
def job_update(id):
    job = Job.query.get(id)
    title = request.json['title']
    description = request.json['description']
    company = request.json['company']
    location = request.json['location']
    category = request.json['category']

    job.title = title
    job.description = description
    job.company = company
    job.location = location
    job.category = category

    db.session.commit()
    return job_schema.jsonify(job)


# endpoint to delete job
@app.route("/jobs/<id>", methods=["DELETE"])
def job_delete(id):
    job = Job.query.get(id)
    db.session.delete(job)
    db.session.commit()

    return job_schema.jsonify(job)


if __name__ == '__main__':
    app.run(debug=True)
