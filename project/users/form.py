from flask_wtf import Form, RecaptchaField
from wtforms import TextField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from project.models import db, User

class LoginForm(Form):
	user = TextField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])

class SignupForm(Form):
	user = TextField('Username', validators=[DataRequired(), Length(min=3, max=25)])
	email = TextField('Email', validators=[DataRequired(), Email(message=None), Length(min=5, max=40)])
	password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=25)])
	confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match.')])

class PostForm(Form):
	title = TextField('Title', validators=[DataRequired()])
	description = TextAreaField('Content', validators=[DataRequired()])
	recaptcha = RecaptchaField()