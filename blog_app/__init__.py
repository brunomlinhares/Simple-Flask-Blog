import os


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
    )

    if test_config is None:
        app.config.from_mapping(
            WFT_CSRF_TIME_LIMIT=7200,
            SQLALCHEMY_DATABASE_URI="postgresql://postgres:9uIq70zIomlkHrXY@db.davysblfsvixrnjdqvif.supabase.co:5432/postgres",
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
        )
    else:
        app.config.from_mapping(test_config)

    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)


    from .models.User import User
    from .models.Post import Post

    from .blueprints.admin.admin_bp import admin_bp
    
    app.register_blueprint(admin_bp)



    return app
