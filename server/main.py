from flask import Flask

from app import create_app, db
from config import Config

app: Flask = create_app(Config)

if __name__ == '__main__':
    db.create_all(app=app)
    app.run('0.0.0.0', 80)
