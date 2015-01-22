from flask import flash, redirect, url_for, Blueprint

users_blueprint = Blueprint(
	'users', __name__,
	template_folder='templates'
)

@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
	flash('You don\'t have to login, you think I would make login functionality on this app?')
	return redirect(url_for('home.index'))

@users_blueprint.route('/logout', methods=['GET', 'POST'])
def logout():
	flash('Were you ever logged in??')
	return redirect(url_for('home.index'))