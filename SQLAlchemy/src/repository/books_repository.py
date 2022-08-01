#!/usr/bin/env python
#  encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: books_repository.py
#  Version: 0.0.1
#  Summary: Leaning SQLAlchemy
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
#  ------------------------------------------------------------------------------

from database_connection.connection import DataBaseConnectionHandler as DBConnection
from models.authors import Author
from models.books import Book
from models.genres import Genre
from models.publishers import Publisher
from models.ratings import Rating
from models.types import Kind
from sqlalchemy.exc import NoResultFound


class BooksRepository:
    """A class to handle books repository."""

    @staticmethod
    def select_all():
        with DBConnection(dialect='sqlite', path='books.db', log_informational=False) as connection:
            try:
                return connection.session.query(Book) \
                    .join(Author, Genre, Kind, Publisher, Rating) \
                    .with_entities(Book.id,
                                   Book.title,
                                   Author.author,
                                   Genre.genre,
                                   Publisher.publisher,
                                   Book.year_published,
                                   Kind.type,
                                   Book.date_started,
                                   Book.date_finished,
                                   Rating.rating,
                                   Rating.meaning,
                                   Book.review) \
                    .all()
            except NoResultFound:
                return None
            except Exception as exception:
                connection.session.rollback()
                raise exception
