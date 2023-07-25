from blog_app import db
from blog_app.config import config
from datetime import datetime
import os

from flask import url_for
class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    body = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def __init__(self, title: str, body: str, author_id: int):
        self.title = title
        self.body = body
        self.author_id = author_id

    def __repr__(self):
        return f"<Post {self.title}>"
    
    def get_post_image_path(self):
        return os.path.join(config.UPLOAD_FOLDER, f"post_{self.id}.png")
    
    def get_post_image_url(self):
        return url_for("static", filename=self.get_post_image_path())
