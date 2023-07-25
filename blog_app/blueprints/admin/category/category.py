from flask import Blueprint, render_template, request


category_bp = Blueprint(
    "category",
    __name__,
    template_folder="templates",
    url_prefix="/category",
)

from .forms import CategoryCreateAdminForm


from blog_app.models.Category import Category
from blog_app import db
from flask_login import login_required, current_user


@category_bp.route("/", methods=["GET", "POST"])
@login_required
def index():
    categories = Category.query.all()
    form = CategoryCreateAdminForm()
    form.parent_id.choices = [(0, 'None')] + [(category.id, category.name) for category in categories]


    if form.validate_on_submit():
        category = Category(
            name=form.name.data,
        )
        db.session.add(category)
        db.session.commit()
  

    return render_template(
        "admin/category/index.html",
        form=form,
        categories=categories,
        page_title="Category List",
    )