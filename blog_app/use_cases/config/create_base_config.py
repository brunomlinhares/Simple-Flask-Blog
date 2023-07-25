
from blog_app.models.Config import Config

from blog_app import db



def get_all_configs():
    return Config.query.all()

def get_config_by_key(key: str):
    return Config.query.filter_by(key=key).first()

def update_config(config: Config, value: str):
    config.value = value
    db.session.commit()
    return config


def create_config(key: str, value: str):
    config = Config(
        key=key,
        value=value,
    )
    db.session.add(config)
    db.session.commit()
    return config


def delete_config(config: Config):
    db.session.delete(config)
    db.session.commit()
    return config


def get_config_by_id(config_id: int):
    return Config.query.filter_by(id=config_id).first()


def create_default_configs():
    CONFIGS = [
        ("site_name", "My Blog"),
        ("site_description", "My Blog Description"),
        ("main_color_name","emerald"),
        ("secondary_color_name","amber"),
    ]
    for key, value in CONFIGS:
        config = get_config_by_key(key)
        if not config:
            create_config(key=key, value=value)
        