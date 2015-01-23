import json
import requests
from datetime import date

from flask import flash, redirect, render_template, url_for, Blueprint, request

from project import db, slack
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
		points = db.session.query(Point).filter(Point.created_at >= date.today()).filter_by(user_id=user.id).count()
		user.points_today = points

	ctx = {
        'users': users
    }

	return render_template('index.html', **ctx)

@home_blueprint.route('/give', methods=['GET', 'POST'])
@slack.command('points', token='qm76q99wz5FNKiNvoYCVkfnw', team_id='T0001', methods=['POST'])
def response():
	channel = request.form['channel_name']
	if channel == 'directmessage':
		return slack.response('can\'t give POINTS in direct message, public generosity only!')
	if not request.form['text']:
		return slack.response('type "/points [user] [amount]" to give <http://hobiz.herokuapp.com/|POINTS!>')
	from_user = request.form['user_name']
	text = request.form['text'].split()
	from_user = db.session.query(User).filter(User.name == from_user).first()
	if text[0] == 'help':
		return slack.response('figure out yourself, just kidding <http://hobiz.herokuapp.com/halp|click here bro>')
	if text[0] == 'wut':
		return slack.response('what do you mean wut? it\'s POINTS')
	if text[0] == 'img':
		if not text[1]:
			return slack.response('are you trying to change your image bro?? type /points img [image url]')
		from_user.img_url = text[1]
		db.session.commit()
		return slack.response('you just changed your image, congratz man')
	to_user = text[0]
	to_user = db.session.query(User).filter(User.name == to_user).first()
	if to_user is None:
		return slack.response('wrong. make sure you do user before points.')
	points = int(text[1])
	available_points = from_user.points_to_give
	if available_points == 0:
		return slack.response('you don\'t have any points left today, like literally zero dude')
	if available_points - points < 0:
		return slack.response('you don\'t have enough points! you have {} left for today.'.format(available_points))
	from_user.points_to_give -= points
	n = points
	for i in range(0,n):
		point = Point(to_user.id)
		db.session.add(point)
	db.session.commit()
	webhook_url = 'https://hooks.slack.com/services/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'
	payload = {
        'text': '{} just gave {} POINT{} to {}!!!!!!! <http://hobiz.herokuapp.com/|View the points board>'.format(from_user.name,points,'' if points == 1 else 'S',to_user.name),
		'channel': '#' + channel
    }
	req = requests.post(webhook_url, data={'payload': json.dumps(payload)})
	if req.status_code != 200:
 		return slack.response('Error: {}'.format(req.content))
	return slack.response('')

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