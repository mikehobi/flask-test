from flask.ext.wtf import Form
from wtforms.fields import TextField

class GivePoints(Form):
	user = TextField()
	from_user = TextField()
	amount = TextField()