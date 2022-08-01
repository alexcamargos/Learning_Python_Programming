#!/usr/bin/env python
#  encoding: utf-8
#
#  ------------------------------------------------------------------------------
#  Name: authors_repository.py
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
from sqlalchemy.exc import NoResultFound


class AuthorsRepository:
    """A class to handle authors repository."""

    @staticmethod
    def select_all():
        with DBConnection(dialect='sqlite', path='books.db', log_informational=False) as connection:
            try:
                return connection.session.query(Author) \
                    .join(Book) \
                    .with_entities(Author.id,
                                   Author.author,
                                   Book.title,
                                   Book.year_published) \
                    .all()
            except NoResultFound:
                return None
            except Exception as exception:
                connection.session.rollback()
                raise exception
