from datetime import date

from flask import flash, redirect, render_template, url_for, Blueprint

from project import db, slack
from project.models import User, Point

from .form import GivePoints

home_blueprint = Blueprint(
	'home', __name__,
	template_folder='templates'
)

# ROUTES

@home_blueprint.route('/')
def index():
	users = db.session.query(User).all()

	for user in users:
		points = db.session.query(Point).filter(Point.created_at >= date.today()).filter_by(user_id=user.id).count()
		user.points_today = points

	ctx = {
        'users': users
    }

	return render_template('index.html', **ctx)

@home_blueprint.route('/give', methods=['GET', 'POST'])
def give():
	points_form = GivePoints()

	if points_form.validate_on_submit():
		# get the from user
		from_user = db.session.query(User).filter(User.name == points_form.from_user.data).first()

		# get the to user
		user = db.session.query(User).filter(User.name == points_form.user.data).first()
		if user != None and from_user != None:
			available_points = from_user.points_to_give
			if available_points - int(points_form.amount.data) < 0:
				flash('You don\'t have enough points')
			else:
				from_user.points_to_give -= int(points_form.amount.data)
				n = int(points_form.amount.data)
				for i in range(0,n):
					point = Point(user.id)
					db.session.add(point)
				flash('You gave points!')
				db.session.commit()
				return redirect( url_for('home.index') )
		else:
			flash('something went terribly wrong.')

	return render_template('give.html', form=points_form)

@home_blueprint.route('/user/<username>')
def profile(username):
	user = db.session.query(User).filter(User.name == username).first()
	if user != None:
		return render_template('profile.html', user=user)
	else:
		flash('That user does not exist.')
		return redirect(url_for('home.index'))
