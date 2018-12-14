from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app(config=None) -> Flask:
    app: Flask = Flask(__name__)

    if config:
        app.config.from_object(config)

    db.init_app(app)
    db.create_all(app=app)

    return app
