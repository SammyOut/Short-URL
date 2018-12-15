from flask import request, redirect, Response, jsonify
from .model import UrlModel


def save_url():
    original_url = request.json['url']

    url_key = UrlModel(original_url).save_url()

    return jsonify({'url': 'http://localhost/' + url_key}), 201


def get_url(key) -> Response:
    url = UrlModel.get_url(key)

    if url is None:
        return Response('', 204)
    return redirect(url)
