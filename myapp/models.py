#models 
from myapp import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
#allows to set up isAuthenticate etc 
from flask_login import UserMixin
from datetime import datetime

#login management 
# allows us to use this in templates for isUser stuff 
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

#going to use this in our login view 
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f"Username {self.username}"

# trail model
class Trail(db.Model):
    __tablename__ = 'trail'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    trail_name = db.Column(db.String(140), nullable=False)
    distance = db.Column(db.Integer, nullable=False)
    review = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=False)

    def __init__(self, trail_name, distance, review, comment):
        self.trail_name = trail_name
        self.distance = distance
        self.review = review
        self.comment = comment

    def __repr__(self):
        return f"Trail ID: {self.id} -- Date: {self.date} --- Trail Name: {self.trail_name}"
