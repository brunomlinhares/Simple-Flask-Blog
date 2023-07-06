from .. import db
from datetime import datetime

class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    body = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, title:str,body:str,author_id:int):
        self.title = title
        self.body = body
        self.author_id = author_id
    
    def __repr__(self):
        return f"<Post {self.title}>"
