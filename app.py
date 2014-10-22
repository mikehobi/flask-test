from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask.ext.sqlalchemy import SQLAlchemy
from functools import wraps

app = Flask(__name__)

# config
import os
app.config.from_object(os.environ['APP_SETTINGS'])

# sqlalchemy object
db = SQLAlchemy(app)

from models import *


#  login dec
def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('You need to login first.')
			return redirect(url_for('login'))
	return wrap

@app.route('/')
@login_required
def index():
	posts = db.session.query(BlogPost).all()
	return render_template('index.html', posts=posts)

@app.route('/welcome')
def welcome():
	return render_template('welcome.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['user'] != 'admin' or request.form['password'] != 'admin':
			error = 'Oops. That username or password is incorrect.'
		else:
			session['logged_in'] = True
			flash('You just logged in!')
			return redirect(url_for('index'))
	return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
	session.pop('logged_in', None)
	flash('You just logged out')
	return redirect(url_for('welcome'))

if __name__ == '__main__':
	app.run()