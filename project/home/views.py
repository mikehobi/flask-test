from project import app, db
from project.models import BlogPost
from flask import flash, redirect, session, url_for, render_template, Blueprint
from functools import wraps

home_blueprint = Blueprint(
	'home', __name__,
	template_folder='templates'
)

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

@home_blueprint.route('/')
@login_required
def index():
	posts = db.session.query(BlogPost).all()
	return render_template('index.html', posts=posts)

@home_blueprint.route('/welcome')
def welcome():
	return render_template('welcome.html')
