#  #!/usr/bin/env python
#  encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: models.py
#  Version: 0.0.1
#  Summary: Leaning SQLAlchemy
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  ------------------------------------------------------------------------------

"""Models used by the application."""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Construct a base class for declarative class definitions.
Base = declarative_base()
metadata = Base.metadata


class Book(Base):
    """An entity to store books."""

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


class Author(Base):
    """An entity to store authors."""

    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    author = Column(String(255), nullable=False)
    books = Column(Integer, ForeignKey('books.id'))

    def __repr__(self):
        return f'Author(author={self.author}'


class Genre(Base):
    """An entity to store genres."""

    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True)
    genre = Column(String(128), unique=True)
    books = Column(Integer, ForeignKey('books.id'))

    def __repr__(self):
        return f'Genres(genre={self.genre})'


class Publisher(Base):
    """An entity to store publishers."""

    __tablename__ = 'publishers'

    id = Column(Integer, primary_key=True)
    publisher = Column(String(128))
    books = Column(Integer, ForeignKey('books.id'))

    def __str__(self):
        return f'Publishers(publisher={self.publisher})'


class Kind(Base):
    """An entity to store kinds.

    kinds are:
        Papel
        Ebook / Digital
        Audio Book

    """

    __tablename__ = 'kind'

    id = Column(Integer, primary_key=True)
    type = Column(String(32), unique=True)
    books = Column(Integer, ForeignKey('books.id'))

    def __repr__(self):
        return f'Kind(kind={self.type})'


class Rating(Base):
    """An entity to store ratings.

    The meaning of the rating is stored in the database as a string,
    but the rating is stored as an integer.

    ratings are:
         1 - não gostei
         2 - foi OK
         3 - gostei
         4 - gostei muito
         5 - foi incrível

    """

    __tablename__ = 'ratings'

    id = Column(Integer, primary_key=True)
    rating = Column(Integer, unique=True)
    meaning = Column(String(64))
    books = Column(Integer, ForeignKey('books.id'))

    def __repr__(self):
        return f'Ratings(rating={self.rating} - {self.meaning})'
