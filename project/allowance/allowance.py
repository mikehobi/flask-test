from flask.ext.script import Command

from project.models import User
from project import db

class GiveAllowance(Command):
	def run(self):
		for user in db.session.query(User):
			user.points_to_give = 20

		db.session.commit()

class DeleteUsers(Command):
	def run(self):
		for user in db.session.query(User):
			db.session.delete(user)
			db.session.commit()

class MikeIsRich(Command):
	def run(self):
		user = db.session.query(User).filter(User.name == 'mike').first()
		user.points_to_give = 100
		db.session.commit()

# Slack users hard-coded. Need to figure out cross-reference w/ Slack roster
class CreateUsers(Command):
	def run(self):
		db.session.add(User("mike"))
		db.session.add(User("ana"))
		db.session.add(User("sean"))
		db.session.add(User("nick"))
		db.session.add(User("trev"))
		db.session.add(User("zak"))
		db.session.add(User("hakeem"))
		db.session.commit()