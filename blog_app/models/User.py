from .. import db, login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id:int):
    return User.query.get(user_id)

class User(db.Model,UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    email = db.Column(db.String(200), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_admin = db.Column(db.Boolean, default=False)
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    password_hash = db.Column(db.String(128), nullable=False)

    def __init__(self, name:str,email:str,password:str):
        self.name = name
        self.email = email
        self.password_hash = generate_password_hash(password)
    
    @property
    def is_active(self):
        return True
    def __repr__(self):
        return f"<User {self.name}>"
    
    def check_password(self, password:str):
        return check_password_hash(self.password_hash, password)