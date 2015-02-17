#################
#### imports ####
#################

import json
import random
import requests

from flask import Flask, render_template, url_for, request
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from flask_slack import Slack

import os

################
#### config ####
################

app = Flask(__name__)
bcrypt = Bcrypt(app)
slack = Slack(app)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from project.users.views import users_blueprint
from project.home.views import home_blueprint
from project.models import User, Point

# register our blueprints
app.register_blueprint(users_blueprint)
app.register_blueprint(home_blueprint)
app.add_url_rule('/give', view_func=slack.dispatch)

@slack.command('points', token=app.config['SLACK_TOKEN'], team_id=app.config['TEAM_ID'], methods=['POST'])
def response(**kwargs):
	webhook_url = app.config['WEBHOOK']
	channel = request.form['channel_name']
	if channel == 'directmessage':
		return slack.response('can\'t give POINTS in direct message, public generosity only!')
	if not request.form['text']:
		return slack.response('type "/points [user] [amount]" to give <{}/|POINTS!>'.format(url_for('home.index', _external=True)))
	from_user = request.form['user_name']
	text = request.form['text'].split()
	from_user = db.session.query(User).filter(User.name == from_user).first()
	available_points = from_user.points_to_give
	if text[0] == 'help':
		return slack.response('figure out yourself, just kidding <{}/halp|click here bro>'.format(url_for('home.index', _external=True)))
	if text[0] == 'why':
		return slack.response('Because I said so.')
	if text[0] == 'balance':
		return slack.response('You have {} left for today.'.format(available_points))
	if text[0] == 'img':
		if not text[1]:
			return slack.response('are you trying to change your image bro?? type /points img [image url]')
		from_user.img_url = text[1]
		db.session.commit()
		return slack.response('you just changed your image, congratz man')
	try:
		points = int(text[1])
	except:
		return slack.response('seriously? don\'t make me do that kind of math')
	to_user = text[0]
	to_user = db.session.query(User).filter(User.name == to_user).first()
	if to_user is None:
		return slack.response('wrong. make sure you do [user] before [points].')
	if points <= 0:
		return slack.response('chill bro, points is about positivity, man')
	if available_points == 0:
		return slack.response('you don\'t have any points left today, like literally zero dude')
	if available_points - points < 0:
		return slack.response('you don\'t have enough points! you have {} left for today.'.format(available_points))
	# if to_user == from_user == db.session.query(User).filter(User.name == 'hakeem').first():
	if to_user == from_user:
		rand = random.randrange(0, db.session.query(User).count()) 
		rand_user = db.session.query(User)[rand]
		from_user.points_to_give -= 1
		point = Point(rand_user.id)
		db.session.add(point)
		db.session.commit()
		payload = {
	        'text': '@{} just tried to give himself {} point{}! Instead we\'ll randomly give ONE point to @{}!'.format(from_user.name,points,'' if points == 1 else 's',rand_user.name),
			'channel': '#' + channel
	    }
		req = requests.post(webhook_url, data={'payload': json.dumps(payload)})
		if req.status_code != 200:
	 		return slack.response('Error: {}'.format(req.content))
		return slack.response('')
	from_user.points_to_give -= points
	n = points
	for i in range(0,n):
		point = Point(to_user.id)
		db.session.add(point)
	db.session.commit()
	payload = {
        'text': '@{} just gave {} POINT{} to @{}!!!!!!! <{}|View the points board>'.format(from_user.name,points,'' if points == 1 else 'S',to_user.name, url_for('home.index', _external=True)),
		'channel': '#' + channel
    }
	req = requests.post(webhook_url, data={'payload': json.dumps(payload)})
	if req.status_code != 200:
 		return slack.response('Error: {}'.format(req.content))
	return slack.response('')

@app.errorhandler(403)
def server_error_403(error):
    return 'wut'

@app.errorhandler(404)
def server_error_404(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error_500(error):
    return 'something went terribly wrong, tell @mike'