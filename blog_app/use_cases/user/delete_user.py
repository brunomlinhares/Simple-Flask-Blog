from blog_app import db
from blog_app.models.User import User
import os
import shutil

def delete_user(user: User) -> bool:
    if os.path.exists(user.get_folder_path()):
        print("Deleting user folder")
        shutil.rmtree(user.get_folder_path())
    db.session.delete(user)
    db.session.commit()
    return True