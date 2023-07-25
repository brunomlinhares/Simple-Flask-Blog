from flask import (
    Blueprint,
    render_template,
    request
)

user_bp = Blueprint(
    "user", __name__,
    template_folder="templates",
    url_prefix="/user",
)

from .forms import UserRegisterAdminForm
from flask_login import login_required
from blog_app.models.User import User
from blog_app import db

from blog_app.use_cases.user.query_user import get_all_users
from blog_app.use_cases.user.delete_user import delete_user
from blog_app.use_cases.user.update_user import update_user,update_user_image
from blog_app.use_cases.user.create_user import create_user
from blog_app.use_cases.user.query_user import get_user_by_id
import io
from flask import url_for,redirect

@user_bp.route("/",methods=["GET","POST"])
@login_required
def index():
    form = UserRegisterAdminForm()
    if form.validate_on_submit():
        profile_image = request.files.get("profile_image")
        if profile_image:
            user = create_user(
                name=form.name.data,
                email=form.email.data,
                password=form.password.data,
                image_bytes=io.BytesIO(profile_image.read())
            )
    users = get_all_users()
    META = {
        "have_header":True,
        "page_title":"User List",
        "page_description":"User List",
        "action": "Create new user",
        "action_url": url_for("admin.user.index")

    }
    return render_template(
        "admin/user/index.html", 
        META=META,
        page_title="User List",
        form=form, 
        users=users,
        )


@user_bp.route("/<int:user_id>/",methods=["GET","POST"])
@login_required
def edit(user_id):
    user = get_user_by_id(user_id)
    form = UserRegisterAdminForm(obj=user)
    if form.validate_on_submit():
        profile_image = request.files.get("profile_image")
        user = update_user(
            user=user,
            name=form.name.data,
            email=form.email.data,
            password=form.password.data,
        )
        if profile_image:
            update_user_image(user=user,image_bytes=io.BytesIO(profile_image.read()))
    return render_template("admin/user/edit.html", form=form, user=user,page_title="Edit User")


@user_bp.route("/<int:id>/delete",methods=["GET","POST"])
@login_required
def delete(id):
    user = get_user_by_id(id)
    delete_user(user)
    return redirect(url_for("admin.user.index"))