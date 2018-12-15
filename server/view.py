from flask import request, redirect, Response, jsonify, current_app
from server.model import UrlModel


def save_url():
    original_url = request.json['url']

    url_key = UrlModel(original_url).save_url()

    if current_app.config['SERVER_NAME'] is not None:
        base_url = current_app.config['SERVER_NAME'] + '/'
    else:
        base_url = 'localhost/'

    return jsonify({'url': 'http://' + base_url + url_key}), 201


def get_url(key) -> Response:
    url = UrlModel.get_url(key)

    if url is None:
        return Response('', 204)
    return redirect(url)
