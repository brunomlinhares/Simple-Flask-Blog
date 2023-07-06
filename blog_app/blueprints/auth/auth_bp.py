from flask import (
    Blueprint,
    render_template,
    flash,
    redirect,
    url_for,
)

auth_bp = Blueprint(
    "auth",
    __name__,
    template_folder="templates",
    url_prefix="/auth",
)


from .forms import UserRegisterForm, UserLoginForm


from blog_app.models.User import User
from blog_app import db

from flask_login import login_user, logout_user, login_required


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    form = UserRegisterForm()
    if form.validate_on_submit():
        user = User(
            name=form.name.data,
            email=form.email.data,
            password=form.password.data,
        )
        db.session.add(user)
        db.session.commit()
        flash("User created successfully.", "success")
        return redirect(url_for("auth.login"))
    
    return render_template("auth/register.html", form=form)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = UserLoginForm()
    if form.validate_on_submit():
        user:User = User.query.filter_by(email=form.email.data).first()
        
        if user and user.check_password(form.password.data):
            login_user(user)
            flash("Logged in successfully.", "success")
            return redirect(url_for("admin.index"))

    return render_template("auth/login.html", form=form)

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out successfully.", "info")
    return redirect(url_for("auth.login"))