#!/usr/bin/env python
#  encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: books.py
#  Version: 0.0.1
#  Summary: Leaning SQLAlchemy
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  ------------------------------------------------------------------------------

"""Models to represent information of books."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database_connection.base import Base


class Book(Base):
    """An entity to represent books."""

    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    author = relationship('Author', backref='Books', lazy='dynamic')
    genre = relationship('Genre', backref='Books', lazy='dynamic')
    publisher = relationship('Publisher', backref='Books', lazy='dynamic')
    year_published = Column(Integer)
    kind = relationship('Kind', backref='Books', lazy='dynamic')
    date_started = Column(Integer)
    date_finished = Column(Integer)
    rating = relationship('Rating', backref='Books', lazy='dynamic')
    review = Column(String)

    def __repr__(self):
        return f'Books(id={self.id}, title={self.title}, author={self.author}'
