from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app(config=None) -> Flask:
    app: Flask = Flask(__name__)

    if config:
        app.config.from_object(config)

    db.init_app(app)
    db.create_all(app=app)

    from .view import get_url, save_url
    app.add_url_rule('/<key>', 'get_url', view_func=get_url, methods=['GET'])
    app.add_url_rule('/', 'save_url', view_func=save_url, methods=['POST'])

    return app
