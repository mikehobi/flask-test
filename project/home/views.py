from flask import flash, redirect, render_template, url_for, Blueprint

from project import db
from project.models import User, Point

from .form import GivePoints

home_blueprint = Blueprint(
	'home', __name__,
	template_folder='templates'
)

# ROUTES

@home_blueprint.route('/')
def index():
	return render_template('index.html')

@home_blueprint.route('/give', methods=['GET', 'POST'])
def give():
	points_form = GivePoints()

	if points_form.validate_on_submit():
		user = db.session.query(User).filter(User.name == points_form.user.data).first()
		if user != None:
			n = int(points_form.amount.data)
			for i in range(1,n):
				point = Point(user.id)
				db.session.add(point)
			db.session.commit()
			flash('you gave points!')
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
