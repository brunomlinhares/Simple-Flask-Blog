from blog_app import db

from blog_app.config import config
from datetime import datetime


class Config(db.Model):
    __tablename__ = "configs"
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(200), unique=True)
    value = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value

    def __repr__(self):
        return f"<Config {self.key}>"
