# Creates a dummy datebase -> crud.splite
# This should be run first if there is no crud.sqlite file

from app import db, Job
import random


db.create_all()
nr_of_items = 200
for i in range(0, nr_of_items):
    title = 'title' + str(i)
    description = 'description' + str(i)
    company = 'company' + str(random.randint(1, 5))
    location = random.choice(['location1', 'location2', 'location3'])

    if location == 'location1':
        category = random.choice(['category1', 'category2', 'category3', 'category4', 'category5'])
    elif location == 'location2':
        category = random.choice(['category3', 'category4', 'category5'])
    else:
        category = random.choice(['category2', 'category5'])

    job = Job(title, description, company, location, category)
    db.session.add(job)

db.session.commit()
print("Created " + str(nr_of_items) + " entries.")

