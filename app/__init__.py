from flask import Flask

from config import Config
from app.extensions import db, migrate


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.models import bp as models_bp
    app.register_blueprint(models_bp)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app
