from flask import flash, redirect, render_template, request, url_for, Blueprint
from flask.ext.login import login_user, login_required, logout_user
from form import LoginForm
from project import db
from project.models import User, bcrypt

users_blueprint = Blueprint(
	'users', __name__,
	template_folder='templates'
)

@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	form = LoginForm(request.form)
	if request.method == 'POST':
		if form.validate_on_submit():
			user = User.query.filter_by(name=request.form['user']).first()
			if user is not None and bcrypt.check_password_hash(user.password, request.form['password']):
				# session['logged_in'] = True
				login_user(user)
				flash('You just logged in!')
				return redirect(url_for('home.index'))
			else:
				error = 'Oops. That username or password is incorrect.'
	return render_template('login.html', form=form, error=error)

@users_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You were logged out.')
    return redirect(url_for('home.welcome'))