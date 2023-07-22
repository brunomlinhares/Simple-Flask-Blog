import os

class Config:
    UPLOAD_FOLDER = os.path.join("blog_app","static", "upload")
    SECRET_KEY="dev",
    MAX_CONTENT_LENGTH = 1024 * 1024
    ALLOWED_IMAGE_EXTENSIONS = ["png", "jpg", "jpeg", "gif"]
    MAX_IMAGE_FILESIZE = 0.5 * 1024 * 1024

config = Config()