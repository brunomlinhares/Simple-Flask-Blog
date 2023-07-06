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

from blog_app.models.User import User
from blog_app import db

@user_bp.route("/",methods=["GET","POST"])
def index():
    form = UserRegisterAdminForm()
    if form.validate_on_submit():
        user = User(
            name=form.name.data,
            email=form.email.data,
        )
        db.session.add(user)
        db.session.commit()
    users = User.query.all()




    
    return render_template("admin/user/index.html", form=form, users=users,page_title="User List")