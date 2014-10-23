from flask import flash, redirect, render_template, request, session, url_for, Blueprint
from functools import wraps

users_blueprint = Blueprint(
	'users', __name__,
	template_folder='templates'
)

def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args, **kwargs)
		else:
			flash('You need to login first.')
			return redirect(url_for('login'))
	return wrap

@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['user'] != 'admin' or request.form['password'] != 'admin':
			error = 'Oops. That username or password is incorrect.'
		else:
			session['logged_in'] = True
			flash('You just logged in!')
			return redirect(url_for('home.index'))
	return render_template('login.html', error=error)

@users_blueprint.route('/logout')
@login_required
def logout():
	session.pop('logged_in', None)
	flash('You just logged out')
	return redirect(url_for('home.welcome'))
