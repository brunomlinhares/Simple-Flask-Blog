from blog_app import db
from blog_app.models.User import User
from PIL import Image

def create_user(name: str, email: str, password: str,image_bytes: bytes):
    user = User(
        name=name,
        email=email,
        password=password,
    )

    db.session.add(user)
    db.session.commit()

    image = Image.open(image_bytes)
    image.save(user.get_profile_image_path())

    return user





