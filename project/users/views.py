from flask import flash, redirect, render_template, request, url_for, Blueprint
from flask.ext.login import login_user, login_required, logout_user, current_user
from form import LoginForm, SignupForm, PostForm
from project import app, db
from project.models import User, BlogPost, bcrypt

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

@users_blueprint.route('/signup', methods=['GET', 'POST'])
def signup():
	form = SignupForm()
   	if request.method == 'POST':
	    if form.validate() == False:
	     	return render_template('signup.html', form=form)
	    else:
			newuser = User(form.user.data, form.email.data, form.password.data)
			db.session.add(newuser)
			db.session.commit()
			return redirect(url_for('home.index'))	
	elif request.method == 'GET':
  		return render_template('signup.html', form=form)

@users_blueprint.route('/post', methods=['GET', 'POST'])
@login_required
def new_post():
	form = PostForm()
	if request.method == 'POST':
		if form.validate() == False:
			return render_template('post.html', form=form)
		else: 
			newpost = BlogPost(form.title.data, form.description.data, current_user.id)
			db.session.add(newpost)
			db.session.commit()
			return redirect(url_for('home.index'))
	elif request.method == 'GET':
		return render_template('post.html', form=form)