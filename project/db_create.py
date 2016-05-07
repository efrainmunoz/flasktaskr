# project/db_create.py


from views import db
from models import Task
from datetime import date


# create the database and the db table
db.create_all()

#insert data
db.session.add(
	Task(
		'Finish this tutorial',
		'05/08/2016',
		10,
		1
	)
)

db.session.add(
	Task(
		'Finish Real Python',
		'05/08/2016',
		10,
		1
	)
)

# commit the changes
db.session.commit()