from typing import Union

from .app import db

from .base62 import *


class UrlModel(db.Model):
    __tablename__ = 'urltbl'

    id: int = db.Column(db.Integer, db.Sequence('url_id_seq'), primary_key=True)
    url: str = db.Column(db.Text)

    def __init__(self, url: str):
        self.url = url

    def __repr__(self):
        return f'<URL({self.id}, {self.url}>'

    def is_exist_url(self) -> Union[str, None]:
        url = db.session.query(UrlModel).filter_by(url=self.url).first()
        if url:
            return encrypt_base62(url.id)
        return None

    def save_url(self) -> str:
        exist_url_key = self.is_exist_url()
        if exist_url_key:
            return exist_url_key

        db.session.add(self)
        db.session.commit()

        return encrypt_base62(self.id)

    @staticmethod
    def get_url(key: str) -> Union[str, None]:
        index = decrypt_base62(key)

        url: UrlModel = db.session.query(UrlModel).filter_by(id=index).first()

        if url:
            return url.url
        return None
