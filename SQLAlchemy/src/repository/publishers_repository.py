#!/usr/bin/env python
#  encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: publishers_repository.py
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
from models.publishers import Publisher
from sqlalchemy.exc import NoResultFound


class PublishersRepository:
    """A class to handle publishers repository."""

    @staticmethod
    def select_all():
        with DBConnection(dialect='sqlite', path='books.db', log_informational=False) as connection:
            try:
                return connection.session.query(Publisher) \
                    .join(Book) \
                    .with_entities(Publisher.id,
                                   Publisher.publisher,
                                   Publisher.books,
                                   Book.id,
                                   Book.title,
                                   Author.author,
                                   ) \
                    .all()
            except NoResultFound:
                return None
            except Exception as exception:
                connection.session.rollback()
                raise exception
