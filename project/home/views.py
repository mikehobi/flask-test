from datetime import date

from flask import flash, redirect, render_template, url_for, Blueprint

from project import db
from project.models import User, Point

home_blueprint = Blueprint(
	'home', __name__,
	template_folder='templates'
)

# ROUTES

@home_blueprint.route('/')
def index():
	users = db.session.query(User).all()

	for user in users:
		today = date.today()

		ptz_today = db.session.query(Point).filter(Point.created_at >= today).filter_by(user_id=user.id).count()
		user.points_today = ptz_today

		this_month = date(today.year, today.month, 1)
		ptz_month = db.session.query(Point).filter(Point.created_at >= this_month).filter_by(user_id=user.id).count()
		user.points_this_month = ptz_month

	ctx = {
        'users': users
    }

	return render_template('index.html', **ctx)

@home_blueprint.route('/user/<username>')
def profile(username):
	user = db.session.query(User).filter(User.name == username).first()
	if user != None:
		return render_template('profile.html', user=user)
	else:
		flash('That user does not exist.')
		return redirect(url_for('home.index'))

@home_blueprint.route('/halp')
def help():
	return render_template('help.html')