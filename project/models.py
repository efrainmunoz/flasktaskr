# project/models.py


from views import db


class Task(db.Model):

	__tablename__ = "tasks"

	# table columns
	task_id = db.Column(
		db.Integer,
		primary_key=True
	)
	name = db.Column(
		db.String,
		nullable=False
	)
	due_date = db.Column(
		db.String,
		nullable=False
	)
	priority = db.Column(
		db.Integer,
		nullable=False
	)
	status = db.Column(
		db.Integer
	)

	# constructor
	def __init__(self, name, due_date, priority, status):
		self.name = name
		self.due_date = due_date
		self.priority = priority
		self.status = status

	# string representation
	def __repr__(self):
		return '<name {0}>'.format(self.name)