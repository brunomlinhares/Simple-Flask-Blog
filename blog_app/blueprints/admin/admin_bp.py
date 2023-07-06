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
admin_bp.register_blueprint(user_bp)
admin_bp.register_blueprint(post_bp)

@admin_bp.route("/")
@login_required
def index():
    return render_template("admin/index.html")