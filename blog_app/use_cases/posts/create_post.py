from blog_app.models.Post import Post
from blog_app import db
from PIL import Image
import io
def create_post(title: str, content: str, user_id: int, image_bytes: io.BytesIO):
    post = Post(
        title=title,
        body=content,
        author_id=user_id,
    )

    db.session.add(post)
    db.session.commit()

    image = Image.open(image_bytes)
    image.save(post.get_post_image_path())

    return post