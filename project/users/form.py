from flask_wtf import Form, RecaptchaField
from wtforms import TextField, PasswordField, TextAreaField
from wtforms.validators import DataRequired

class LoginForm(Form):
	user = TextField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])

class PostForm(Form):
	title = TextField('Title', validators=[DataRequired()])
	description = TextAreaField('Content', validators=[DataRequired()])
	recaptcha = RecaptchaField()