from flask import Flask

from .app import create_app
from .config import Config

app: Flask = create_app(Config)

if __name__ == '__main__':
    app.run('0.0.0.0', 80)
