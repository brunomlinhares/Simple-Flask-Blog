from .. import db
from datetime import datetime


class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    # posts = db.relationship("Post", backref="category", lazy="dynamic")
    parent_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=True)

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"<Category {self.name}>"
