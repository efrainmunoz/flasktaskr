# project/forms.py


from flask_wtf import Form

from wtforms import StringField
from wtforms import DateField
from wtforms import IntegerField
from wtforms import SelectField

from wtforms.validators import DataRequired


class AddTaskForm(Form):
	task_id = IntegerField()

	name = StringField(
		'Task Name',
		validators=[DataRequired()]
	)

	due_date = DateField(
		'Date Due (mm/dd/yy)',
		validators=[DataRequired()],
		format='%m/%d/%y'
	)

	priority = SelectField(
		'Priority',
		validators=[DataRequired()],
		choices=[
			('1', '1'),
			('2', '2'),
			('3', '3'),
			('4', '4'),
			('5', '5'),
			('6', '6'),
			('7', '7'),
			('8', '8'),
			('9', '9'),
			('10', '10'),
		]
	)

	status = IntegerField('Status')