from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from project import db
from project import bcrypt

# class BlogPost(db.Model):

# 	__tablename__ = "posts"
	
# 	id = db.Column(db.Integer, primary_key=True)
# 	title = db.Column(db.String, nullable=False)
# 	description = db.Column(db.String, nullable=False)
# 	author_id = db.Column(db.Integer, ForeignKey('users.id'))
	
# 	def __init__(self, title, description, author_id):
# 		self.title = title
# 		self.description = description
# 		self.author_id = author_id

# 	def __repr__(self):
# 		return '<{}>'.format(self.title)

class User(db.Model):

	__tablename__ = "users"

	id = db.Column(db.Integer, primary_key=True)
	created_at = db.Column(db.DateTime, default=datetime.now)
	name = db.Column(db.String, nullable=False)
	points_to_give = db.Column(db.Integer, default=20)
	points = relationship("Point", backref="user")
	img_url = db.Column(db.String)

	def __init__(self, name):
		self.name = name

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return unicode(self.id)

class Point(db.Model):

	__tablename__ = "points"

	id = db.Column(db.Integer, primary_key=True)
	created_at = db.Column(db.DateTime, default=datetime.now)
	user_id = db.Column(db.Integer, ForeignKey('users.id'))

	def __init__(self, user_id):
 		self.user_id = user_id