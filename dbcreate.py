from app import db
from models import BlogPost

# create the db homie
db.create_all()


# insert
db.session.add(BlogPost("Good", "Bad"))
db.session.add(BlogPost("Great", "Dandy"))
db.session.add(BlogPost("Good", "Bad"))



# commit 
db.session.commit()