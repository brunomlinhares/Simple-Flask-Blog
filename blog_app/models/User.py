from .. import db, login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import os
from blog_app.config import config
from flask import url_for

@login_manager.user_loader
def load_user(user_id: int):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    email = db.Column(db.String(200), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_admin = db.Column(db.Boolean, default=False)
    posts = db.relationship("Post", backref="author", lazy="dynamic")
    password_hash = db.Column(db.String(128), nullable=False)

    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password_hash = generate_password_hash(password)

    @property
    def is_active(self):
        return True

    @property
    def profile_image_url(self):
        return url_for("static", filename=f"upload/users/{self.id}/profile_image.webp")
    
    def __repr__(self) -> str:
        return f"<User {self.name}>"

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)
    
    def get_profile_image_path(self) -> str:
        return os.path.join(self.get_folder_path(),"profile_image.webp")

    def get_folder_path(self) -> str:
        return os.path.join(config.UPLOAD_FOLDER, "users",f"{self.id}")