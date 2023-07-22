from blog_app import db
from blog_app.models.User import User
import os
import shutil


def get_user_by_id(user_id: int) -> User:
    return User.query.get(user_id)


def get_user_by_email(email: str) -> User:
    return User.query.filter_by(email=email).first()

def get_all_users() -> list[User]:
    return User.query.all()

def get_user_by_name(name: str) -> User:
    return User.query.filter_by(name=name).first()

def get_admin_users() -> list[User]:
    return User.query.filter_by(is_admin=True).all()

