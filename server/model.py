from typing import Union

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, Sequence, Text
from sqlalchemy.orm import sessionmaker

from server.base62 import *


engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()


class UrlModel(Base):
    __tablename__ = 'url'

    id: int = Column(Integer, Sequence('url_id_seq'), primary_key=True)
    url: str = Column(Text)

    def __init__(self, url: str):
        self.url = url

    def __repr__(self):
        return f'<URL({self.id}, {self.url}>'


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


def is_existed_url(url: str) -> Union[str, None]:
    url = session.query(UrlModel).filter_by(url=url).first()
    if url:
        return encrypt_base62(url.id)
    return None


def save_url(url: str) -> str:
    exist_url_key = is_existed_url(url)
    if exist_url_key:
        return exist_url_key

    url: UrlModel = UrlModel(url)
    session.add(url)
    session.commit()

    return encrypt_base62(url.id)


def get_url(key: str) -> Union[str, None]:
    index = decrypt_base62(key)

    url: UrlModel = session.query(UrlModel).filter_by(id=index).first()

    if url:
        return url.url
    return None
