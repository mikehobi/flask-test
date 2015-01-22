from flask.ext.script import Command

from project.models import User
from project import db

class GiveAllowance(Command):
	def run(self):
		for user in db.session.query(User):
			user.points_to_give = 20

		db.session.commit()