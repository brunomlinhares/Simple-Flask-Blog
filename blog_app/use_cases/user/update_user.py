from blog_app import db
from blog_app.models.User import User

from PIL import Image
from werkzeug.security import generate_password_hash
import io
def update_user_image(user: User, image_bytes: io.BytesIO) -> User:
    image = Image.open(image_bytes)
    image.save(user.get_profile_image_path())
    return user

def update_user(user: User, name: str, email: str, password: str,image:bytes | None = None) -> User:
    user.name = name
    user.email = email
    user.password = generate_password_hash(password)
    db.session.commit()
    if image:
        update_user_image(user,image)
    return user

def set_user_admin(user: User, is_admin: bool) -> User:
    user.is_admin = is_admin
    db.session.commit()
    return user



