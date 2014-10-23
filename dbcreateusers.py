from app import db
from models import User

db.session.add(User("mike", "mike@hobiz.al", "nikeboy"))
db.session.add(User("admin", "admin@admin.com", "admin"))

db.session.commit()