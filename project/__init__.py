#################
#### imports ####
#################

from flask import Flask, render_template, redirect, url_for
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

# register our blueprints
app.register_blueprint(users_blueprint)
app.register_blueprint(home_blueprint)

@app.errorhandler(403)
def server_error_403(error):
    return redirect(url_for('home.index'))

@app.errorhandler(404)
def server_error_404(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error_500(error):
    return render_template('500.html'), 500