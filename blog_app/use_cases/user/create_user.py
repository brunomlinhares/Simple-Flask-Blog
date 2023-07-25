from blog_app import db
from blog_app.models.User import User
from PIL import Image
import io
import os
def create_user(name: str, email: str, password: str,image_bytes: io.BytesIO):
    user = User(
        name=name,
        email=email,
        password=password,
    )

    db.session.add(user)
    db.session.commit()
    if not os.path.exists(user.get_folder_path()):
        os.makedirs(user.get_folder_path())
    image = Image.open(image_bytes)
    image.save(user.get_profile_image_path())

    return user






