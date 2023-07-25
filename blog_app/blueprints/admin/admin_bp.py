from flask import (
    Blueprint,
    render_template,
)
from flask_login import login_required

admin_bp = Blueprint(
    "admin", 
    __name__,
    url_prefix="/admin",
)

from .user.user import user_bp
from .posts.post import post_bp
from .category.category import category_bp
admin_bp.register_blueprint(user_bp)
admin_bp.register_blueprint(post_bp)
admin_bp.register_blueprint(category_bp)



@admin_bp.route("/")
@login_required
def index():
    return render_template("admin/index.html")





from blog_app.extensions.menu_builder.MenuBuilder import MenuBuilder

@admin_bp.context_processor
def inject_menu():
    menu_builder = MenuBuilder()
    menu_builder.add_menu_item("Dashboard", "admin.index")
    menu_builder.add_menu_item("Configs", "admin.index")
    menu_builder.add_menu_item("Posts", "admin.user.index")
    menu_builder.add_child("Posts", "Create Post", "admin.user.index")
    menu_builder.add_child("Posts", "List Posts", "admin.user.index")

    menu_builder.add_menu_item("Users", "admin.user.index")
    menu_builder.add_child("Users", "Create User", "admin.user.index")
    menu_builder.add_child("Users", "List Users", "admin.user.index")

    menu_builder.add_menu_item("Categories", "admin.user.index")
    menu_builder.add_child("Categories", "Create Category", "admin.user.index")
    menu_builder.add_child("Categories", "List Categories", "admin.user.index")

    return dict(menu=menu_builder.get_menu())

from blog_app.use_cases.config.create_base_config import create_default_configs
from blog_app.use_cases.config.create_base_config import get_all_configs

@admin_bp.context_processor
def inject_configs():
    configs = get_all_configs()
    if not configs:
        configs = get_all_configs()
    configs = {config.key:config.value for config in configs}
    return dict(configs=configs)