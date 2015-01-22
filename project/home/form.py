from flask.ext.wtf import Form
from wtforms.fields import TextField

class GivePoints(Form):
	user = TextField()
	amount = TextField()