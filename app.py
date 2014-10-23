from flask import Flask, flash, redirect, session, url_for, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from functools import wraps
import os

# CONFIG

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from models import *
from project.users.views import users_blueprint

# REGISTER BLUEPRINTS
app.register_blueprint(users_blueprint)

# HELPERS

def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('You need to login first.')
			return redirect(url_for('users.login'))
	return wrap

# ROUTES

@app.route('/')
@login_required
def index():
	posts = db.session.query(BlogPost).all()
	return render_template('index.html', posts=posts)

@app.route('/welcome')
def welcome():
	return render_template('welcome.html')

if __name__ == '__main__':
	app.run()
