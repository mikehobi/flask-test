from project import db
from project.models import User
from flask import flash, redirect, render_template, url_for, Blueprint

home_blueprint = Blueprint(
	'home', __name__,
	template_folder='templates'
)

# ROUTES

@home_blueprint.route('/')
def index():
	return render_template('index.html')

@home_blueprint.route('/user/<username>')
def profile(username):
	user = db.session.query(User).filter(User.name == username).first()
	if user != None:
		return render_template('profile.html', user=user)
	else:
		flash('That user does not exist.')
		return redirect(url_for('home.index'))
