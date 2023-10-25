from flask import Flask

from app.extensions import db, migrate
from config import db_uri


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

    db.init_app(app)
    migrate.init_app(app, db)

    from app.models import bp as models_bp
    app.register_blueprint(models_bp)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app
