from flask import Blueprint, render_template, request


post_bp = Blueprint(
    "post",
    __name__,
    template_folder="templates",
    url_prefix="/post",
)

from .forms import PostCreateAdminForm


from blog_app.models.Post import Post
from blog_app import db
from flask_login import login_required, current_user


@post_bp.route("/", methods=["GET", "POST"])
@login_required
def index():
    form = PostCreateAdminForm()
    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            body=form.body.data,
            author_id=current_user.id,
        )
        db.session.add(post)
        db.session.commit()
    posts = Post.query.all()

    return render_template(
        "admin/post/index.html", form=form, posts=posts, page_title="Post List"
    )
