from flask import Flask, request, redirect, Response

from app import create_app
from config import Config
from model import UrlModel

app: Flask = create_app(Config)


@app.route('/', methods=['POST'])
def post() -> Response:
    original_url = request.json['url']

    url_key = UrlModel(original_url).save_url()

    return Response('http://localhost/' + url_key, 201)


@app.route('/<key>', methods=['GET'])
def get(key) -> Response:
    url = UrlModel.get_url(key)

    if url is None:
        return Response('', 204)
    return redirect(url)


if __name__ == '__main__':
    app.run('0.0.0.0', 80)
