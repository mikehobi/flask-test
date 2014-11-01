from flask_wtf import Form, RecaptchaField
from wtforms import TextField, PasswordField, TextAreaField
from wtforms.validators import DataRequired
from project.models import db, User

class LoginForm(Form):
	user = TextField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])

class SignupForm(Form):
	user = TextField('Username', validators=[DataRequired()])
	email = TextField('Email', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])

	# def __init__(self, *args, **kwargs):
	# 	Form.__init__(self, *args, **kwargs)

	# def validate(self):
	# 	if not Form.validate(self):
	# 	  return False
		 
	# 	user = User.query.filter_by(email = self.email.data.lower()).first()
	# 	if user:
	# 	  self.email.errors.append("That email is already taken")
	# 	  return False
	# 	else:
	# 	  return True

class PostForm(Form):
	title = TextField('Title', validators=[DataRequired()])
	description = TextAreaField('Content', validators=[DataRequired()])
	recaptcha = RecaptchaField()